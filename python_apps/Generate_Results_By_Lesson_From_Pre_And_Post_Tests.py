#!/usr/bin/env python
# coding: utf-8
# import pandas for spreadsheet manipulation
import pandas as pd

# Read in Pre-and Post-Test Excel Files
df_pre = pd.read_excel('./Lesson_4_Pre_Test.xlsx')
df_post = pd.read_excel('./Lesson_4_Post_Test.xlsx')

# Prepare Data Frame Pre-Test
df_pre = df_pre[['Email Address', 'Score']]
df_pre = df_pre.rename(columns={'Email Address': 'Email_Address', 'Score': 'Pre_Test_Score'})
df_pre = df_pre.drop_duplicates(subset=['Email_Address'])
df_pre = df_pre.sort_values(by=['Email_Address'])
df_pre = df_pre.reset_index(drop=True)

# Prepare Data Frame Post Test
df_post = df_post[['Email Address', 'Score']]
df_post = df_post.rename(columns={'Email Address': 'Email_Address', 'Score': 'Post_Test_Score'})
df_post = df_post.drop_duplicates(subset=['Email_Address'])
df_post = df_post.sort_values(by=['Email_Address'])
df_post = df_post.reset_index(drop=True)

# Merge Pre-and Post-Test Data Frames by Email Address Column
df_scores = pd.merge(df_pre, df_post, on='Email_Address')
# Score = Post Score - Pre Score
df_scores['Score_Diff'] = df_scores['Post_Test_Score'] - df_scores['Pre_Test_Score']
# convert Data Frame to Dictionary
list_of_students = df_scores.to_dict(orient='records')

# Define Score Effect Type
for student in list_of_students:
    if student['Score_Diff'] > 0: student['Effect'] = 'Positive'
    if student['Score_Diff'] < 0: student['Effect'] = 'Negative'
    if student['Score_Diff'] == 0: student['Effect'] = 'Neutral'
    
    # include columns for completed challenge and on time
    student['Completed_Challenge'] = 'Yes'
    student['Challenge_On_Time'] = True

# Define if there is a measurable effect and if it is postive, negative, or None
for student in list_of_students:
    if student['Effect'] == 'Positive' and student['Challenge_On_Time'] == True: 
        student['Measured_Effect'] = 'Yes'
        student['Measured_Effect_Type'] = 'Positive'
    elif student['Effect'] == 'Negative' and student['Challenge_On_Time'] == False:
        student['Measured_Effect'] = 'Yes'
        student['Measured_Effect_Type'] = 'Negative'
    else:
        student['Measured_Effect'] = 'No'
        student['Measured_Effect_Type'] = 'None'


# Convert Updated Dictionary back to Data Frame
df_scores = pd.DataFrame(list_of_students, columns=['Email_Address', 'Pre_Test_Score', 'Post_Test_Score', 'Score_Diff', 'Effect', 'Completed_Challenge', 'Challenge_On_Time', 'Measured_Effect','Measured_Effect_Type'])
# Rename Columns of Data Frame
df_results =  df_scores.rename(columns={'Email_Address': 'Student Email', 'Pre_Test_Score': 'Pre-Test', 'Post_Test_Score': 'Post-Test', 'Score_Diff': 'Score Difference', 'Effect' : 'Score Effect', 'Completed_Challenge': 'Completed Challenge', 'Challenge_On_Time': 'On Time', 'Measured_Effect': 'Measured Effect', 'Measured_Effect_Type': 'Measured Effect Type'})

# Write Data Frame to Excel File, Do no include the index number column
df_results.to_excel('./Results_By_Lesson/Lesson_4_Results.xlsx', index=False)
