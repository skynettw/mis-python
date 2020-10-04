#讀取檔案之後，把圖形檔縮小為 800x600，並讓圖形變模糊
#本範例習題：請使用不同的函式完成模糊效果並加以比較
import cv2

img = cv2.imread("test.jpg")
simg1 = cv2.resize(img, (800, 600))
simg2 = cv2.resize(img, (800, 600))
cv2.imshow("原圖", simg1)
for y in range(simg1.shape[0]):     # height
    for x in range(simg1.shape[1]): # width
        simg2[y][x] = (twofold(simg1[y][x]))
cv2.imshow("模糊效果", simg2)
cv2.waitKey(0)
cv2.destroyAllWindows()