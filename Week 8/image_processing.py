# from PIL import Image

# img = Image.open('image.png')

# transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# transposed_img.save('corrected.png')

# print('Done Flipping')

#image enhancement CLAHE

import cv2 

img = cv2.imread('image.png')


clahe = cv2.createCLAHE()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

enhanced = clahe.apply(gray)

cv2.imwrite('enhanced.png', enhanced)

print("done enhancing")