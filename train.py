from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    
    model.train(data="dataset.yml",  epochs=5, batch=4, optimizer="Adam")




