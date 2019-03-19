import os


def remove_text_inside_brackets(text, brackets="()[]"):
    count = [0] * (len(brackets) // 2)
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close
                if count[kind] < 0:
                    count[kind] = 0
                else:
                    break
        else:
            if not any(count):
                saved_chars.append(character)
    return ''.join(saved_chars)


def remove_artist_name(filename,artist):
    key_words = ["%s - " % artist, " - %s" % artist, "%s" % artist]
    for words in key_words:
        filename = filename.replace(words, "")
    return filename


def get_filename(filename):
    filename = filename[:-5] + '.mp3'
    return filename


def rename(filename, id, artist):
    length = len(id)
    new_filename = filename[:-(length + 5)]
    print(new_filename)
    new_filename = remove_text_inside_brackets(new_filename)
    print(new_filename)
    new_filename = remove_artist_name(new_filename, artist)
    print(new_filename)
    os.rename(filename, 'songs/' + new_filename.strip() + '.mp3')
    return new_filename


def kostul(filename):
    omg = '111123454323411111111.mp3'
    os.rename(filename, omg)
    return omg

