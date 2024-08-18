import datetime
import tkinter as tk
import pygame


ana_pencere=tk.Tk()
ana_pencere.title("Çalar Saat")

saat_etiketi=tk.Label(ana_pencere,font=('calibri', 40, 'bold'), background='purple', foreground='white')
saat_etiketi.pack(anchor='center')

alarm_saati = tk.Entry(ana_pencere)
alarm_saati.pack(anchor='center')

alarm_buton = tk.Button(ana_pencere, text="Alarm Kur", command=lambda: alarm_kur())
alarm_buton.pack()


#zamanın güncellenmesi
def time_guncel():
    simdiki_zaman = datetime.datetime.now().strftime("%H:%M:%S")
    saat_etiketi.config(text=simdiki_zaman)
    saat_etiketi.after(1000, time_guncel)


alarm_zamani = None
def alarm_kur():
    global alarm_zamani
    alarm_zamani = alarm_saati.get()

    try:
        datetime.datetime.strptime(alarm_zamani, "%H:%M")
    except ValueError:
        alarm_zamani = None
        print("Geçersiz saat formatı. Lütfen HH:MM formatında girin.")


pygame.mixer.init()

def alarm_kontrol():
    if alarm_zamani == datetime.datetime.now().strftime("%H:%M"):
        pygame.mixer.music.load("alarm1.mp3")
        pygame.mixer.music.play()
    ana_pencere.after(1000, alarm_kontrol)


# Zamanı güncelle
time_guncel()

# Alarm kontrolünü başlat
alarm_kontrol()

# Ana pencereyi başlat
ana_pencere.mainloop()
