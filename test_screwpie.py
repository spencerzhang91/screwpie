from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.douban.com/group/kaopulove/discussion?start=0"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

# the main topic table
table = soup.findAll("table", {"class": "olt"})
# finds the total topics
total_topic_data =  soup.find("span", {"class":"thispage"}).attrs["data-total-page"]
# finds rows of the table, exclude <tr> tags that not holding valid topic data
# the "id" key is to exclude javascript at the beginning of the table rows
rows = list(table)[0].findAll("tr", {"class": "", "id": ""})

title = rows[0].find("td", {"class": "title"}).a.attrs["title"]
title_url = rows[0].find("td", {"class": "title"}).a.attrs["href"]
author = rows[0].find("td", {"nowrap": "nowrap"}).a.text
author_url = rows[0].find("td", {"nowrap": "nowrap"}).a.attrs["href"]
follow = rows[0].find(lambda tag: len(tag.attrs)==2 and tag.name=="td").text
time = rows[0].find("td", {"nowrap": "nowrap", "class": "time"}).text


print(title, title_url)
print(author, author_url)
print(follow)
print(time)