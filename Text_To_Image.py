from huggingface_hub import InferenceClient
from PIL import Image


client = InferenceClient(
    "stabilityai/stable-diffusion-xl-base-1.0",
    token="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"
)

prompt = input("Enter your prompt: ")

image = client.text_to_image(prompt, guidance_scale=7.5, num_inference_steps=30)

# Save the output image
image.save("output.png")
img = Image.open("output.png")
img.show()
print("Image saved as output.png")
