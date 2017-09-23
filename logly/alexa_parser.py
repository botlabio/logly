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
    
    test = test.replace('-','0')
    test['bounce_rate'] = test.bounce_rate.str.replace('%','')
    test['rank'] = test['rank'].str.replace(',','')
    test.loc[test['country_rank'].str.contains('%')] = '0'
    test['country_rank'] = test['country_rank'].str.replace(',','')
    test['bounce_rate'] = test.bounce_rate.str.replace('%','')
    test['search_visits'] = test.search_visits.str.replace('%','')
    test['sites_linkin'] = test['sites_linkin'].fillna(0).str.replace(',','')
    test['branded_search'] = test['branded_search'].fillna(0).astype(int)

    l = []

    for i in test.avg_time.str.split(':'):
        try:
            l.append((int(i[0]) * 60) + int(i[1]))
        except:
            l.append(np.nan)

    test['avg_time'] = l
    test['avg_time'] = test['avg_time'].fillna(0)

    test['rank'] = test['country_rank'].astype(int)
    test['country_rank'] = test['country_rank'].astype(int)
    test['bounce_rate'] = test['bounce_rate'].astype(float)
    test['search_visits'] = test['search_visits'].astype(float)
    test['avg_time'] = test['avg_time'].astype(int)
    test['sites_linkin'] = test['sites_linkin'].astype(int)
    test['branded_search'] = test['branded_search'].astype(int)
    test['avg_pageviews'] = test['avg_pageviews'].astype(float)
    
    return test


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
