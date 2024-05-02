import os
import time

import pytube
import requests
from colorama import Fore, init

init(autoreset=True)
VERSION = "1.1.4"


def save_thumbnail(link):
    # Getting a title
    response = requests.get(f"https://noembed.com/embed?url={link}")
    video_title = response.json()["title"]
    invalid_chars = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
    video_title = "".join(char for char in video_title if char not in invalid_chars)

    # Saving an image
    with open(f"thumbnails/{video_title}.png", "wb") as f:
        response = requests.get(pytube.YouTube(link).thumbnail_url)
        f.write(response.content)
        print(f"Saved as {Fore.GREEN}{video_title}.png\n")


if __name__ == "__main__":
    while True:
        print(f"YouTube Thumbnail Saver v{VERSION} © {Fore.GREEN}anekobtw{Fore.RESET}, 2024\n")

        text = (
            "What do you want to download?\n",
            f"{Fore.CYAN}[1]{Fore.RESET} A video thumbnail.\n",
            f"{Fore.CYAN}[2]{Fore.RESET} All the thumbnails of a playlist.\n",
        )

        download_type = int(input("".join(text)))

        match download_type:
            case 1:
                save_thumbnail(input("Enter the video link: "))
            case 2:
                link = input("Enter the link to the playlist: ")
                for video in pytube.Playlist(link).videos:
                    save_thumbnail(video.watch_url)
            case _:
                print(f"{Fore.RED}Error occured.")
                time.sleep(1)
                quit()

        if input("Do you want to download another one? (y/n) ").lower() not in ["yes", "y", "yeah"]:
            break

        os.system("cls" if os.name == "nt" else "clear")
