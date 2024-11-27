from groq import Groq
from base64 import b64encode
from os import environ

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return b64encode(image_file.read()).decode('utf-8')

def image_name_suggestion(image_name):
    # Path to your image
    image_path = image_name

    # Getting the base64 string
    base64_image = encode_image(image_path)

    client = Groq(api_key=environ.get("GROQ_API_KEY"))

    prompt = '''Analyze this image and perform the following tasks:
    1. Identify the main subject, style, and key visual elements
    2. Generate a descriptive filename that:
       - Captures the main subject/theme
       - Is concise (2-4 words)
       - Uses underscores between words
       - Excludes special characters
    3. Return the response in this JSON format:
    {
        "name": "suggested_image_name",
        "extension": ".jpeg"
    }'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        stream=False,
        response_format={"type": "json_object"},
        model="llama-3.2-11b-vision-preview",
        stop=None,
        temperature=1
    )

    return chat_completion.choices[0].message.content

