import cv2

# Load the image

image=cv2.imread("NATURE.jpeg")





# Display the image in the resized window

cv2.imshow('Loaded Image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window