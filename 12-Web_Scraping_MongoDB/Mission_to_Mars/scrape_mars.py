from bs4 import BeautifulSoup as bs
import requests
import pymongo
import pandas as pd
from selenium import webdriver
from splinter import Browser
import time
import re
import os
import ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def scrape_all():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path) 
    news_title, news_summary = scrape_info(browser)
    mars_prof,mars_earth = mars_facts()
    mars_data={
        "news_title": news_title,
        "news_summary": news_summary,
        "mars_image": featured_image(browser),
        "mars_weather": mars_weather(browser),
        "mars_profile_t":  mars_prof,
        "mars_earth_t": mars_earth
    } 
    browser.quit()
    return mars_data

# def latest_article():    
#     mars_news = mongo.db.latest_news.find_one()
#     return render_template("index.html", mars_news=mars_news)

def init_browser():
    executable_path = {
        "executable_path": "/Users/Andrea Rose/Documents/Boot_Camp/Application_Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info(browser):
    news_url = 'https://mars.nasa.gov/news'
    browser.visit(news_url)
    browser.is_element_present_by_css("ul.item_list li.slide",wait_time=0.5)
    html=browser.html
    news_soup = bs(html,"html.parser")
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        news_title = slide_elem.find("div",class_="content_title").get_text()
        news_summary = slide_elem.find("div",class_="article_teaser_body").get_text()
    except AttributeError:
        return None, None
    return news_title,news_summary

def featured_image(browser):
    url_element = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_element) 
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text("more info",wait_time=0.5)
    more_info_element = browser.find_link_by_partial_text('more info')
    more_info_element.click()
    html = browser.html
    image_soup = bs(html,"html.parser")
    image_url = image_soup.select_one("figure.lede a img").get("src")
    mars_image = 'http://www.jpl.nasa.gov' + image_url
    return mars_image

def mars_weather(browser):
    mars_twitter = 'https://twitter.com/MarsWxReport'
    browser.visit(mars_twitter)
    time.sleep(5)
    html=browser.html
    twitter_soup = bs(html,"html.parser")
    tweet = twitter_soup.find("div", attrs={"class":"tweet","data-name": "Mars Weather"})
    try:
        mars_weather = tweet.find("p", "tweet-text").get_text()
    except AttributeError:
        pattern = re.compile(r'sol')
        mars_weather = twitter_soup.find('span', text=pattern).text
    return mars_weather

def mars_facts():
    mars_df = pd.read_html("https://space-facts.com/mars")
    #mars_df.colums=["description","value"]
    #mars_df.set_index("description",inplace=True)
    mars_profile_t = mars_df[0].to_html(classes="table table-striped")
    mars_earth_t =mars_df[1].to_html(classes="table table-striped")
    return mars_profile_t,mars_earth_t

if __name__ == "__main__":
    print(scrape_all())