def to_rna(dna_strand):   
        
    dna = {'G':'C','C':'G','T':'A','A':'U'}
    rna = ''
    for i in dna_strand:
        if i not in dna.keys():
            raise ValueError("The strand value in input DNA is invalid")
        
        rna += dna[i]
    return rna    
        
        