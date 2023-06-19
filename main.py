import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def plotHistogram(image, cumulative=False):
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    if cumulative:
        hist = hist.cumsum()
    hist /= hist.sum()

    plt.figure()
    plt.plot(hist)
    plt.show()
    return hist


def fiveone(img):

    # hist = plotHistogram(img, True)
    hist2 = plotHistogram(img, False)
    min_val, max_val, _, _ = cv.minMaxLoc(img)
    desired_min = 100
    desired_max = 150
    scaled_image = cv.convertScaleAbs(img, alpha=(desired_max - desired_min) / (max_val - min_val),
                                      beta=(desired_min * max_val - desired_max * min_val) / (max_val - min_val))
    plotHistogram(scaled_image)

    desired_min = 0
    desired_max = 255
    scaled_image2 = cv.convertScaleAbs(img, alpha=(desired_max - desired_min) / (max_val - min_val),
                                      beta=(desired_min * max_val - desired_max * min_val) / (max_val - min_val))
    plotHistogram(scaled_image2)

def fivetwo(image):
    #1  Berechnung des Histogramms
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    #2 akkumulierten Histogramms
    cumulative_histogram = np.cumsum(hist)
    #3 Berechnung der kumulativen Verteilungsfunktion (eng. CDF): Teilen des akkumulierten Pixelzählers durch die Bildauflösung (also max. Pixelanzahl)
    cumulative_histogram_normalized = cumulative_histogram / cumulative_histogram.max()
    #: Multiplizieren der Verteilungsfunktion mit der höchstmöglichen Pixelintensität des Zielbildes (normalerweise 255) und Abrunden auf den nächsten Integer
    test = cumulative_histogram_normalized * 255
    test = np.round(test)
    test = test.astype(np.uint8)
    #5 Wenden Sie die resultierende Abbildung auf jeden Pixel des Input-Bildes an.
    test = test[image]




    cv.imshow("fff", test)
    plt.figure()
    plt.plot(cumulative_histogram_normalized)
    plt.show()
    # QUESTIONS
    # Ein Beispiel für die Berechnung und die Funktionsweise des Algorithmus’ finden Sie in Abbildung 1, für
    # ein 4-Bit Inputbild.
    # Wenn Ihre Implementierung funktioniert, werfen Sie einen Blick auf das resultierende Histogramm. Was
    # passiert im akkumulierten Histogramm? Wie verhält sich der Algorithmus bei dem angepassten Bild mit
    # verringertem Kontrast aus Aufgabe 5.1?


def fivethree():

    image = cv.imread('kante.png')

    F1 = np.array([[0, 0, 0],
                [-1,  1, 0],
                [0, 0, 0]], dtype=np.float32)

    F2 = np.array([[0, 0, 0],
                [0,  -1, 1],
                [0, 0, 0]], dtype=np.float32)

    F3 = np.array([[0, 0, 0],
                [1,  -2, 1],
                [0, 0, 0]], dtype=np.float32)
    
    F4 = np.array([[0,  0, 0],
                [0.333,  0.333,  0.333],
                [0, 0,  0]], dtype=np.float32)
    
    F5 = np.array([[0,  0, 0],
                [0,  1,  0],
                [0, 0,  0]], dtype=np.float32)
    
    F6 = np.array([[0,  0, 0],
                [0.333,  -0.666,  0.333],
                [0, 0,  0]], dtype=np.float32)

    delta = 128

    # Perform convolutions
    result1 = cv.filter2D(image.copy(), -1, F1, delta=delta)
    result2 = cv.filter2D(result1, -1, F2, delta=delta)
    result3 = cv.filter2D(image.copy(), -1, F3, delta=delta)

    cv.imwrite('F1.png', result1)
    cv.imwrite('F2.png', result2)
    cv.imwrite('F3.png', result3)



    result4 = cv.filter2D(image.copy(), -1, F4, delta=delta)
    result5 = cv.filter2D(image.copy(), -1, F5, delta=delta)
    result6 = cv.filter2D(image.copy(), -1, F6, delta=delta)


    cv.imwrite('F4.png', result4)
    cv.imwrite('F5.png', result5)
    cv.imwrite('F6.png', result6)


    cv.waitKey(0)
    cv.destroyAllWindows()

# Fragen:
# 1) Was liefert der Vergleich der beiden zuletzt erzeugten Ergebnisse?

# 2) Die beiden Faltungsmatrizen F1 und F2 differenzieren das Bild (d.h. sie bilden jeweils die Ableitung)
# in Zeilenrichtung. Was bewirkt demzufolge die Faltungsmatrix F3 bzgl. des Begriffes "Ableitung"?

# • Falten Sie eine Kopie des ursprünglichen Bildes mit der Faltungsmatrix F4.
# • Falten Sie unabhängig davon eine weitere Kopie des ursprünglichen Bildes mit der Faltungsmatrix F5.
# • Wenn Sie jetzt das mit F5 erzeugte Bild von dem mit F4 erzeugten Bild subtrahieren würden,
# so entspräche das einer Faltung des ursprünglichen Bildes mit der Faltungsmatrix F6, die eine
# Subtraktion dieser zwei Faltungsmatrizen ist: F6= F4 - F5. Führen Sie die Faltung mit F6 durch
# (delta=128).

# Fragen:
# 3) Was liefert der pixelweise Vergleiche des Ergebnisses der Faltung mit F6 mit dem Ergebnis der
# Faltung mit F3? Begründen Sie die Unterschiede.

# 4) Was bewirken die beiden Faltungen F4 bzw. F5?

# 5) Was erhält man, wenn man die Faltungsmatrix F3 um 90 Grad dreht und zu F3 selbst addiert?
# Wie heißt dieser Operator und was bewirkt er bzgl. des Begriffes "Ableitung"?





if __name__ == '__main__':
    imggrey = cv.imread('schrott.png', cv.IMREAD_GRAYSCALE)
    img = cv.imread('schrott.png')

    #fiveone(imggrey)
    #cv.imshow("inputOrig", img)
    #fivetwo(imggrey)
    #fivethree()

