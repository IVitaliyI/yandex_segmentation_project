import os
import shutil
from pathlib import Path

files_to_move = [
    "train/000000023731_404.jpg", 
    "train/000000028253_7169.jpg", 
    "train/000000049758_3963.jpg",
    "train/000000066011_2187.jpg", 
    "train/000000121530_5761.jpg", 
    "train/000000247301_4455.jpg",
    "train/000000258305_3996.jpg", 
    "train/000000275028_3168.jpg", 
    "train/000000275919_4499.jpg",
    "train/000000317781_4461.jpg", 
    "train/000000419618_7033.jpg", 
    "train/000000481212_908.jpg",
    "train/000000562835_2386.jpg", 
    "train/000000574769_0.jpg"
]

target_dir = Path("data") / "train_dataset_for_students" / "img" / "to_fix"

os.makedirs(target_dir, exist_ok=True)

for file_path in files_to_move:
    file_path = Path("data") / "train_dataset_for_students" / "img" / file_path
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        new_path = os.path.join(target_dir, file_name)
        shutil.copy(file_path, new_path)
        print(f"Перенесен: {file_name}")
    else:
        print(f"Файл не найден: {file_path}")
