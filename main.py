from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import pytube
from random import randint
import threading


class YoutubeDownloader(App):
    
    def build(self):
        self.layout = GridLayout(cols=1)
        self.input_url = TextInput(hint_text="ссылка на видео", multiline=False)
        self.logoText = Label(text="Youtube downloader")
        self.download_video_button = Button(text='Скачать видео', on_press=self.video_thread)
        self.input_url_two = TextInput(hint_text="ссылка на аудио", multiline=False)
        self.download_audio_button = Button(text="Скачать аудио", on_press=self.download_audio)
        self.layout.add_widget(self.logoText)
        self.layout.add_widget(self.input_url)
        self.layout.add_widget(self.download_video_button)
        self.layout.add_widget(self.input_url_two)
        self.layout.add_widget(self.download_audio_button)
        return self.layout
    
    def video_thread(self, instance):
        video_url = self.input_url.text
        t = threading.Thread(target=self.download_video, args=(video_url,))
        t.start()

      
    def download_video(self, video_url):
        yt = pytube.YouTube(video_url)
        stream = yt.streams.filter(progressive=True,  file_extension="mp4").first()
        stream.download()
        print('Видео успешно скачано.')

    def download_audio(self, instance):
       audio_url = self.input_url_two.text
       yt = pytube.YouTube(audio_url)
       stream = yt.streams.filter(only_audio=True).first()
       stream.download(filename=f'audioYouTube{randint(0, 1000)}.mp3')
       print('Аудио успешно скачано')

if name == 'main':
    app = YoutubeDownloader()
    app.run()
