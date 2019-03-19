from __future__ import unicode_literals
import youtube_dl
from setparams import set_artist
from filename import rename, get_filename


def download_mp3(url):
    class MyLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        id = info.get("id", None)
        filename = get_filename(ydl.prepare_filename(info))
        artist = info['artist'],
        new_filename = set_artist(filename, info['artist'], info['thumbnails'][0]['url'])
        new_name = rename(new_filename, id, artist)
    return "Succesfully downloaded - \"%s\"" % new_name





