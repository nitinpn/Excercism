def is_pangram(sentence):
    
    try:
        sentence_l = list(sentence.lower())
        pangram_list = list('abcdefghijklmnopqrstuvwxyz')
        
        result = []
        
        result = [x for x in pangram_list if x in sentence_l ]
        
        return len(result) == 26
    except:
        raise
        
        
    
   