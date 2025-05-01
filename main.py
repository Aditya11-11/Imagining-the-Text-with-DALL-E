import streamlit as st
import openai
import base64
from PIL import Image
import io

# Set up OpenAI API key
openai.api_key = "api-key"  

def generate_image(prompt):
    result = openai.Image.create(
        model="gpt-image-1",  
        prompt=prompt
    )
    
    # Decode base64 image
    image_base64 = result['data'][0]['b64_json']
    image_bytes = base64.b64decode(image_base64)

    # Convert bytes to image
    image = Image.open(io.BytesIO(image_bytes))
    
    return image

st.title("Image Generation with OpenAI")

prompt = st.text_input("Enter an image description:", "A children's book drawing of a veterinarian using a stethoscope to listen to the heartbeat of a baby otter.")

# Generate button
if st.button("Generate Image"):
    if prompt:
        with st.spinner('Generating image...'):
            # Generate the image
            generated_image = generate_image(prompt)
            st.image(generated_image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt to generate an image.")
