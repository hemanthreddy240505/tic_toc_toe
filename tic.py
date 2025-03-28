import requests
from bs4 import BeautifulSoup
import os

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded: {filename}")
    else:
        print(f"Failed to download image: {filename}")

def download_images_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for i, image in enumerate(images):
        image_url = image.get('src')
        if image_url:
            filename = f"image_{i+1}.jpg"
            download_image(image_url, filename)

def main():
    url = input("Enter the URL: ")
    download_images_from_url(url)

if __name__ == "__main__":
    main()
