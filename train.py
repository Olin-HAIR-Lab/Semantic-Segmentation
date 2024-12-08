from ultralytics import YOLO

model = YOLO("yolo 11n-seg.pt")
model.train(data="config.yaml", epochs=100)

#print(model.names)
#print("Number of classes:", len(model.names))
