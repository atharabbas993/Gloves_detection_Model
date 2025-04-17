from ultralytics import YOLO

# Load your trained model
model = YOLO(r'D:\worksapce\Gloves_Detector\Trained_Models\best.pt')

# Run prediction
results = model.predict(source=r'test_image.jpg', save=True, save_txt=True, conf=0.5)

print("✅ Inference complete. Results saved in 'runs/detect/predict'")
