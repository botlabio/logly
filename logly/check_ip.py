import netaddr
import numpy as np

def check_ip(ips, blacklist, dropna=True):
    
    '''IP Blacklist Checker 
    
    WHAT: An efficient way to check a large list of IP addresses 
          against a blacklist either in IP or CIDR format. 
          
    HOW:  check_ip(df[0], deny[0])
    
    INPUT: Two series or lists of IP addresses in string format. 
           NOTE: IP address in non-string format will be dropped 
           automatically as they will yield error otherwise. 
    
    OUTPUT: returns a number of matching records
    
    '''

    ips[ips.map(type) == int]
    
    if dropna is True:
        ips = ips.dropna()
    
    ips = np.array(ips)

    if type(blacklist) is not netaddr.ip.sets.IPSet:
        blacklist = np.array(blacklist)
    
    ip = netaddr.IPSet(ips)
    black = netaddr.IPSet(blacklist)
    out = ip.intersection(black)
    
    return len(out)