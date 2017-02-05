# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3
import tkinter.messagebox as tmp

c = sqlite3.connect('translation.db').cursor()

with open('words', 'r+') as w:
   words = [i[:-1] for i in w.readlines()]

all_content = ''

def get_translation(w):
    api = 'http://www.youdao.com/w/replace/#keyfrom=dict2.top'
    api = api.replace('replace', w)
    web = urlopen(api)
    bs = BeautifulSoup(web, 'html.parser')
    translates = [i.get_text() for i in bs.find(class_='trans-container').find_all('li')]
    return translates

def checking(w, all_content,total_time = 0):
    t = get_translation(w)
    if t != [] and t != None:
        all_content += w+':'+str(t)+'\n'
        return all_content
    elif total_time < 3:
        checking(w, all_content,total_time+1)

for w in words:
    print(w)
    all_content = checking(w, all_content)

tmp.showinfo(title="At your service", message=all_content)


with open('translated', 'w+') as t:
    t.write(all_content)
