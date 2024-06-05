import os
import time
from typing import Tuple
import customtkinter
from CTkMessagebox import CTkMessagebox

import pytube
import requests

VERSION = "1.1.4"


class App(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # configure window
        self.title("YouTube Thumbnail Saver")

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="YouTube Thumbnail Saver v2.0.0",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))
        self.dev_label = customtkinter.CTkLabel(self.sidebar_frame, text="© anekobtw, 2024")
        self.dev_label.grid(row=1, column=0, padx=20, pady=(0, 20))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20)
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(0, 10))

        # create first frame
        self.frame1 = customtkinter.CTkFrame(self)
        self.frame1.grid(row=0, column=1, padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(self.frame1, text="YouTube video", font=customtkinter.CTkFont(size=15))
        self.label1.grid(row=0, column=0, padx=15, pady=(10, 8))

        self.entry1 = customtkinter.CTkEntry(self.frame1, placeholder_text="Video URL")
        self.entry1.grid(row=1, column=0, padx=15, pady=(10, 5))

        self.downloadbutton1 = customtkinter.CTkButton(
            self.frame1, text="Download", fg_color="transparent", border_width=2, text_color=("gray15", "#DCE4EE"), command=self.download_1
        )
        self.downloadbutton1.grid(row=2, column=0, padx=15, pady=(5, 10), sticky="nsew")

        # create first frame
        self.frame2 = customtkinter.CTkFrame(self)
        self.frame2.grid(row=1, column=1, padx=20, pady=20)

        self.label2 = customtkinter.CTkLabel(self.frame2, text="YouTube playlist", font=customtkinter.CTkFont(size=15))
        self.label2.grid(row=0, column=0, padx=15, pady=(10, 8))

        self.entry2 = customtkinter.CTkEntry(self.frame2, placeholder_text="Playlist URL")
        self.entry2.grid(row=1, column=0, padx=15, pady=(10, 5))

        self.downloadbutton2 = customtkinter.CTkButton(
            self.frame2, text="Download", fg_color="transparent", border_width=2, text_color=("gray15", "#DCE4EE"), command=self.download_2
        )
        self.downloadbutton2.grid(row=2, column=0, padx=15, pady=(5, 10), sticky="nsew")

        # set default values
        self.appearance_mode_optionmenu.set("System")

    def save_thumbnail(self, link: str) -> str:
        response = requests.get(f"https://noembed.com/embed?url={link}")
        video_title = response.json()["title"]
        invalid_chars = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
        video_title = "".join(char for char in video_title if char not in invalid_chars)

        with open(f"thumbnails/{video_title}.png", "wb") as f:
            response = requests.get(pytube.YouTube(link).thumbnail_url)
            f.write(response.content)

    def download_1(self) -> None:
        self.save_thumbnail(self.entry1.get())
        CTkMessagebox(title="Info", message="The thumbail has been saved!")

    def download_2(self) -> None:
        for video in pytube.Playlist(self.entry2.get()).videos:
            self.save_thumbnail(video.watch_url)
        CTkMessagebox(title="Info", message="The thumbails have been saved!")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
