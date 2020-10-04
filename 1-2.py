#以灰階的方式讀取並顯示圖形檔
#本範例習題：自己利用公式，謮取彩色圖形檔，然後建立一個灰階的圖檔並顯示
import cv2

img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()