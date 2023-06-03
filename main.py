import cv2 as cv


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
    img[0::5, 0::5] = [0, 0, 0]
    cv.imshow("Every 5th pixel", img)
    cv.imwrite("NewYoshi.png", img)


if __name__ == '__main__':
    image = cv.imread("yoshi.png")
    cv.imshow("yoshi", image)
    # imghsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    one(image)
    cv.waitKey(0)
