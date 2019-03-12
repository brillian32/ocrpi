import cv2
def print_howto():
    print("""
        Change color space of the
        input video stream using keyboard controls. The control keys are:
        1. Grayscale - press 'g'
        2. YUV - press 'y'
        3. HSV - press 'h'
    """)
if __name__=='__main__':
    print_howto()
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened correctly
    if not cap.isOpened():
    raise IOError("Cannot open webcam")
    cur_mode = None
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5,interpolation=cv2.INTER_AREA)
        c = cv2.waitKey(1)
        if c == 27:
            break
        if c != -1 and c != 255 and c != cur_mode:
            cur_mode = c
        if cur_mode == ord('g'):
            rows, cols = frame.shape
            sobel_horizontal = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
            sobel_vertical = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
            output = cv2.cvtColor(sobel_horizontal, sobel_horizontal)
        elif cur_mode == ord('y'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        elif cur_mode == ord('h'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        else:
            output = frame
        cv2.imshow('Webcam', output)
    cap.release()
    cv2.destroyAllWindows()