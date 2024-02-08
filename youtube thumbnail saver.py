import os
import time

import pytube
import requests
from colorama import Fore, init

init(autoreset=True)
VERSION = '1.1.3'


def save_thumbnail(link):
    # ! Getting a title
    response = requests.get(f'https://noembed.com/embed?url={link}')
    video_title = response.json()['title']
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    video_title = ''.join(char for char in video_title if char not in invalid_chars)

    # Getting a thumbnail
    thumbnail_url = pytube.YouTube(link).thumbnail_url

    # Saving an image
    with open(f'{video_title}.png', "wb") as f:
        response = requests.get(thumbnail_url)
        f.write(response.content)
        print(f'Saved as {Fore.GREEN}{video_title}.png\n')


while True:
    print(f'--------------------------------\nYouTube Thumbnail Saver v{VERSION}.\n© anekobtw, 2024\n--------------------------------')

    download_type = input(f'''What do you want to download?
{Fore.CYAN}[1]{Fore.RESET} A video thumbnail.
{Fore.CYAN}[2]{Fore.RESET} All the thumbnails of a playlist.
''')

    match download_type:
        case '1':
            save_thumbnail(input('Enter the video link: '))
        case '2':
            link = input('Enter the link to the playlist: ')
            for video in pytube.Playlist(link).videos:
                save_thumbnail(video.watch_url)
        case _:
            print(f'{Fore.RED}Error occured.')
            time.sleep(1)
            quit()

    if input('Do you want to download another one? (y/n) ').lower() not in ['yes', 'y']:
        break

    os.system('cls' if os.name == 'nt' else 'clear')
