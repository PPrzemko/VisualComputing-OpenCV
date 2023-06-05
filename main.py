import cv2 as cv
import numpy as np


def one(img):
    # get height width channel
    print(img.shape)
    # float image
    image_float = img.astype(float)
    cv.imshow("float image", image_float)
    # draw red square

    height, width, not_used = img.shape
    center_x = width // 2
    center_y = height // 2
    # Koordinaten des Quadrats berechnen
    top_left = (center_x - 5, center_y - 5)
    bottom_right = (center_x + 5, center_y + 5)
    cv.rectangle(img, top_left, bottom_right, (0, 0, 255), -1)
    cv.imshow('Bild mit Quadrat', image)

    # every 5th pixel to black
    img[0::5] = [0, 0, 0]
    cv.imshow("Every 5th pixel", img)
    cv.imwrite("NewYoshi.png", img)


def two(img):
    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.imread("mask.png")
    imghsv[mask == 255] = 140
    cv.imshow("test", mask)
    cv.imshow("hue", cv.cvtColor(imghsv, cv.COLOR_HSV2BGR))
    # useless testing
    # maskhsv2 = maskhsv[:, :, 0] = (maskhsv[:, :, 0] - int(255 * 0.3333)) % 255
    # imghsv[maskhsv > 0] = np.uint8([[120, 255, 255]])
    # test = cv.addWeighted(imghsv, 0.5, maskhsv, 0.5, 0)
    # mask2 = cv.bitwise_and(imghsv, imghsv, maskhsv)
    # cv.imshow("h2", cv.cvtColor(maskhsv, cv.COLOR_HSV2BGR))
    # cv.imshow("h", img3)
    # cv.imshow("2", cv.cvtColor(imghsv, cv.COLOR_HSV2BGR))
    # cv.imshow("test", cv.cvtColor(test, cv.COLOR_HSV2BGR))

def three():
    input = cv.imread("FigSource.png")
    target = cv.imread("FigTarget.png")
    cv.imshow("inputOrig", input)
    inputFloat = cv.normalize(input, None, 0.0, 1.0, cv.NORM_MINMAX, cv.CV_32F)
    targetFloat = cv.normalize(target, None, 0.0, 1.0, cv.NORM_MINMAX, cv.CV_32F)

    # convert to lab
    inputLab = cv.cvtColor(inputFloat, cv.COLOR_BGR2LAB)
    targetLab = cv.cvtColor(targetFloat, cv.COLOR_BGR2LAB)
    # l is brightness, A is green-red, B is blue-yellow
    inputL, inputA, inputB = cv.split(inputLab)
    targetL, targetA, targetB = cv.split(targetLab)
    
    inputL = inputL - np.mean(inputL)
    inputA = inputA - np.mean(inputA)
    inputB = inputB - np.mean(inputB)

    inputL = inputL / np.std(inputL)
    inputA = inputA / np.std(inputA)
    inputB = inputB / np.std(inputB)

    inputL = inputL * np.std(targetL)
    inputA = inputA * np.std(targetA)
    inputB = inputB * np.std(targetB)

    inputL = inputL + np.mean(targetL)
    inputA = inputA + np.mean(targetA)
    inputB = inputB + np.mean(targetB)

    #convert to rbg
    inputLab = cv.merge([inputL, inputA, inputB])
    inputBGR = cv.cvtColor(inputLab, cv.COLOR_LAB2BGR)
    cv.imshow("changed", inputBGR)
    cv.imshow("target", target)



if __name__ == '__main__':
    image = cv.imread("yoshi.png")
    #cv.imshow("yoshi", image)
    #one(image.copy())
    #two(image.copy())
    three()
    cv.waitKey(0)
    cv.destroyAllWindows()
