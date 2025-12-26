from diffusers import StableDeffusionPipeline
import torch


#Load AI model
pipe=StableDeffusionPipeline.from_pretrained ;{
    "stabilityai/stable-diffusion-2-1"
}


#Draw Picture
image=pipe("A cute robot reading a book").images[0]

#Save Picture
image.save("picture.png")

print(" Picture saved as picture.png")