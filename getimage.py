import urllib.request


def get_image(url):
    filename = "images/song_cover.jpg"
    urllib.request.urlretrieve(url,filename)
    return filename

