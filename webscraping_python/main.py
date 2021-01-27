from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content,'lxml')
    tags=soup.find_all('h5'
                       )
    print(tags)