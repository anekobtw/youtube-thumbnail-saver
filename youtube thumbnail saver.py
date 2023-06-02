import requests
import pytube
VERSION = '1.0.1'

print(f"""
--------------------------------
YouTube Thumbnail Saver v{VERSION}.
© Aneko, 2023
--------------------------------
""")

def sanitize_title(title):
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        title = title.replace(char, '')
    return title

while True:
    link = input('Enter video link: ')
    
    # Getting a title
    response = requests.get(f'https://noembed.com/embed?url={link}')
    video_title = sanitize_title(str(response.json()['title']))
    
    # Getting a thumbnail
    thumbnail_url = pytube.YouTube(link).thumbnail_url

    # Saving an image
    response = requests.get(thumbnail_url)
    with open(f"{video_title}.jpg", "wb") as f:
        f.write(response.content)
        print(f'Saved as {video_title}.jpg\n')

    if input('Do you want to download another thumbnail? (Y/n) ').lower() not in ['yes', 'y']:
        break