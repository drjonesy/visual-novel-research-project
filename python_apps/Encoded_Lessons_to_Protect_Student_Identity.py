#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os
import secrets

dir_in = './Lesson_Results_Consented/'
dir_out = './Encoded_Results/'
lesson = 1
secret_list = []

for filename in os.listdir(dir_in):
    filepath_read = os.path.join(dir_in, filename)
    df = pd.read_excel(filepath_read)
    
    # Remove columns
    df.drop(columns=['Child_First_Name', 'Child_Last_Name'], inplace=True)
    # convert each email address to a random number
    # store that random number in a list and make sure there are no duplicates
    # -1 to ignore totals row
    for i in range(0, len(df['Student Email'])-1):
        while True:
            new_secret = secrets.token_hex(4)
            if new_secret not in secret_list:
                df.at[i, 'Student Email'] = secrets.token_hex(4)
                secret_list.append(new_secret)
                break
    
    # Change the Last Value NaN in the Email Column to the value of 'Calculations'
    df.at[len(df.index)-1, 'Student Email'] = 'Calculations'
    # Change first column to Student
    df.rename(columns={'Student Email': 'Student'}, inplace=True)
    
    # write data to file
    filename_encoded = filename.split('.')[0] + '_Encoded.xlsx'
    filepath_write = os.path.join(dir_out, filename_encoded)
    df.to_excel(filepath_write, index=False)
    
    # clear out secret_list
    secret_list = []