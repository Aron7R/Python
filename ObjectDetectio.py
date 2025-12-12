import cv2
from transformers import pipeline

detector = pipeline("object-detection",model="facebook/detr-resnet-50")

result = detector("image.jpg")
print(result)
