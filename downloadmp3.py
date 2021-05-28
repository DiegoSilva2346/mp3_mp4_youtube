from pytube import YouTube        

import os
from moviepy.editor import VideoFileClip
class MP3():
   def __init__(self,links):
    
      self.links=links
      print(self.links)
   def download_mp4(self):
         for keys,values in self.links.items():
            YouTube(keys).streams.first().download(filename=values)
            mp4=values+".mp4" 
            mp3=values+"_mp3.mp3"
            videoclip = VideoFileClip(mp4)
            audioclip = videoclip.audio
            audioclip.write_audiofile(mp3)
            audioclip.close()
            videoclip.close()
            #os.remove(mp4)


mi_mp3=MP3({"https://www.youtube.com/watch?v=4NRXx6U8ABQ":"The Weeknd - Blinding Lights (Official Video)"})
mi_mp3.download_mp4()
