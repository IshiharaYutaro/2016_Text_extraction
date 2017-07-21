#coding: UTF-8
from readability.readability import Document
from bs4 import BeautifulSoup
import html2text
import urllib
import codecs


f = open('input.html')
htmldata= f.read()

readable_article = Document(htmldata).summary()
readable_title = Document(htmldata).short_title()

soup =BeautifulSoup(readable_article,"lxml")
soup.get_text()
soup.find("img")
soup.find("a")
soup.extract()
readable_article=soup.get_text()

f = codecs.open('output.html', 'w','utf-8')
f.write(readable_title);
f.write(readable_article);

readable_article=html2text.html2text(readable_article,)

f = codecs.open('output.txt', 'w','utf-8')
f.write(readable_title);
f.write(readable_article);
f.close()

