import cv2

if __name__ == "__main__":
    winnam = "MUSHROOMS"
    img = cv2.imread("images1.jpeg", cv2.IMREAD_COLOR)
    cv2.namedWindow(winnam)
    cv2.moveWindow(winnam, 300, 75)
    cv2.imshow(winnam, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
