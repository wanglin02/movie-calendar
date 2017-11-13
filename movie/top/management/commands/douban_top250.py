# coding:utf-8

import re
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from top.models import Movie


class Command(BaseCommand):
    help = 'get douban movie top250'

    def handle(self, *args, **options):
        num = 0
        while num <= 250:
            url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
            num += 25
            '''
            利用循环实现翻页并获取网页内容
            '''
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            movies = soup.find_all('div', class_="info")

            for info in movies:
                # 获得电影的中文名
                title = info.find('span', class_='title').text  # find()只找到一个，结果以树结构返回

                # 获得电影在豆瓣中的链接
                link = info.find('a').get('href')

                subject = re.findall('\d+', link)

                # 找到评分以及评价人数
                rating = info.find(class_='rating_num').text

                # 获得一句话评价
                comment_one = info.find('span', class_='inq')
                if comment_one is None:
                    comment = u' '
                else:
                    comment = comment_one.text

                print(subject[0], title, link, rating, comment)

                Movie.objects.update_or_create(subject=subject[0], defaults={'title': title, 'link': link,
                                                                             'rating': rating, 'comment': comment})
