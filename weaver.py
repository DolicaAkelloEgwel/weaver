import cv2

# read the image file
img = cv2.imread('input.jpg', 2)

bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ones_and_zeros = bw[1] / 255
print(1 - ones_and_zeros)

cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()