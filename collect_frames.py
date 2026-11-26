import cv2
import os
from datetime import datetime

out_dir = "new_photos"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Камера не открылась")
    exit()

count = len([f for f in os.listdir(out_dir) if f.endswith(".jpg")])
print(f"Уже сохранено: {count}. Пробел — снять кадр, q — выход.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Съёмка", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(" "):
        name = datetime.now().strftime("photo_%Y%m%d_%H%M%S_%f")[:-3] + ".jpg"
        cv2.imwrite(os.path.join(out_dir, name), frame)
        count += 1
        print(f"Сохранено: {name} (всего {count})")
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
