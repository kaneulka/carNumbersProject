import sqlite3
import cv2
import numpy as np
from PIL import Image
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def cut_image(img, x, y, x_plus_w, y_plus_h):
    image = Image.open("inputImages/" + img)
    image_masked = image.crop((x, y, x_plus_w, y_plus_h))
    image_masked.save( "outputImages/" + img + "_masked.jpg")

def get_output_layers(net):
    layer_names = net.getLayerNames()
    try:
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    except:
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

    

def work_with_image(imageArg):
    
    def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
        label = str(classes[class_id])
        color = COLORS[class_id]
        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
    image = cv2.imread("inputImages/" + imageArg)
    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392
    classes = None
    with open(configArg, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
    net = cv2.dnn.readNet(weightsArg, configArg)
    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(get_output_layers(net))
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    for i in indices:
        try:
            box = boxes[i]
        except:
            i = i[0]
            box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
        cut_image(imageArg, round(x), round(y), round(x+w), round(y+h))
    cv2.imwrite("outputImages/" + imageArg + "_object-detection.jpg", image)
    cv2.destroyAllWindows()


con = sqlite3.connect("TestDB") 
cursor = con.cursor()
getUserInfo = con.cursor()
query = "SELECT * FROM users INNER JOIN cars ON users.userId = cars.userId;"
cursor.execute(query)
data = cursor.fetchall()

carNumbers = []
for line in data:
    carNumbers.append(line[4])

configArg = "config/darknet-yolov3.cfg"
weightsArg = "config/lapi.weights"
classesArg = "config/classes.names"

for imageName in os.listdir("inputImages"):
    image = imageName
    work_with_image(image)
    
    # загрузить образ и преобразовать его в оттенки серого
    cutImage = "outputImages/" + image + "_masked.jpg"
    converCutImage = np.array(Image.open(cutImage)) #"outputImages/" + image + "_masked.jpg"
    preprocess = "thresh"
    gray = cv2.cvtColor(converCutImage, cv2.COLOR_BGR2GRAY)
    
    # проверьте, следует ли применять пороговое значение для предварительной обработки изображения
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # если нужно медианное размытие, чтобы удалить шум
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)
        
    # сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR
    filename_dir = "outputImages/gray/{}.png".format(os.getpid())
    cv2.imwrite(filename_dir, gray)
    
    # загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
    text = pytesseract.image_to_string(Image.open(filename_dir))
    print(text)
    os.remove(filename_dir)
    #os.remove(cutImage)

    #Поиск номера в базе
    carIsExist = ""
    try:
        query = "SELECT * FROM users INNER JOIN cars ON users.userId = cars.userId WHERE carNumber={text};"
        getUserInfo.execute(query)
        carData = getUserInfo.fetchall()
        print(carData)
    except:
        print("Car not in database!")