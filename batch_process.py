import os
import csv
from pathlib import Path
from ultralytics import YOLO

# Инициализация модели
model = YOLO("runs/detect/train/weights/best.pt")

# Папки
input_dir = Path("detect-simple-desk-objects-2/test/images")
output_dir = Path("output/images")
output_dir.mkdir(parents=True, exist_ok=True)

results_csv = "output/detection_report.csv"

# Заголовки CSV
csv_headers = ["filename", "class", "confidence", "x_min", "y_min", "x_max", "y_max"]

with open(results_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)

    # Проход по всем картинкам
    for img_path in input_dir.glob("*.jpg"):
        results = model.predict(source=str(img_path), conf=0.5, save=True, project="output", name="images")
        
        # Сохраняем результаты в CSV
        for r in results:
            if r.boxes is not None:
                for box in r.boxes:
                    cls_id = int(box.cls)
                    conf = float(box.conf)
                    # xyxy — тензор [1, 4], берём первую (единственную) строку
                    x1, y1, x2, y2 = box.xyxy[0].tolist()

                    row = [
                        img_path.name,
                        model.names[cls_id],
                        f"{conf:.3f}",
                        f"{x1:.2f}", f"{y1:.2f}",
                        f"{x2:.2f}", f"{y2:.2f}",
                    ]
                    writer.writerow(row)


print(f"Готово! Картинки в {output_dir}, отчёт в {results_csv}")
