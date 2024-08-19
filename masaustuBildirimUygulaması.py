from winotify import Notification,audio
import datetime
import time

toast=Notification(
    app_id="Bildirim Uyarı",
    title="Takip et",
    msg="Buraya Tıkla",
    duration="long",#bildirimin süresi
    icon=r"C:\Users\yilma\Downloads\png-clipart-warning-sign-traffic-sign-road-warning-signs-angle-triangle.png"
)
toast.add_actions(label="Tıkla",
                  launch="https://www.youtube.com/watch?v=CHm2gTkNQxc")
toast.set_audio(audio.Reminder,loop=False)
#toast.show()


bildirim_saati = "13:45"  # 24 saat formatında

# Zaman döngüsü
while True:
    # Şu anki saat
    simdiki_zaman = datetime.datetime.now().strftime("%H:%M")
    
    # Bildirim saati geldiğinde bildirimi göster
    if simdiki_zaman == bildirim_saati:
        toast.set_audio(audio.Reminder, loop=False)  # Bildirim sesi ekle
        toast.show()
        break  # Bildirim gösterildikten sonra döngüyü kır
    
    # 60 saniye bekle (kontrolü azaltmak için)
    time.sleep(60)
