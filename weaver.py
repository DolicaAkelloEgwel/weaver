import cv2

# read the image file
img = cv2.imread('input.jpg', 2)

# converting to its binary form
bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

# divide by 255 to get an array of 1s and 0s - 1 is black and 0 is white
ones_and_zeros = bw_img / 255
ones_and_zeros = 1 - ones_and_zeros

# just checking
print(ones_and_zeros.shape)

# write it to a file
with open("output.txt", "w") as f:
    for line in ones_and_zeros:
        line = [str(int(val)) for val in line]
        f.write("".join(line) + "\n")

# display the b&w image
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()