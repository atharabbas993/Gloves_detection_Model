# 🧤 Gloves Detector using YOLOv8

This repository contains all files needed to train and infer a glove detection model using YOLOv8.

---

## 📁 Project Structure

```plaintext
GLOVES_DETECTOR/
│
├── dataset/                     # Labeled dataset in YOLOv8 format
│   ├── test/                    # Test images and labels
│   ├── train/                   # Training images and labels
│   ├── valid/                   # Validation images and labels
│   ├── data.yaml                # YOLO dataset configuration
│   ├── README.dataset.txt       # Dataset info
│   └── README.roboflow.txt      # Roboflow metadata
│
├── main_file/                   # Scripts for training, inference, unzip
│   ├── inference.py
│   ├── train.py
│   └── unzip.py
│
├── runs/
│   └── detect/                  # Output folders from detection and training runs
│       ├── predict/
│       ├── predict7/
│       ├── train/
│       ├── train2/
│       ├── train3/
│       ├── train4/
│       ├── train5/
│       ├── train6/
│       └── train7/
│
├── yolov8env/                   # Virtual environment (optional)
│
├── Gloves_Detection_Dataset.v1i.yolov8.zip   # Roboflow dataset zip
├── requirements.txt             # Dependencies list
├── result.jpg                   # Sample output image
├── test.jpg                     # Test input image
├── yolov8n.pt                   # YOLOv8 nano model weights
└── yolov8s.pt                   # YOLOv8 small model weights
