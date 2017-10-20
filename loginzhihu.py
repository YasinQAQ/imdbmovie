import requests
from bs4 import BeautifulSoup
# url = 'https://www.zhihu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
i=1
ranking = 'http://www.imdb.com/chart/top?sort=rk'
imdb_rating = 'http://www.imdb.com/chart/top?sort=ir'
release_date = 'http://www.imdb.com/chart/top?sort=us'
number_of_ratings = 'http://www.imdb.com/chart/top?sort=nv'

response = requests.get(ranking,headers=headers)
# response.encoding="gb2312"
soup = BeautifulSoup(response.text,"html.parser")
tag = soup.find(attrs={'class': 'lister-list'})
for movie in tag.find_all('tr'):
    print i,
    td = movie.find('td', attrs={'class': 'titleColumn'})
    movie_name = td.find('a')
    print movie_name.text,
    movie_year = td.find('span')
    print movie_year.text
    i=i+1
# print tag[1]['value']