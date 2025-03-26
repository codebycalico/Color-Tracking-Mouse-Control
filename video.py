import cv2

# the 0 signifies to look for a webcam
# instead of taking in an actual video file
stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not stream.isOpened():
    print("No camera detected.")
    exit()

while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more camera.")
        break

    cv2.imshow("Webcam.", frame)

    # ord casts the character 'q' to its integer ASCII
    if cv2.waitKey(1) == ord('q'):
        break
    
stream.release()
cv2.destroyAllWindows()