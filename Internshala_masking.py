import cv2
import pytesseract

# Taking input image
print('Enter the path of the image you want to mask: ')
img_path = input()

# Storing name of the image
img_name = img_path.split('/')
img_name = img_name[len(img_name) - 1]

img = cv2.imread(img_path)

# Converting image to RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Configuring tesseract to input only numerical strings
conf = r'--oem 1 --psm 6 outputbase digits'

# Reading the data according ton the configurations
data = pytesseract.image_to_data(img_RGB, config=conf)

# Initializing variable to store aadhaar number
aadhaar_num = 0

# Iterating through all the data read by tesseract
for count, D in enumerate(data.splitlines()):
    if count != 0:
        D = D.split()

        # If statement for selecting the string with some value
        if len(D) == 12:
            # Selecting string with length 12 since aadhaar number is of 12 digits
            if len(D[11]) == 12:
                # Storing aadhaar number
                aadhaar_num = D[11]
                # Storing coordinates(x,y) and width and height if the bounding box around the string.
                x, y, w, h = int(D[6]), int(D[7]), int(D[8]), int(D[9])
                # Masking the first 8 digits of the aadhaar number
                cv2.rectangle(img, (x, y),
                              (int(0.67*w)+x, h+y), (255, 255, 255), -1)

# Printing aadhaar number
print('Your aadhaar number is: ' + str(aadhaar_num))

# Showing and storing the masked image
print('Press Esc to close the image: ')
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.imwrite('maked_'+img_name, img)
