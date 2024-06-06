from flask import Flask, render_template, request, send_file
from pytube import YouTube
from pydub import AudioSegment
import os
import hashlib

app = Flask(__name__)
CACHE_DIR = 'cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def get_video_id(url):
    return YouTube(url).video_id

def generate_file_path(video_id, resolution, file_type):
    return os.path.join(CACHE_DIR, f"{video_id}_{resolution}.{file_type}")

def download_video(url, resolution):
    yt = YouTube(url)
    video_id = get_video_id(url)
    
    if resolution == 'audio':
        file_path = generate_file_path(video_id, resolution, 'mp3')
        if not os.path.exists(file_path):
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download()
            audio = AudioSegment.from_file(out_file)
            audio.export(file_path, format="mp3")
            os.remove(out_file)
        return file_path
    else:
        file_path = generate_file_path(video_id, resolution, 'mp4')
        if not os.path.exists(file_path):
            stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
            if not stream:
                stream = yt.streams.get_highest_resolution()
            stream.download(output_path=CACHE_DIR, filename=f"{video_id}_{resolution}.mp4")
        return file_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        choice = request.form['choice']
        resolution = request.form.get('resolution', 'highest')
        file_path = download_video(url, 'audio' if choice == 'mp3' else resolution)
        return send_file(file_path, as_attachment=True)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
