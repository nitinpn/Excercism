def word_count(phrase):
    input_string = phrase.lower()
    
    final_dict  = {}
    delimiter_list = []
    for word in input_string:
        
        if (word.isalnum() == False) and ('\'' not in word):
            delimiter_list.append(word)

    if len(delimiter_list) > 1:
        word_list = input_string.split(delimiter_list[0])
        #Remove single quotes in the beginning and end of word
        word_list =  [word.lstrip('\'').rstrip('\'') for word in word_list]
        #As we have already split the words with first delimiter, we use [1:]
        [word_list.extend(x.split(y)) for y in set(delimiter_list[1:]) for x in word_list if y in x]

        duplicates = [x for y in set(delimiter_list)  for x in word_list if y in x]
        #Removing duplicates
        for x in set(duplicates):
            for i in range(word_list.count(x)):
                word_list.remove(x)
    else:       
        final_dict[input_string] = 1
        return final_dict
    
    for word in word_list:
        if len(word) < 1:
            continue
            
        final_dict[word] = word_list.count(word)
    
        
    return final_dict    



 
 