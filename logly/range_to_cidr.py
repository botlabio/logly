import netaddr

def range_to_cidr(data):
    
    '''IP Range to CIDR Conversion
    
    WHAT: Takes in a tuple of IP ranges and converts
          it in to a CIDR.
          
    INPUT: Dataframe with two columns where each column is
           IP addresses. 
           
    OUTPUT: netaddr IPSet
    
    '''
    
    temp = netaddr.IPSet()
    
    for ip_range in data.values:
        
        temp_cidr = netaddr.iprange_to_cidrs(ip_range[0], ip_range[1])[0]
        temp.add(temp_cidr)
        
    return temp