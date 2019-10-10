my_file = open('question4.txt','r') #open the file
answer = open('answer2.txt','w')  #we create the new file where we are going to store the list
all_lines = my_file.readlines()   #read all the lines and create a list for each line
s=" "   #create a variable s that the separation criteria that Im going to use later
all_together=s.join(all_lines)   #Merge all elements on the list just to have them in one
all_together_good = all_together.replace('\n',"")   #I eliminate the n
all_together_good_lower=all_together_good.lower()   #it converts all upper case into lower case
dic_words=dict.fromkeys(all_together_good_lower.split(sep=" "))  #I created a dictonary of words
for i in dic_words:
    dic_words[i] = all_together_good_lower.count(i)