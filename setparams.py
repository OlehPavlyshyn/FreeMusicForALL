import eyed3
from getimage import get_image
from filename import kostul


def set_artist(filename, artist, image_url):
    audiofile = eyed3.load(u"Oxxxymiron - Башня из слоновой кости (2016)-yrTNDYsG-RU.mp3")
    if (audiofile == None):
        new_name = kostul(filename)
        set_artist(new_name, artist, image_url)
        return new_name
    img = get_image(image_url)
    audiofile.tag.images.set(0, open(img,'rb').read(), 'image/jpeg')
    audiofile.tag.artist = artist
    audiofile.tag.save()
    return filename



