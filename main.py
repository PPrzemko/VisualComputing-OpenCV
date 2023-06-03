import cv2 as cv

if __name__ == '__main__':
    img = cv.imread("yoshi.png")
    cv.imshow("yoshi", img)
    cv.waitKey(0)
