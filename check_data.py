import os

data_path = "detect-simple-desk-objects-2"
img_folder = os.path.join(data_path, "train", "images")
lbl_folder = os.path.join(data_path, "train", "labels")

images = [f for f in os.listdir(img_folder) if f.endswith('.jpg')]
labels = [f for f in os.listdir(lbl_folder) if f.endswith('.txt')]

print(f"Найдено картинок в train: {len(images)}")
print(f"Найдено файлов разметки в train: {len(labels)}")

if len(images) == len(labels):
    print("✅ Количество совпадает! Скорее всего, всё ок.")
else:
    print("⚠️ Количество не совпадает, проверь папку.")
