import cv2
import PoseEstimationModule as pe
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = pe.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    print(lmList)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
