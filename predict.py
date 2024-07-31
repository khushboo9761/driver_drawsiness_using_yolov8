import cv2
from ultralytics import YOLO

if __name__== '__main__':
    img_url = f'datasets/images/validation/awake_2024-07-31_00-45-09.jpg' 
    img = cv2.imread(img_url)

    model = YOLO(f"runs/detect/train7/weights/last.pt")

    pred = model.predict(img)[0]
    pred= pred.plot()

    cv2.imwrite(f"prediction.jpg", pred)
