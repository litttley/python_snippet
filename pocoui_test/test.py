#!/usr/bin/env python
# encoding: utf-8


import requests





if __name__ =="__main__":
    while True:
        req =requests.get("http://106.12.131.211/")
        if req.status_code ==200:
            print("ss")
            pass
            #print(req.text)