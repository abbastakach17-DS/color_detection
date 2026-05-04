import cv2
import functions
from PIL import Image
yellow=(0, 255, 255)  # couleur jaune en BGR
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow, upper_yellow = functions.get_limits(yellow)
    mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()#(x1, y1, x2, y2)
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Camera snapshot app", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()