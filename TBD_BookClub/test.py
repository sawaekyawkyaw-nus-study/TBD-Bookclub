# import cv2
import base64

# img = cv2.imread('TBD_BookClub/membership.jpg')

# cv2.imshow('image',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# from PIL import Image

# img = Image.open('TBD_BookClub/membership.jpg')
# img.show()
with open('TBD_BookClub/membership.jpg', 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    print(base64_bytes)

    base64_string = base64_bytes.decode()
    print(base64_string)
