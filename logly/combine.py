def combine_sets(set1, set2):
    
    '''Combine Sets w/o Duplicates
    
    WHAT: Combines two IPSet objects in to one 
          while dropping duplicate values. 
    '''
    
    temp = set1.difference(set2)
    out = temp.union(set2)
    
    return out