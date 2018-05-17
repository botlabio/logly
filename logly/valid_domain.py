from pandas import read_csv

url = 'http://data.iana.org/TLD/tlds-alpha-by-domain.txt'
tlds = list(pd.read_csv(url, header=None, skiprows=1)[0])

def is_domain(domain):
    
    '''CHECKS IF DOMAIN IS VALID'''

    return domain.split('.')[-1].upper() in tlds
