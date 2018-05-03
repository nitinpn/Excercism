

class BowlingGame(object):
    def __init__(self):
        
        self.frames = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
        self.frame_number = 1

    def roll(self, pins):
       #Error Handling
        if pins not in (range(11)):
            raise ValueError("Invalid Pin value")
        elif self.frame_number != 10 and (len(self.frames[self.frame_number]) < 2 
            and (sum(self.frames[self.frame_number]) + pins)  > 10):
            raise ValueError("You cannot have more than 10 pins fall in a frame")
        elif self.frame_number == 10:
            if len(self.frames[self.frame_number]) == 2:
                if (self.frames[self.frame_number][1] not in  ['X','S'] 
                   and (self.frames[self.frame_number][1] + pins)  > 10):
                   raise ValueError("You cannot have more than 10 pins fall in a frame")
            elif len(self.frames[self.frame_number]) == 1:
                 if (self.frames[self.frame_number][0] != 'X' 
                   and (self.frames[self.frame_number][0] + pins)  > 10):
                   raise ValueError("You cannot have more than 10 pins fall in a frame")
                
        if self.frame_number == 10:
            if len(self.frames[self.frame_number]) < 2:
                if pins == 10 and len(self.frames[self.frame_number]) == 0:
                    self.frames[self.frame_number].append('X')
                elif pins == 10 and self.frames[self.frame_number][0] == 'X':
                    self.frames[self.frame_number].append('X')    
                else:
                    self.frames[self.frame_number].append(pins)                    
                    if (('X' not in self.frames[self.frame_number]) and 
                        (sum(self.frames[self.frame_number]) == 10)):
                        self.frames[self.frame_number][1] = 'S'
            elif (('X' in self.frames[self.frame_number]) or 
                  ('S' in self.frames[self.frame_number])):
                self.frames[self.frame_number].append(pins)
            else:
                raise IndexError("You only have 2 chances")
                
        elif pins == 10 and len(self.frames[self.frame_number]) == 0:
            self.frames[self.frame_number].append('X')
            self.frame_number +=1
        else:
            self.frames[self.frame_number].append(pins)
            if sum( self.frames[self.frame_number]) == 10:
                self.frames[self.frame_number][1] = 'S'
                self.frame_number +=1
            if len(self.frames[self.frame_number]) == 2:
                self.frame_number += 1             
       
        
    def score(self):
        final_score = 0
        #Validations
        if ('X' in self.frames[10] or 'S' in self.frames[10]) and len(self.frames[10]) < 3:
            raise IndexError("Score cannot be calculated until all frames are played")
        elif len(self.frames[10]) not in [2,3]:
            raise IndexError("Score cannot be calculated until all frames are played")
        for keys,values in self.frames.items():
            if keys not in [9, 10]:
                if 'X' in values:
                    if ('X' in self.frames[keys + 1]):
                        #or 'S' in self.frames[keys + 1] ):                   
                        final_score += 10 + 10
                        if  ('X' in self.frames[keys + 2]):
                            final_score += 10
                        else:                            
                            final_score += self.frames[keys + 2][0]
                    elif ('S' in self.frames[keys + 1]):
                        final_score += 10 + 10
                    else:    
                        final_score += 10 + sum(self.frames[keys + 1])
                elif 'S' in values:
                    if ('X' in self.frames[keys + 1]):
                        final_score += 10 + 10
                    else:
                        final_score += 10 + self.frames[keys + 1][0]
                else:                    
                    final_score += sum(values)
            elif keys == 9:
                if 'X' in values:
                    frame_10_score = [10 if x=='X' else x for x in self.frames[keys + 1]]
                    if frame_10_score[1] == 'S':
                        final_score += 10 + 10
                    else:
                        final_score += 10 + frame_10_score[0] + frame_10_score[1]  
                else:
                    final_score += sum(values)

                
            else:
                frame_10_score = []
                frame_10_score = [10 if x=='X' else x for x in values]
                if len(frame_10_score) == 3:
                    if frame_10_score[1] == 'S':
                        final_score += 10 + frame_10_score[2]
                    elif frame_10_score[2] == 'S':
                        final_score += values[0] + 10
                    else:
                        final_score += sum(frame_10_score)
                else:
                    final_score += sum(frame_10_score)
        self.__init__()
        return final_score
                
        

                