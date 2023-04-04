from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import vergedb
import datetime
import os

url = 'https://www.theverge.com/'
response = requests.get(url)
browser = webdriver.Chrome()
browser.delete_all_cookies()
browser.get(url)
soup = BeautifulSoup(browser.page_source,'html5lib')

headers=[]
Urls=[]
authors=[]
dates=[]

# create a table in the database
vergedb.create_table()



def getHeaderArticles():

    articles = soup.find('div',{'class':'relative border-b border-gray-31 pb-20 md:pl-80 lg:border-none lg:pl-[165px] -mt-20 sm:-mt-40'})
    headline = articles.h2.text
    link = url+articles.h2.a['href']
    author_text = articles.div.div.a.text
    find_date = soup.find('div',{'class':'inline-block'})
    date = find_date.span.text
    headers.append(headline)
    Urls.append(link)
    authors.append(author_text)
    dates.append(date)

    vergedb.insert_article(headline,link,author_text,date)
    return [dict(headline=headline,url=link,author=author_text,date=date)]

def get_main_articles():
    articles = soup.find_all('div',{'class':'max-w-content-block-standard md:w-content-block-compact md:max-w-content-block-compact lg:w-[240px] lg:max-w-[240px] lg:pr-10'})   
    lst=[]
    for article in articles:
        headline = article.h2.text
        link = url+article.h2.a['href']
        author_text = article.div.a.text
        datetime = article.div.span.text
        headers.append(headline)
        Urls.append(link)
        authors.append(author_text)
        dates.append(datetime)

        #insert records into the articles table      
        vergedb.insert_article(headline,link,author_text,datetime)
        lst.append(dict(headline=headline,url=link,author=author_text,date=datetime))
    return lst
    


def get_side_articles():
    side_articles = soup.find_all('div',{'class':'max-w-content-block-mobile'})
    lst=[]
    for article in side_articles:
        headline = article.h2.text
        if headline == 'Advertiser Content':
            continue

        link = url+article.h2.a['href']
        author = article.find('div',attrs={'class':'inline-block'})
        author_text = author.a.text
        if author.span.text.strip()=='and':
            next_author = author.span.find_next_sibling('a')
            author_text+=author.span.text + next_author.text
        else:
            datetime = author.span.text
        headers.append(headline)
        Urls.append(link)
        authors.append(author_text)
        dates.append(datetime)

        vergedb.insert_article(headline,link,author_text,datetime)
        lst.append(dict(headline=headline,url=link,author=author_text,date=datetime))
    return lst


def create_filename():
    f = datetime.datetime.today().strftime('%d%m%Y') + '_verge.csv'
    return f

def create_csv(headers,Urls,authors,date_time):
    # create a dataframe with the lists as columns of the dataframe and save it into a csv file

    df = pd.DataFrame({'Header':headers,'URL':Urls,'Author':authors,'Date':date_time})
    df.index.name = 'id'
    f = create_filename()
    f_path = os.path.join('D:\\python-progs\\theverge-assignment\\',f)
    if os.path.exists(f_path):
        os.remove(f_path)
    with open(f,'w') as f:
        df.to_csv(f,index=True,header=f.tell() == 0,encoding='UTF-8')



if __name__ == '__main__':
    getHeaderArticles()
    get_main_articles()
    get_side_articles()
    create_csv(headers,Urls,authors,dates)
