import requests
from bs4 import BeautifulSoup

n = int(input("Enter how many page you want: "))

def upto_page(n):
    links = []
    subtext = []
    for i in range(n):
        res = requests.get("https://news.ycombinator.com/news?p=" + str(i))
        soup = BeautifulSoup(res.text, 'html.parser')
        links += soup.select('.storylink')
        subtext += soup.select('.subtext')
    return create_custom_hn(links, subtext)    

def sort_storyes_by_votes(hn):
    return sorted(hn, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title':title, 'href':href, 'votes':points})
    return sort_storyes_by_votes(hn)

print(upto_page(n))            