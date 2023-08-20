import os
import time

from bs4 import BeautifulSoup
import requests


def pars():
    if os.path.isfile("./set/atvList.txt"):
        # Variable search logic in 'atvList.txt' file
        with open("./set/atvList.txt", "r") as file:
            content = file.read()
        file.close()

        if content.find("$") == -1:
            print("[Error] Tag variable missing 'atvList.txt'")
            return

        print("[Info] Handling Tag Variables...")
        substringsTag = content.split('$')[1::2]
        tagList = [substring.strip() for substring in substringsTag]

        time.sleep(3)
        if content.find("@") == -1:
            print("[Warning] Class variable missing 'atvList.txt'")
        else:
            print("[Info] Handling Class Variables...")

        substringsClass = content.split('@')[1::2]
        classList = [substring.strip() for substring in substringsClass]

        # Parsing
        url = input("URL of the site you want to scrape from: ")
        print(url)
        page = requests.get(url)

        if page.status_code == 200:
            print("[Info] Successfully connected, you can parse :)")

            allAnime = []
            resultHtml = BeautifulSoup(page.text, "html.parser")

            for tegResult in tagList:
                for classResult in classList:
                    allAnime = resultHtml.findAll(tegResult, classResult)

            for animes in allAnime:
                print(animes.h3.text)

        elif page.status_code == 403:
            print(f"[Error] The {url} server accepted the request but refused to authorize it")
        else:
            print(f"[Error] Error with status code: {page.status_code}")

    else:
        print("[Error] Initialize parse '-init'!")
