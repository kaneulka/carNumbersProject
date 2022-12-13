from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

base_dir = os.path.dirname(os.path.abspath(__file__))
image = base_dir + r'\tmp\test.PNG'
d = Image.open(image)
preprocess = "thresh"

# загрузить образ и преобразовать его в оттенки серого
image = cv2.imread(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# проверьте, следует ли применять пороговое значение для предварительной обработки изображения

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# если нужно медианное размытие, чтобы удалить шум
elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

# сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR
filename_dir = base_dir +"\gray\{}.png".format(os.getpid())
cv2.imwrite(filename_dir, gray)

# загрузка изображения в виде объекта image Pillow, применение OCR, а затем удаление временного файла
text = pytesseract.image_to_string(Image.open(filename_dir))
print(text)
os.remove(filename_dir)

# показать выходные изображения
cv2.imshow("Image", image)
cv2.imshow("Output", gray)