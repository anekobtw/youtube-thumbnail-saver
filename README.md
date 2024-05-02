# YouTube Thumbnail Saver
![version](https://img.shields.io/badge/Project_version-v1.1.4-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![made with love](https://img.shields.io/badge/Made_with-Love-red)

YouTube Thumbnail Saver is a Python script designed to help users easily save thumbnails of YouTube videos or entire playlists. With this tool, you can quickly download thumbnails for your favorite videos for various purposes such as creating thumbnails for your own videos or for personal reference.

## Features
**Save Single Thumbnail:** Download the thumbnail of a single YouTube video by providing its link.\
**Save Playlist Thumbnails:** Download thumbnails for all videos in a YouTube playlist.\
**Simple CLI:** Easy-to-use command-line interface for quick thumbnail downloads.

## Installation
To use YouTube Thumbnail Saver, follow these steps:

1. Clone or download this repository to your local machine
2. Make sure you have Python installed on your system
3. Install the required dependencies by running `pip install -r requirements.txt`
4. Run the script by executing `python yts.py`

## Usage
Once the script is running, follow the prompts to choose the type of download you want

**Single Thumbnail:** Enter 1 to save the thumbnail of a single YouTube video. Provide the video link when prompted.\
**Playlist Thumbnails:** Enter 2 to save thumbnails for all videos in a YouTube playlist. Provide the playlist link when prompted.

After downloading the thumbnails, they will be saved in a directory named thumbnails within the same directory as the script.


## Example
```
$ python yts.py

YouTube Thumbnail Saver v1.1.4 © anekobtw, 2024

What do you want to download?
[1] A video thumbnail.
[2] All the thumbnails of a playlist.
1
Enter the video link: https://www.youtube.com/watch?v=0e3GPea1Tyg&ab_channel=MrBeast

Saved as $456,000 Squid Game In Real Life!.png

Do you want to download another one? (y/n) n
```


## Contributing
Contributions are always welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue on the [GitHub repository](https://github.com/anekobtw/youtube-thumbnail-saver).

## Licence
Copyright © 2024 anekobtw.\
This project is [MIT](https://github.com/anekobtw/youtube-thumbnail-saver/blob/main/LICENSE) licensed.
