#!/usr/bin/env python
# coding: utf-8

# In[147]:


import datetime
import re
import os
from datetime import datetime
from datetime import date


# In[148]:


#Determine current date
while True:
    print( """
    Pick a Choice!
    The program would perserve the data in the past month. Now select the current date.
    [1]. Default date by local configuration
    [2]. Enter date manually\n
    """)
    choice = input()
    if choice == '1':
        get_date = date.today()
    elif choice == '2':
        print("Please enter date YYYY-MM-DD ")
        tmp_date = input()
        try:
            get_date = datetime.strptime(tmp_date, '%Y-%m-%d').date() 
        except:
            print("Invalid input. Please try again")
            continue
    else:
        print(choice)
        print("Invalid choice. Please try again")
        continue
    print(f'The current date is {get_date}. Continue? Enter any key to continue or enter b to return')
    submit_key = input()
    if submit_key != 'b':
        break
    


# In[149]:


def month_substract(month):
    if month == 1:
        return [1,12]
    else:
        return [0,month-1]


# In[150]:


#Sample date
cur_year = get_date.year
cur_month = get_date.month
[tmp_year_count,get_month] = month_substract(cur_month)
past_year = cur_year - tmp_year_count
past_month = get_month


# In[151]:


#initialize rule string
past_match_string = str(past_year)+'[-_]0?'+str(past_month)
cur_match_string = str(cur_year)+'[-_]0?'+str(cur_month)


# In[152]:


#initialize rule 
rule1 = re.compile(past_match_string)
rule2 = re.compile(cur_match_string)


# In[153]:


while True:
    print("Please enter folder you want to delete files from.")
    enter_folder = input()
    print(f'The folder you enter is {enter_folder}. Are you sure?\nPlease enter yes to continue. Other key would direct to input again.')
    submit_folder = input()
    if submit_folder == 'yes':
        break


# In[154]:


listdir_obj = os.scandir(enter_folder)


# In[155]:


search_files_count = 0


# In[156]:


for file_path in listdir_obj:
    if not file_path.is_file():
        continue
    file = file_path.name
    judge1 = rule1.search(file)
    judge2 = rule2.search(file)
    if judge1 or judge2:
        pass
    else:
        os.remove(os.path.join(enter_folder,file))
    search_files_count += 1
    if search_files_count %1000 ==0:
        print(f'Processed {search_files_count}files.')
    

