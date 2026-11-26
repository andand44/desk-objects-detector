from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
results = model.predict(
    source="detect-simple-desk-objects-2/test/images",
    conf=0.5,
    save=True  # сохранит размеченные картинки в runs/detect/predict
)

for r in results:
    for box in r.boxes:
        name = model.names[int(box.cls)]
        print(f"{name}: уверенность {float(box.conf):.2f}")
