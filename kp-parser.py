# -*- encoding: utf-8 -*-
import re
import requests
import pprint
from bs4 import BeautifulSoup

with open('ids.txt', 'r') as f:
    ids = [x.strip() for x in f.readlines()]
# ids = [ids[1]]

def parse_kp(movie_id):
    r = requests.get('http://kinopoisk.ru/film/' + movie_id)
    soup = BeautifulSoup(r.text, "html.parser")

    t_i = soup.select('table.info')[0]
    m_name = soup.select('h1.moviename-big')[0].get_text()
    m_year = t_i.a.get_text()
    m_country = [x.get_text() for x in t_i('a', href=re.compile('country'))]
    m_director = t_i.find(itemprop='director').a.get_text()
    m_actors = [
        x.get_text() for x in
        soup.find(id='actorList').find('ul')('a') if x.get_text() != '...'
    ]
    m_genres = [
        x.get_text() for x in
        t_i('span', itemprop='genre')[0].find_all('a')
    ]
    m_time = t_i.find(id='runtime').get_text().split(' ')[0]
    m_rating = soup('span', class_='rating_ball')[0].get_text()
    m_voters = soup(
        'span', class_='ratingCount'
    )[0].get_text().replace(u'\xa0', '')

    return {
        'id': movie_id,
        'name': m_name,
        'year': m_year,
        'country': ';'.join(m_country),
        'director': m_director,
        'actors': ';'.join(m_actors),
        'genres': ';'.join(m_genres),
        'time': m_time,
        'rating': m_rating,
        'voters': m_voters
    }

with open('res.txt', 'w') as f:
    h = '\t'.join(['id', 'name', 'year', 'country', 'genres', 'rating',
                   'voters', 'time', 'director', 'actors'
    ])
    f.write(h + '\n')
    for i in ids:
        r = parse_kp(i)
        l = '\t'.join([
            r['id'],
            r['name'],
            r['year'],
            r['country'],
            r['genres'],
            r['rating'],
            r['voters'],
            r['time'],
            r['director'],
            r['actors']
        ])
        f.write(l + '\n')