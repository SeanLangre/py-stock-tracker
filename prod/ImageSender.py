import os
import requests

class ImageSender:
    def SendImage(path_img, url, title):
        postData = {"content": title}

        with open(path_img, "rb") as img:
            name_img = os.path.basename(path_img)
            files = {"image": (name_img, img, "multipart/form-data", {"Expires": "0"})}
            with requests.Session() as s:
                r = s.post(url, files=files, data=postData)
                print(r.status_code)

    def SendDeleteMessage(url, msg):
        postData = {"content": msg}
        with requests.Session() as s:
            r = s.post(url, data=postData)
            print(r.status_code)
