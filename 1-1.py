#標準讀取檔案模式
import cv2

img = cv2.imread("test.jpg")
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()