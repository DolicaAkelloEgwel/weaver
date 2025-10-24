import cv2

# read the image file + check the shape
base_img = cv2.imread('Code 0.png', 2)
print(base_img.shape)

def convert_image_to_ones_and_zeroes(image):
    bw = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    ones_and_zeros = bw[1] / 255
    ones_and_zeros = 1 - ones_and_zeros
    return ones_and_zeros

# things are flipped for the base image
base_image = 1 - convert_image_to_ones_and_zeroes(base_img)

# these are the codes the student used
CODES = [2,3,5,6]

for code in CODES:
    code_image = cv2.imread(f'Code {code}.png', 2)
    print(base_image[206][:5])
    code_image = convert_image_to_ones_and_zeroes(code_image) * (code - 1)
    base_image = base_image + code_image

with open("output.txt", "w") as f:
    for line in base_image:
    line = [str(int(val)) for val in line]
    f.write("".join(line) + "\n")

cv2.imshow("Binary", base_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
