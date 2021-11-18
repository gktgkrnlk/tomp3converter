import youtube_dl

video_url = input("Link giriniz: ")

video_bilgisi = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False)

dosyaAdi = f"{video_bilgisi['title']}.mp3"

ayarlar={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':dosyaAdi,
}

with youtube_dl.YoutubeDL(ayarlar) as ydl:

    ydl.download([video_bilgisi['webpage_url']])

print(f"İndirme Tamamlandı.{dosyaAdi}")
