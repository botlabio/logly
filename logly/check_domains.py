import pandas as pd
import logly as lo

from blacklist import blacklist
from combine import combine_sets
from check_ip import check_ip


def check_domains(ip, domain, data, list_mode, head=None, verbose=1):
    
    '''Domain Checker 
    
    WHAT: Takes a list of domain names with IP addresses and checks 
          the fraction of visits from blacklisted sites. 
          
    HOW: check_domains(ip_col, domain_col, df, blacklist='malicious')
    
    INPUT: A pandas dataframe with a column of domains and a column of ips
    
    OUTPUT: A pandas dataframe with fraction of traffic on the blacklist per domain
    
    '''
    
    if list_mode is 'datacenter':
        denylist = blacklist('denylist')
        client9 = blacklist('client9')
        list_mode = combine_sets(denylist, client9)
        
    if list_mode is 'bogon': 
        list_mode = blacklist('cymru')
        
    if list_mode is 'malicious':
        list_mode = blacklist('firehol1')
        
    if list_mode is 'malicious_all':
        temp1 = blacklist('firehol1')
        temp2 = blacklist('firehol2')
        temp3 = blacklist('firehol3')
        temp4 = blacklist('firehol4')
        temp5 = combine_sets(temp1, temp2)
        temp6 = combine_sets(temp3, temp4)
        list_mode = combine_sets(temp5, temp6)
        
    out = []
    
    data[domain] = data[domain].str.lower()
    domains = data[domain].value_counts().index[:head]

    if head is None:
        head = len(domains)
    
    for site in domains:

        temp = data[data[domain] == site][ip]
        total = len(temp)
    
        result = check_ip(temp, list_mode)
        result = float(result) / float(total) * 100
        
        out.append([site, result])
        out = pd.DataFrame(out)
        out.columns = ['domain', 'in_blacklist']
        
        if verbose > 0:
            print("%s : %.2f%%" % (site, result))
        
    return out