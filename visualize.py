import os
import cv2

# Пути
data_path = "detect-simple-desk-objects-2"
img_folder = os.path.join(data_path, "train", "images")
lbl_folder = os.path.join(data_path, "train", "labels")

CLASS_NAMES = ["keyboard", "mouse", "pen"]

# Список картинок и берём первую
images = [f for f in os.listdir(img_folder) if f.endswith((".jpg", ".jpeg", ".png"))]
if not images:
    print("Картинки не найдены!")
    exit()

img_name = images[0]  # можно поменять индекс: images[5], images[10] и т.д.
img_path = os.path.join(img_folder, img_name)
lbl_path = os.path.join(lbl_folder, os.path.splitext(img_name)[0] + ".txt")

# Читаем картинку
img = cv2.imread(img_path)
h, w, _ = img.shape

# Читаем разметку и рисуем рамки
boxes = []
if os.path.exists(lbl_path):
    with open(lbl_path, "r") as f:
        for line in f:
            parts = list(map(float, line.strip().split()))
            if len(parts) >= 5:
                class_id, cx, cy, bw, bh = parts[:5]
                x1 = int((cx - bw / 2) * w)
                y1 = int((cy - bh / 2) * h)
                x2 = int((cx + bw / 2) * w)
                y2 = int((cy + bh / 2) * h)
                boxes.append((class_id, x1, y1, x2, y2))
else:
    print(f"Файл разметки не найден: {lbl_path}")

for class_id, x1, y1, x2, y2 in boxes:
    color = (0, 255, 0)
    name = CLASS_NAMES[int(class_id)]
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    cv2.putText(img, name, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

print(f"Картинка: {img_name}, объектов найдено: {len(boxes)}")
print("Нажми любую клавишу в окне с картинкой, чтобы закрыть.")

cv2.imshow("Разметка", img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()

if key == 27:  # ESC
    print("Выход")

cv2.waitKey(0)
cv2.destroyAllWindows()
