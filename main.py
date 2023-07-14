import cv2
#setting configurable parameters:
source='download.jpg'
destination='New_image.png'
scale_percent=75

#Loading and Diaplaying image on window
src=cv2.imread(source)
cv2.imshow("Image",src)


#Scaling new dimension of image
new_width=int(src.shape[1] * scale_percent/100)
new_height=int(src.shape[0] * scale_percent/100)

#Re-sizing image
dsize=(new_width,new_height)
output=cv2.resize(src,dsize)

#Saving image to storage device
cv2.imwrite(destination,output)
