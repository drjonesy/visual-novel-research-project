#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os

# read in file with only last row
# Remove Columns: 'Child_First_Name', 'Child_Last_Name', 'Student_Email' 
# Create a New Column in the front called: 'Lesson' and assign the lesson number
# create index dictionary
# Store each of the lessons in the dictionary
# convert dictionary to DataFrame
# Save DataFrame to File
path = './Lesson_Results_Consented/'
file_save_path = './Encoded_Results/Lesson_Totals_Only.xlsx'
lesson = 1
lessons_list = []

for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    df = pd.read_excel(filepath)
    df.drop(columns=['Child_First_Name', 'Child_Last_Name', 'Student Email'], inplace=True)
    df.insert(0, 'Lesson', lesson)
    lesson_dict = df.iloc[-1].to_dict()
    lessons_list.append(lesson_dict)
    lesson += 1


df_lessons = pd.DataFrame.from_dict(data=lessons_list) 

df_lessons.to_excel(file_save_path, index=False)