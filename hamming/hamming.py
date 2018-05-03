def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("The length of strands should be same")
    
        
    strand_a_list = list(strand_a)
    strand_b_list = list(strand_b)
    
    return len(strand_a) - sum(map(lambda (x,y): x==y,zip(strand_a_list,strand_b_list)))