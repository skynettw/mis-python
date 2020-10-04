#讀取檔案之後，把圖形檔縮小為 800x600，並加上馬賽克濾鏡效果
#本範例習題：請使用不同的尺寸執行馬賽克效果
import cv2

SIZE = 20
img = cv2.imread("test.jpg")
simg1 = cv2.resize(img, (800, 600))
simg2 = cv2.resize(img, (800, 600))
cv2.imshow("Orign", simg1)
for y in range(0, simg1.shape[0], SIZE):     # height
    for x in range(0, simg1.shape[1], SIZE):     # width
        for j in range(SIZE):
            for k in range(SIZE):
                simg2[y+j][x+k] = simg1[y][x]
cv2.imshow("Mosaic", simg2)
cv2.waitKey(0)
cv2.destroyAllWindows()