import time

import cv2 as cv


    
def image_processing():
    img = cv.imread('variant-2.png')
    blur = cv.GaussianBlur(img, (15, 15), 0)
    cv.imshow('image', blur)
   

def video_processing():
    cap = cv.VideoCapture(0)
    img = cv.imread('fly64.png')
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv.resize(frame, down_points, interpolation=cv.INTER_LINEAR)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv.threshold(gray, 110, 255, cv.THRESH_BINARY_INV)

        contours, _ = cv.findContours(thresh,
                            cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            a = x + (w // 2)
            b = y + (h // 2)
            img_w = w // 4 if (w // 4) % 2 == 0 else w // 4 + 1
            img_h = h // 4 if (h // 4) % 2 == 0 else h // 4 + 1
            img = cv.resize(img, (img_w, img_h), interpolation=cv.INTER_LINEAR)
            frame[b - img_h // 2:b + img_h // 2, a - img_w // 2:a + img_w // 2] = img
            if i % 5 == 0:
                with open('lab8.txt', 'a') as f:
                    f.write('x: {x}, y: {y}\n'.format(x=a, y=b))

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    #image_processing()
    video_processing()

cv.waitKey(0)
cv.destroyAllWindows()
