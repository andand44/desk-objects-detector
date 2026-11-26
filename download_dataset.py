import os
from dotenv import load_dotenv
from roboflow import Roboflow

load_dotenv()
api_key = os.getenv("ROBOFLOW_KEY")

if not api_key:
    raise ValueError("Не найден ROBOFLOW_KEY — проверь файл .env рядом со скриптом")

rf = Roboflow(api_key=api_key)
project = rf.workspace("menakant").project("detect-simple-desk-objects")
version = project.version(2)
dataset = version.download("yolov8")

print(f"Готово! Датасет сохранён в: {dataset.location}")
