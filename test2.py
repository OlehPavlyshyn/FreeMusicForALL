import argparse
import json
import itertools
import logging
import re
import os
import uuid
import sys
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup




REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'html.parser')


def get_query_url(query):
    return u"https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query


def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records


def extract_images(query, num_images):
    url = get_query_url(query)
    soup = get_soup(url, REQUEST_HEADER)
    link_type_records = extract_images_from_soup(soup)
    return itertools.islice(link_type_records, num_images)


def get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()


def save_image(raw_image, image_type, save_directory):
    extension = image_type if image_type else 'jpg'
    file_name = 'name' + "." + extension
    save_path = os.path.join(save_directory, file_name)
    with open(save_path, 'wb') as image_file:
        image_file.write(raw_image)


def download_images_to_dir(images, save_directory, num_images):
    for i, (url, image_type) in enumerate(images):
            raw_image = get_raw_image(url)
            save_image(raw_image, image_type, save_directory)


def run(query, save_directory, num_images=100):
    query = '+'.join(query.split())
    images = extract_images(query, num_images)
    download_images_to_dir(images, save_directory, num_images)


def main():
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default="odun v kanoe v mene nemae domu", type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=1, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default='C:/Users/Oleg/PycharmProjects/FreeMusicForAll/images', type=str,
                        help='save directory')
    args = parser.parse_args()
    run(args.search, args.directory, args.num_images)


if __name__ == '__main__':
    main()