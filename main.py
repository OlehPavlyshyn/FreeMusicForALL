from flask import Flask,request
import dowloader
import json

app = Flask(__name__)




@app.route("/url", methods=['POST'])
def download():
    url = request.json
    image_url = dowloader.download_mp3(url['url'])
    return str(image_url)


if __name__ == "__main__":
    app.run()
