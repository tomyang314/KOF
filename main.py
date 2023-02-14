from Pose import PoseDetector
import cv2
from movements import *
import threading
from windows import Windows
import time

angle1 = 360
angle2 = 360
angle3 = 360
flag = False
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = PoseDetector()
hwnd = Windows("Qt5QWindowIcon", u"约战竞技场-游戏(活跃)")
hwnd.top()


def trigger(character):
    global angle1, angle2, flag
    while True:
        time.sleep(0.05)
        if 300 < angle1 < 320 and 300 < angle2 < 320:
            character.explosive_gas()
        elif 175 < angle1 < 185 and 250 < angle3 < 270:
            character.centipede_hand()
        elif 30 < angle1 < 60 and 305 < angle2 < 330:
            character.gun()
        elif 30 < angle1 < 60:
            character.grand()
        if flag:
            break


def camera():
    global angle1, angle2, angle3, flag
    while True:
        _, img = cap.read()
        img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
        img = cv2.flip(img, 1)
        img = detector.find_pose(img)
        lm_list = detector.find_position(img)
        angle1 = detector.find_angle(img, 11, 13, 15, draw=False)
        angle2 = detector.find_angle(img, 16, 14, 12, draw=False)
        angle3 = detector.find_angle(img, 23, 11, 13, draw=False)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    flag = True
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    k = K9999()
    threads = [threading.Thread(target=camera),
               threading.Thread(target=trigger, args=(k, ))
               ]

    for i in threads:
        i.start()


