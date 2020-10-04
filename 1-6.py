#讀取檔案之後，把圖形檔縮小為 800x600，並加上模糊效果
#本範例習題：請使用不同方式執行模糊效果，並比較其中的差別
import cv2

def blur(image, y, x, size):
    r, g, b= list(), list(), list()
    for i, j in zip(range(size), range(size)):
        r.append(image[y-size+i][x-size+j][0])
        g.append(image[y-size+i][x-size+j][1])
        b.append(image[y-size+i][x-size+j][2])
    return (sum(r)/len(r), sum(g)/len(g), sum(b)/len(b))
SIZE = 4
img = cv2.imread("test.jpg")
simg1 = cv2.resize(img, (800, 600))
simg2 = cv2.resize(img, (800, 600))
cv2.imshow("Orign", simg1)
for y in range(SIZE, simg1.shape[0]-SIZE):          # height
    for x in range(SIZE, simg1.shape[1]-SIZE):      # width
        simg2[y][x] = blur(simg1, y, x, SIZE)
cv2.imshow("Blur", simg2)
cv2.waitKey(0)
cv2.destroyAllWindows()