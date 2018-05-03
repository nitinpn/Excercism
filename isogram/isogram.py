def is_isogram(string):
    try:
        
        if len(string) < 1:
            return True                  
        string_list = list(string.replace(" ",'').replace("-",'').lower())
        isogram_yn = True    
        
        for i in range(len(string.replace(" ",'').replace("-",'').lower())):                      
            string_list = list(string.replace(" ",'').replace("-",'').lower())            
            if string_list.pop(i) in string_list:
                isogram_yn = False                
                break       
        
        return isogram_yn   
            
    except Exception as e:
        print "Exception: " + str(e)
    except:
        print "Error!!!"


       
