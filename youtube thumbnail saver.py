from colorama import Fore, init
import requests
import pytube
import time
import os

init(autoreset=True)
VERSION = '1.1'

def save_thumbnail(link):
    response = requests.get(f'https://noembed.com/embed?url={link}')
    
    # Getting a title
    video_title = response.json()['title']
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    video_title = ''.join(char for char in video_title if char not in invalid_chars)

    # Getting a thumbnail
    thumbnail_url = response.json()['thumbnail_url']

    # Saving an image
    with open(f'{video_title}.png', "wb") as f:
        response = requests.get(thumbnail_url)
        f.write(response.content)
        print(f'Saved as {Fore.GREEN}{video_title}.png\n')


while True:
    print(f"""
--------------------------------
YouTube Thumbnail Saver v{VERSION}.
© anekobtw, 2023
--------------------------------
""")

    download_type = input('''What do you want to download?
[1] Video thumbnail.
[2] All the thumbnails from the playlist.
''')

    if download_type == '1':
        link = input('Enter the video link: ')
        save_thumbnail(link)

    elif download_type == '2':
        link = input('Enter the link to the playlist: ')
        playlist = pytube.Playlist(link).videos
        for video in playlist:
            save_thumbnail(video.watch_url)

    else:
        print(f'{Fore.RED}Error occured.')
        time.sleep(1)
        quit()

    if input('Do you want to download another thumbnail? (Y/n) ').lower() not in ['yes', 'y']:
        break
    os.system('cls')
