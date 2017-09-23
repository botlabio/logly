import pandas as pd
from bs4 import BeautifulSoup

def _alexa_parse(domain):
    
    file_name = 'output/{}.alexa.html'.format(domain)
    
    with open(file_name) as fp:
        soup = BeautifulSoup(fp, 'lxml')
    
    # basic stats
    l = []

    l.append( domain)
    
    for item in soup.find_all("strong", class_="metrics-data align-vmiddle"):
        l.append(item.text.replace('\n','').strip(' '))

    # sites linking in
    l.append(soup.find('span', class_='font-4 box1-r').text)

    # branded keywords

    temp =[]
    for item in soup.find_all('td', class_='topkeywordellipsis'):
        temp.append(0 < item.text.replace('&nbsp','').find('vg'))
    l.append(sum(temp))
    
    return l

def alexa_parser(domains):

    temp = []
    
    for domain in domains: 
        temp_out = _alexa_parse(domain)
        temp.append(temp_out)
    
    temp = pd.DataFrame(temp)
    temp.columns = ['domain',
                    'rank',
                    'country_rank',
                    'bounce_rate',
                    'avg_pageviews',
                    'avg_time',
                    'search_visits',
                    'sites_linkin',
                    'branded_search']
    
    return temp
