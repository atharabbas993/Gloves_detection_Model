from ultralytics import YOLO
import cv2

# 1. Apna trained model load karo
model = YOLO(r'D:\worksapce\Gloves_Detector\Trained_Models\best.pt')  # apna actual model path do

# 2. Webcam capture open karo (0 means default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Frame pe inference (detection) run karo
    results = model.predict(source=frame, show=True, conf=0.7)

    # 4. 'q' dabane par loop break hoga
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Cleanup
cap.release()
cv2.destroyAllWindows()
