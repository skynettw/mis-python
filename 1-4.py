#讀取檔案之後，把圖形檔縮小為 800x600，並製成黑白圖片
#本範例習題：找出一個最好的臨界值
import cv2
THRESHOLD = 155     #臨界值

def twofold(value):
    return 255 if value >= THRESHOLD else 0

img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
simg = cv2.resize(img, (800, 600))
print(simg.shape)
cv2.imshow("原圖", simg)
for y in range(simg.shape[0]):     # height
    for x in range(simg.shape[1]): # width
        simg[y][x] = (twofold(simg[y][x]))
cv2.imshow("黑白效果", simg)
cv2.waitKey(0)
cv2.destroyAllWindows()