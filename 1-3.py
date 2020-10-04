#讀取檔案之後，把圖形檔縮小為 800x600，並製成負片效果
import cv2

img = cv2.imread("test.jpg")
simg = cv2.resize(img, (800, 600))
print(simg.shape)
cv2.imshow("原圖", simg)
for y in range(simg.shape[0]):     # height
    for x in range(simg.shape[1]): # width
        simg[y][x] = (255-simg[y][x][0], 255-simg[y][x][1], 255-simg[y][x][2])
cv2.imshow("負片效果", simg)
cv2.waitKey(0)
cv2.destroyAllWindows()