#以灰階的方式讀取並顯示圖形檔，並改變圖片的亮度
#本範例習題：試著改變VALUE的值，看看有什麼變化
import cv2
import numpy as np
import numpy.ma as ma

VALUE = 100
img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (800,600))
cv2.imshow("Origin", img)
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img[y][x] = img[y][x] + VALUE if img[y][x] + VALUE < 255 else 255
cv2.imshow("Brighter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()