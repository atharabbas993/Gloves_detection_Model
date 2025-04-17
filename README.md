# 🧤 Gloves Detector using YOLOv8

This repository contains all necessary scripts and models to detect glove usage using the YOLOv8 model. It's useful for safety compliance monitoring in settings like hotels, hospitals, and factories.

---

## 📁 Project Structure

```plaintext
GLOVES_DETECTOR/
│
├── main.py                      # Main entry point for the app
├── inference.py                 # Script to run inference on images
├── live_webcam.py              # Real-time webcam detection
│
├── runs/                        # YOLOv8 output folder (training/inference)
│
├── Trained_Models/             # Folder for storing trained YOLOv8 models
│   └── best.pt                  # Best model weights
│
├── venv/                        # Virtual environment (optional)
