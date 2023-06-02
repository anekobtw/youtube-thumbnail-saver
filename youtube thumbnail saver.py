import requests
import pytube

while True:
    # Getting video link
    link = input('Enter video link: ')
    
    # Getting title
    response = requests.get(f'https://noembed.com/embed?url={link}')
    video_title = str(response.json()['title'])
    video_title = video_title.replace('/', '')
    video_title = video_title.replace('\\', '')
    video_title = video_title.replace(':', '')
    video_title = video_title.replace('*', '')
    video_title = video_title.replace('?', '')
    video_title = video_title.replace('"', '')
    video_title = video_title.replace('<', '')
    video_title = video_title.replace('>', '')
    video_title = video_title.replace('|', '')
    
    # Getting thumbnail
    thumbnail_url = pytube.YouTube(link).thumbnail_url

    # Saving image
    response = requests.get(thumbnail_url)
    with open(f"{video_title}.jpg", "wb") as f:
        f.write(response.content)
        print(f'Saved as {video_title}.jpg')

    if input('Do you want to download another thumbnail? (Y/n) ').lower() not in ['yes', 'y']:
        break

input('Press Enter to exit')