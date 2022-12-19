#!/usr/bin/env python
# coding: utf-8
import pandas as pd

# functions
def effect_type(value):
    if value > 0: return 'Positive'
    if value < 0: return 'Negative'
    if value == 0: return 'Neutral'

# returns a tuple
def measured_effect_and_type(score_effect, on_time):
    if score_effect == 'Positive' and on_time == True: return 'Yes', 'Positive'
    elif score_effect == 'Negative' and on_time == False: return 'Yes', 'Negative'
    else:
        return 'No', 'None'

# define lesson number
lesson_num = 4
# file paths
parent_child_consent_form_file = './Parent_And_Child_Conent_Forms_Merged.xlsx'
lesson_form_file = f'./Lesson_Results/Lesson_{lesson_num}_Results.xlsx'
lesson_results_consented_file = f'./Lesson_Results_Consented/Lesson_{lesson_num}_Results_Consented.xlsx'

df_consent_form = pd.read_excel(parent_child_consent_form_file)
df_lesson = pd.read_excel(lesson_form_file)

df_consent_form = df_consent_form[['PG_First_Name', 'PG_Last_Name', 'Child_First_Name', 'Child_Last_Name', 'Child_Email']]
df_consent_form = df_consent_form.drop_duplicates(subset=['Child_Email'])
df_consent_form = df_consent_form.sort_values(by=['Child_Email'])
df_consent_form = df_consent_form.reset_index(drop=True)

df_lesson_consented = df_consent_form.merge(df_lesson, how='inner', left_on='Child_Email', right_on='Student Email')

df_lesson_consented.drop(['PG_First_Name', 'PG_Last_Name', 'Child_Email'], axis=1, inplace=True)

# build Totals / Last Row
# create new data frame with existing column names. Convert to Index Dictionary.
df_totals = pd.DataFrame(columns=df_lesson_consented.columns.values.tolist())
df_totals.loc[0] = ''
dict_totals = df_totals.to_dict(orient='index')

# Populate Totals Row
dict_totals[0]['Pre-Test'] = df_lesson_consented['Pre-Test'].mean(axis=0, skipna=True).round(decimals=2)
dict_totals[0]['Post-Test'] = df_lesson_consented['Post-Test'].mean(axis=0, skipna=True).round(decimals=2)
dict_totals[0]['Score Difference'] = dict_totals[0]['Post-Test'] - dict_totals[0]['Pre-Test']
dict_totals[0]['Score Effect'] = effect_type(dict_totals[0]['Score Difference'])
dict_totals[0]['Completed Challenge'] = df_lesson_consented['Completed Challenge'].mode(dropna=True)[0]
dict_totals[0]['On Time'] = df_lesson_consented['On Time'].mode(dropna=True)[0]
dict_totals[0]['Measured Effect'] = measured_effect_and_type(dict_totals[0]['Score Effect'], dict_totals[0]['On Time'])[0]
dict_totals[0]['Measured Effect Type'] = measured_effect_and_type(dict_totals[0]['Score Effect'], dict_totals[0]['On Time'])[1]

# create an additional row and insert dictionary data
df_lesson_consented.loc[len(df_lesson_consented.index)] = dict_totals[0]

# df_lesson_consented - Write to File
df_lesson_consented.to_excel(lesson_results_consented_file, index=False)
