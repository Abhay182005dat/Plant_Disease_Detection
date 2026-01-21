import os
import shutil
import random

# ---------------- CONFIG ----------------
SOURCE_DIR = "Data/PlantVillage/Tomato"   # folder containing renamed class folders
TARGET_DIR = "Data/PlantVillage/Tomato"       # final output folder
TRAIN_RATIO = 0.8
SEED = 42

CLASSES = [
    "Tomato_Healthy",
    "Tomato_Early_Blight",
    "Tomato_Late_Blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_Leaf_Spot",
    "Tomato_Bacterial_Spot",
]
# ---------------------------------------

random.seed(SEED)

def create_dirs():
    for split in ["train", "val"]:
        for cls in CLASSES:
            os.makedirs(os.path.join(TARGET_DIR, split, cls), exist_ok=True)

def split_and_copy():
    for cls in CLASSES:
        src_path = os.path.join(SOURCE_DIR, cls)
        images = [f for f in os.listdir(src_path) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

        random.shuffle(images)
        split_idx = int(len(images) * TRAIN_RATIO)

        train_images = images[:split_idx]
        val_images = images[split_idx:]

        for img in train_images:
            shutil.copy(
                os.path.join(src_path, img),
                os.path.join(TARGET_DIR, "train", cls, img)
            )

        for img in val_images:
            shutil.copy(
                os.path.join(src_path, img),
                os.path.join(TARGET_DIR, "val", cls, img)
            )

        print(f"{cls}: {len(train_images)} train | {len(val_images)} val")

if __name__ == "__main__":
    create_dirs()
    split_and_copy()
