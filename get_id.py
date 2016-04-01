import re

def writeToFile(name, obj):
    with open(name + '.txt', 'w') as f:
        for i in obj:
            f.write(i + '\n')

id_pattern = re.compile('http://plus\.kinopoisk\.ru/film/\d*/')

with open('kp-wed-top-html.txt', 'r') as f:
    urls = id_pattern.findall(f.read())

urls = list(set(urls))  # remove duplicates
ids = [x.split('/')[-2] for x in urls]  # get ids from urls

writeToFile('urls', urls)
writeToFile('ids', ids)