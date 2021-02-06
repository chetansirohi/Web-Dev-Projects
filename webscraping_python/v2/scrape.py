from bs4 import BeautifulSoup
import requests

#we are going to scrape articles and summaries

with open('simple.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

#
# match=soup.title#grabbing the title text,only gives the first title text on the page
# print(match.text) #using .text attribute

#to access multiple title on the page we use find method
# match=soup.find('div',class_='footer')
# print(match)

#good practice is to apply the method on one record and then extend the same method to all the records
for article  in soup.find_all('div',class_='article'):#it will return a list so you can loop over it

    headline=article.h2.a.text
    print(headline)

    summary=article.p.text
    print(summary)

    print()