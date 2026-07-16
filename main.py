from openai import OpenAI
import requests

# Replace with your OpenAI API key
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

prompt = """
Ultra-realistic DSLR portrait of a young Indian woman wearing a traditional blue saree,
standing near Charminar during golden hour, soft natural lighting, 85mm lens,
highly detailed skin texture, cinematic composition, 8K quality.
"""

response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
)

image_url = response.data[0].url

img = requests.get(image_url)

with open("generated_image.png", "wb") as f:
    f.write(img.content)

print("Image generated successfully!")
