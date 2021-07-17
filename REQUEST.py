import requests
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()
root.geometry("400x400")



def pagewrap():
    page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    list(soup.children)
    [type(item) for item in list(soup.children)]
    html = list(soup.children)
b1 = Button(root, command =  pagewrap, width = 22, text = "Press Button for Details")
b1.pack(side = BOTTOM)

root.mainloop()
