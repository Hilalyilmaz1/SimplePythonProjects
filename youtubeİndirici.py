import tkinter as tk
from pytube import YouTube
from tkinter import messagebox,filedialog
import moviepy
from moviepy.editor import *
from pytubefix import YouTube
from pytubefix.cli import on_progress



def download_video():
    url = url_entry.get()
    if not url.startswith("https://www.youtube.com/"):
        messagebox.showerror("Hata", "Geçerli bir YouTube URL'si giriniz.")
        return
    try:
        yt = YouTube(url)
    except Exception as e:
        messagebox.showerror("Hata", f"Bağlantı sırasında bir hata oluştu: {e}")
        return

    # Seçilen format ve kaliteye göre dosya indirme
    stream = yt.streams.filter(res=quality_var.get(), file_extension=format_var.get()).first()
    
    if stream is None:
        messagebox.showerror("Hata", "Seçilen format veya kalite bulunamadı.")
        return
    
    download_path = filedialog.askdirectory()
    if download_path:
        stream.download(download_path)
        messagebox.showinfo("Başarılı", "Video indirildi!")
# Arayüz oluşturma
root = tk.Tk()
root.title("YouTube Video İndirici")

tk.Label(root, text="YouTube URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Format Seç:").pack()
format_var = tk.StringVar(root)
format_var.set("mp4")  # Varsayılan olarak mp4
tk.OptionMenu(root, format_var, "mp4", "mp3").pack()

tk.Label(root, text="Kalite Seç:").pack()
quality_var = tk.StringVar(root)
quality_var.set("720p")  # Varsayılan olarak 720p
tk.OptionMenu(root, quality_var, "144p", "360p", "720p", "1080p").pack()

tk.Button(root, text="İndir", command=download_video).pack()

root.mainloop()  

#def convert_to_mp3(video_path):
    #video = VideoFileClip(video_path)
    #video.audio.write_audiofile(video_path.replace(".mp4", ".mp3"))


