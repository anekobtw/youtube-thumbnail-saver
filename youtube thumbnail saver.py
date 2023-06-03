from colorama import Fore, init
import requests
import os

init(autoreset=True)
VERSION = '1.0.2'

def sanitize_title(title):
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    return ''.join(char for char in title if char not in invalid_chars)


while True:
    print(f"""
--------------------------------
YouTube Thumbnail Saver v{VERSION}.
© Aneko, 2023
--------------------------------
""")
    
    link = input('Enter video link: ')
    
    # Getting a title
    response = requests.get(f'https://noembed.com/embed?url={link}')
    video_title = sanitize_title(response.json()['title'])
    
    # Getting a thumbnail
    thumbnail_url = response.json()['thumbnail_url']

    # Saving an image
    response = requests.get(thumbnail_url)
    with open(f"{video_title}.jpg", "wb") as f:
        f.write(response.content)
        print(f'Saved as {Fore.GREEN}{video_title}.jpg\n')

    if input('Do you want to download another thumbnail? (Y/n) ').lower() not in ['yes', 'y']:
        break
    os.system('cls')