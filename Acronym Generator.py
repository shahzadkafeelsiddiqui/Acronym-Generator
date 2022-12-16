import pandas as pd 
import os
a,v,t,s,y = 0,1,1,1,1
d,temp1,temp2,temp = {},{},{},{}
# File to Write Data
file1 = open('siddiqui_trees_abbrevs.txt', 'w')
# Function to read the text file with words
def readtext():
    global data_into_list
    with open('trees.txt') as f:
        contents1 = f.read()
        data_into_list = contents1.split("\n")  
       
# Function to read the values of the alphabets  
def readvalues():
    global value
    global d
    with open("values.txt") as f:
        for line in f:
            
            (key, val) = line.split()
            d[key] = int(val)
            value = sorted(d.items(), key=lambda x:x[1])
            
# Function to create acronyms
def acronymgenerator():
    global a, t , y , v, s , phrase ,word,acronym, temp,temp1,temp2, ABV1, ABV2
    # For loop to clean the text file
    for words in data_into_list:
        acronym=""
        input_user= data_into_list[a]
        newclean_input = (input_user.replace("'", ''))
        newclean_input = (newclean_input.replace('-', ' '))
        phrase = newclean_input.split()
        word = ' '.join(phrase)
        a +=1
        print ((word))
        L = word+ " \n"
        file1.writelines(L)
        
        # Loop to iterate the single word names
        if (len(phrase) == 1):
            acronym = acronym + words[0].upper()
            
            if (len(acronym) <2):
                
                while (t < len(word)):
                    if t == 1:
                        temp[word[t].upper()] = (d[word[t].upper()]) + 1
                        t += 1
                    elif t == 2:
                        temp[word[t].upper()] = (d[word[t].upper()]) + 2
                        t += 1
                    elif t >2:
                        temp[word[t].upper()] = (d[word[t].upper()]) + 3
                        t += 1    
                t += 1
                
                firstindex= list(temp.keys()).index(min(temp, key=temp.get)) 
                firstsmall = (min(temp, key=temp.get))
                del temp[min(temp, key=temp.get)]
                secondsmall = (min(temp, key=temp.get))
                secondindex= list(temp.keys()).index(min(temp, key=temp.get))
                if firstindex <= secondindex:
                    acronym = acronym + firstsmall + secondsmall
                elif firstindex >= secondindex:
                    acronym = acronym + secondsmall + firstsmall   
                temp = {}
                t = 1
                print (acronym)
                L = acronym+ " \n"
                file1.writelines(L)       
        # Loop to iterate the two word names    
        if (len(phrase) == 2):
            acronym = acronym + words[0].upper()
        
            
            while (s < len(phrase[0])):
               
                if s == 1:
                    temp1[word[s].upper()] = (d[word[s].upper()]) + 1
                    s += 1
                elif s == 2:
                    temp1[word[s].upper()] = (d[word[s].upper()]) + 2
                    s += 1
                elif (s>2):
                    temp1[word[s].upper()] = (d[word[s].upper()]) + 3
                    s += 1    
            s = 1
            
            firstsmall1 = (min(temp1, key=temp1.get))
            score1 = temp1[firstsmall1]
                           
            temp1 = {}
            
            while (y < len(phrase[1])):
                if y == 1:
                  
                    temp2[phrase[1][y].upper()] = (d[phrase[1][y].upper()]) + 1
                    y += 1
                elif y == 2:
                    temp2[phrase[1][y].upper()] = (d[phrase[1][y].upper()]) + 2
                    y += 1
                elif (y>2):
                    temp2[phrase[1][y].upper()] = (d[phrase[1][y].upper()]) + 3
                    y += 1    
            y = 1
            
            firstsmall2 = (min(temp2, key=temp2.get))
           
            score2 = temp2[firstsmall2]
            
            temp2 = {}
            if score1 < score2:
                final = acronym + firstsmall1 + phrase[1][0].upper()
                print (final)
                L = final+ " \n"
                file1.writelines(L)
                
            elif score1> score2:
                final = acronym + phrase[1][0].upper() + firstsmall2 
                print (final)
                L = final+ " \n"
                file1.writelines(L)
               
            elif score1 == score2:
                finalz = acronym + firstsmall1 + phrase[1][0].upper()
                finalz1 = acronym + phrase[1][0].upper() + firstsmall2
                
                print (finalz + " " +finalz1 )
                L = finalz + " " +finalz1 + " \n"
                file1.writelines(L) 
                    
                
        # Loop to iterate the three word names     
        if (len(phrase) == 3): 
            acronym = acronym + phrase[0][0].upper() + phrase[1][0].upper() + phrase[2][0].upper() 
            print (acronym) 
            L = acronym+ " \n"
            file1.writelines(L)
  
            
# Main function 
def main():
    readtext()
    readvalues()
    acronymgenerator()
    
   
main()

