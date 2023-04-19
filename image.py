from key import api_key
import openai
import sys
import requests

openai.api_key = api_key

def generate_image(prompt) -> str:
    """Returns url to image"""
    print("Waiting for openai to create the image")
    response = openai.Image.create(prompt=prompt)
    return response['data'][0]['url']

def get_fname_from_prompt(prompt: str) -> str:
    table = prompt.maketrans(" ", "_", "?/\\!@#$%^&*+=")
    return prompt.translate(table) + ".png"

def download_image(url: str, fname: str):
    print(f"Saving image to {fname}")
    response = requests.get(url)
    with open(fname, "wb") as fp:
        fp.write(response.content)

def create_and_download_image(prompt: str):
    url = generate_image(prompt)
    fname = get_fname_from_prompt(prompt)
    download_image(url, fname)

if __name__ == "__main__":
    prompt = sys.argv[1]
    create_and_download_image(prompt)