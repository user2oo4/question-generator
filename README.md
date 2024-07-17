# Question generator

With knowledge base (as excel file) as input, generate question templates and questions


# Steps

Steps to generate questions

## Install file and read information

- Install the data file and put in a folder with the name **data.xlsx**. 
(E.g.: banking/data.xlsx).
- Change the file_name variable in **codes/excel_read.py** to the name of the folder and execute the code in the command prompt.
- The graph will now be written as dictionary in the folder in 2 files, **knowledge_vertices.py** and **knowledge_graph.py**


## Generate question templates and questions

- Change the folder name in **codes/question_generator.py** and execute. The question templates will show in a file called **4o.txt** in the same folder.
- Select good question templates and put it in the **template.txt** file in the same folder, please see the previous **template.txt** files to know the format it should be in
- Update the folder name and execute **codes/questions.py**, the questions will be shown in **questions.txt** in the same folder.

