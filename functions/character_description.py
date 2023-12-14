import streamlit as st
import base64
import requests

### OVERVIEW: Get_Character_Description function makes a https request.post call to OpenAI chat completions using OpenAI Vision model. An image is provided and OpenAI Vision can look at the image and provide a characer description. ###

# 1. Setup and Variables
openai_api_key = st.secrets.OPENAI_API_KEY                # Used to formulate authorization header
model = "gpt-4-vision-preview"                            # Used in request payload
url = "https://api.openai.com/v1/chat/completions"        # Used in request.post
contenttype = "application/json"                          # Used in request headers
authorization = f"Bearer {openai_api_key}"                # Used in request headers

# 2. Set Instructions (System Message)
sys_instructions = """
You are an expert at describing images and creating effective prompts to use with DALL-E 3 image generator. Your sole job is to create a description for the main character of a childrens storybook from an image provided by a user. You will:
- Identify the main person from the image
- Create a magical, descriptive, detailed description about that main person in the image factoring into account looks, age, clothes, expressions, etc.
- Review the description 3 times - each time enhancing for quality, details, and likeness
- Perform one final check that the description is the most effective prompt that can be used by DALLE-3
- RETURN / OUTPUT: You will return the response in the following format: "Do not modify or diversify this prompt: {{Character Description}} followed by the prompt followed by the character description 

You will follow these set of rules ALWAYS:
1. You will perform all steps internally
2. You will never engage or consult with the user at any point unless it is submitting the final output. 
3. You will create a description fit for a children's storybook
4. Your description should be based on the image provided
5. The stylistic nature of the description should create a character similar to those in Disney or Pixar movies / books
6. You will only return the description as a text string and nothing else.
"""

user_instructions = "Describe the main person in this image."

# 3. Encode Image Function (Used within Get_Character_Description)
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# 4. Get Character Description Function
def get_character_description(image_path): 
  base64_image = encode_image(image_path)
  img_url = f"data:image/jpeg;base64,{base64_image}"
  
  msg_system = {
    "role": "system",
    "content": sys_instructions
  }

  msg_user = {
    "role": "user",
    "content": [
      {"type": "text", "text": user_instructions},
      {"type": "image_url", "image_url": {"url": img_url}}
    ]
  }

  msgs = [msg_system, msg_user]
  headers = {"Content-Type": contenttype, "Authorization": authorization}
  payload = {"model": model, "messages": msgs, "max_tokens": 300}
  response = requests.post(url=url, headers=headers, json=payload)
  response_data = response.json()
  characterdescription = response_data['choices'][0]['message']['content']

  return characterdescription
    


