import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def _alexa_parse(domain):
    
    '''Helper for Alexa Parser
    '''
    
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


def _alexa_cleanup(data):
    
    data['rank'] = data['rank'].str.replace(',','')
    data['bounce_rate'] = data.bounce_rate.str.replace('%','')
    data['search_visits'] = data.search_visits.str.replace('%','')
    data['sites_linkin'] = data['sites_linkin'].fillna(0).str.replace(',','')
    data['branded_search'] = data['branded_search'].fillna(0).astype(int)

    l = []

    for i in data.avg_time.str.split(':'):
        try:
            l.append((int(i[0]) * 60) + int(i[1]))
        except:
            l.append(np.nan)

    data['avg_time'] = l

    data['avg_time'] = data['avg_time'].fillna(0)


def alexa_parser(domains):
    
    '''Alexa Parser
    
    WHAT: Takes in Alexa site info html and gives back 
    key metrics in return. Handles around 10 pages per second. 
    
    HOW: alexa_parser(domains[0])
    
    '''

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
    
    temp = _alexa_cleanup(temp)
    
    return temp
