# Python Apps - Data Manipulation

<img src="../images/python-to-excel.png" height="50">

To help with the heavy lifting of analyzing the data four separate python programs were created. Each of these programs were first created in Jupyter Notebooks using the <a href="https://www.anaconda.com/">Anaconda<a> Python envrionment. The main library used for manipulating the data is <a href="https://pandas.pydata.org/">pandas</a>. While the programs could have been combined into one application, it was deamed best to break up the content into separate files to confirm data analysis accuracy. This also made it easier to compare the differences between each processing phase. Python 3+ was used for this development.

> The programs/apps reference the templates located in the <a href="./Sample_Templates">Sample_Templates</a> directory

## Data Analysis Apps

The programs are available in two formats. Jupyter Notebooks and Python.

```
Jupyter Notebooks = ipynb
Python (only) = .py
```

#### <u>A. Generate Results by Lesson from Pre-and Post-Tests</u>

1.  Reads in the pre-and post-test for specific lesson.
2.  Combines and compares the post-vs. pre-test data.
3.  Creates and populates the columns: Score Difference, Score Effect, Completed Challenge, On Time, Measured Effect, and Measured Effect Type.

    > _**Note:** By default Completed Challenge = Yes and On Time = True. If this is incorrect, you must manually change this infomation after the Results Table for the selected lesson is created. You must also update the Measured Effect and Measured Effect Type columns based on the logic defined in the "Has A Measured Effect" Table._

4.  Creates a new file called: `Lesson_1_Results.xlsx`
    > The number changes for each lesson pre-and post-test data that is processed. You must set this in the code!

```
$ Generate Results by Lesson from Pre-and Post-Tests.ipynb
$ Generate_Results_By_Lesson_From_Pre_And_Post_Tests.py
```

#### <u>B. Reduce Lesson Results Based on Consent Forms</u>

1. Reads in the selected lesson results generated from the pre-and post-tests by number. <br />_Example:_ `Lesson 1 Results.xlsx`
2. Reads in the parent-guardian and child consent form excel file which includes parents-guardians that approved the study and children/students consented to the study.
3. Combines the two tables using an inner-merge on the Student / Child Email Fields. If a student information does not show up in the consent table then it will be excluded when creating the new table using the inner-merge.
4. Generates a totals row to calculate averages, sums, and modes as defined in the code and research study documentation.
5. Creates a new file with the updated data called: `Lesson_1_Results_Consented.xlsx`
   > The lesson number changes based what is defined in the code.

```
$ Reduce Lesson Results Based on Consent Forms.ipynb
$ Reduce_Lesson_Results_Based_on_Consent_Forms.py
```

#### <u>C. Encoded Lessons to Protect Student Identity</u>

1. Reads in all lesson files in the consented results directory in a list.
2. Each lessons results table data executes the following steps.
3. The student's first and last values are dropped from the table.
4. Using the `secrets` python library. All email addresses are converted to random hexidecimal values. No duplicate values exist in the table and values cannot be decoded back to the original string/email value.
5. A new excel file is created for the selected lesson file being processed. It is named based on the lesson number currently being processed. <br />_Example:_`Lesson_1_Results_Consented_Encoded.xlsx`
6. Steps 3 - 5 repeat for each lesson file found in the specified directory.

```
$ Encoded Lessons to Protect Student Identity.ipynb
$ Encoded_Lessons_to_Protect_Student_Identity.py
```

#### <u>D. Totals Only Table</u>

1. Reads in all encoded lesson files
2. Moves all total rows into a new table
3. Generates an overall totals row for all lessons
4. Creates a new file called: `Lessons_Calculations_Only.xlsx`

---

### Data Charts

Charts are not generated using python code. This is intentional. Instead the charts are generated within excel so that data can be easily formatted and organized.
