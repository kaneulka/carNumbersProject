# dicsountProject

1. Подготовил базу из картинок и ПО (Python 3.6, tensorflow==1.14 lower then 2, keras 2.2.4 or lower)
2. Разметил и расширил их с помощью проекта - https://app.roboflow.com/edu/car-numbers-8tl4j/1
3. Сделал копию репозитория для Windows - https://github.com/roboflow-ai/keras-yolo3
4. Запустил train.py с настройками к modelTraining\keras-yolo3-master\Data\test_annotations.txt и modelTraining\keras-yolo3-master\Data\test_classes.txt согласно следующей ссылки - https://colab.research.google.com/drive/1ByRi9d6_Yzu0nrEKArmLMLuMaZjYfygO#scrollTo=4hBFndz8VeI6
5. Ссылка на обученую модель нужно расположить по 
            ~~("modelTraining\keras-yolo3-master\logs\000\trained_weights_stage_1.h5":   
            https://drive.google.com/file/d/1UEsQNRBv1H1K44DEuIcTfAtxtykpaS6n/view?usp=share_link)~~
            (Модель:https://drive.google.com/file/d/1cUimnMvj4cfVwf_F_SM9Qyznvb80XeIj/view?usp=share_link
            Путь: config\lapi.weights и modelTraining\config\lapi.weights)
6. Установка tesseract - https://github.com/UB-Mannheim/tesseract/wiki и установка git - https://github.com/madmaze/pytesseract
7.

Полезные ресурсы:

1. https://habr.com/ru/post/439330/ https://habr.com/ru/post/421299/
2. https://habr.com/ru/post/594401/
3. https://docs.ultralytics.com/tutorials/train-custom-datasets/
4. https://github.com/ultralytics/yolov5/releases
5. https://colab.research.google.com/drive/1spi6jlCnbFWSrp5rv5NTPUxgr5DODaX8?usp=sharing#scrollTo=10g9FTIpxK2P
6. https://colab.research.google.com/drive/1O6PS6v6IE3zaAdPORC9Z1qWDwRgah99A?usp=sharing#scrollTo=1udoJrnAX9pX
