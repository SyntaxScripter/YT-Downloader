import os
import time
import threading
import yt_dlp

os.system('cls' if os.name == 'nt' else 'clear')
os.system("color 79" if os.name == 'nt' else "")
video_downloaded = False


def download_youtube_video(url):
    print("Downloading", end="")
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nVideo downloaded successfully!")


def loading_animation():
    while not video_downloaded:
        for i in range(4):
            print("*", end="", flush=True)
            time.sleep(0.5)
        print("\b\b\b   \b\b\b", end="", flush=True)
        time.sleep(0.5)


def main():
    global video_downloaded
    video_downloaded = False
    url = input("Please enter the YouTube video URL: ")
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()
    download_youtube_video(url)
    video_downloaded = True
    loading_thread.join()


if __name__ == "__main__":
    main()
