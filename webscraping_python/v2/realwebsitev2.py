from bs4 import BeautifulSoup
import requests
import csv


#scraping data from Corey Schafer's Website for title,summary,links and possibly storing in fcsv
#here we make the use of requests library

source=requests.get('http://coreyms.com').text

soup=BeautifulSoup(source,'lxml')

csv_file=open('realwebsitev2.csv','w')#for writing into a csv file
csv_writer=csv.writer(csv_file)#write method of csv module on csv_file
csv_writer.writerow(['headline','summary','video_link']) #mention the headers of the csvfile



for article in soup.find_all('article'):

    headline=article.h2.a.text
    print(headline)

    summary=article.find('div',class_='entry-content').p.text
    print(summary)

    try:
        # get the embedded links which you want to scrape
        vid_src = article.find('iframe', class_='youtube-player')[
            'src']  # as we have to access the video id we we 'src'
        # print(vid_src)

        vid_id = vid_src.split('/')[4]  # as we know the id is encountered after the '/' we make a split
        vid_id = vid_id.split('?')[0]  # we make a second split as we have to further extract the id before the '?'

        # no we can create our custom youtube links
        yt_link = f'https://youtube.com/watch?v=vid{vid_id}'

    except Exception as e:
        yt_link=None


    print(yt_link)

    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()# closing the file else it gives error