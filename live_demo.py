import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Ошибка: не удалось открыть камеру.")
    exit()

print("Выйди в окно видео и держи 'q' для выхода.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # imgsz=320 — втрое быстрее на CPU, точности для крупных объектов хватает
    results = model.predict(source=frame, conf=0.3, imgsz=320, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("Desk Objects Detection", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()