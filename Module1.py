# Getting Started with Python: 
# As a universal rule, every first code of a begginer starts with a Hello World:

# We  can simply do this particular task in multiple ways:

string = "Hello World"    
# In python any combination of alphabets stored inside a variable is called "String", and it should be enclosed in a quotation marks "".

print (string) 
"""
print is a built-in function in python which prints or displays the value stored inside a variable.
Like in our case HELLO WORLD (string) is stored in variable named string (this we can choose, i named it string, you may name it something else). 
"""

"""
NOTE: Anything written inside """ """ or # is not read by python while executing the code and hence these are called comments.
It is advisable to comment your code wherever necessary so that when you or someone else read your code can easily understand what's going on.
"""

# Another way with which we can print Hello World (which is an example of a string data type) is directly writing it inside print function
print("Hello World")
#################################################################

# #### VARIABLES #### #
"""
A variable in python is like a container for storing data values, for creating variable in python we just have to declare it.
Just like we did above while storing our Hello World String inside a variable "String"
"""

gene = "BRCA1" 
# Here gene is a variable while BRCA1 is a string (data type) stored inside the variable 

print (gene)
# we can simply know what is inside the variable using print command

#################################################################

# #### INDENTATION #### #
"""
In python, most of the errors arise mainly due to two reasons.
1. Uppercase/ Lowercase errors (more on that later)
2. Indentation errors.
 Indentation refers to the leading blank spaces at the begining of a code line.
 Most of the IDEs automatically add spaces wherever required but we need to make sure that proper spaces are present wherever required
"""
# Example:
sequence_len = 800

if sequence_len > 1000:
    print("long sequence")    # Note that there is some space before print command this is called indentation
else:
    print("Short sequence")

#################################################################
# #### Data Types & Data Structures #### #

"""
Strings: used to store DNA/RNA sequences, gene names
Integers (+/- numbers), floats (decimal numbers): used to store counts, measurements, expression levels, etc.

List: Defined using square brackets [], used for storing sequenctial data that needs to be modified frequently
Tuples: Defined using (), for storing data that need not to be modified
Dictionaries: Defined using {}, for storing key-value pairs like mapping gene IDs to functions.
"""
gene = "BRCA1"  # BRCA1 is a string (always stored inside quotation marks)

bp_count = 150   # 150 is an integer (no need for quotation marks, if stored it will be considered as a string) 

expression_level = 12.67  #float

print("BP Count", bp_count)
# OUTPUT :  BP Count 150

gene_list = ["TP53", "BRCA1", "MYC"]
# here multiple strings are stored in a list and each value can be accessed using indexing
# lists allows modification using append function

gene_list.append("EFGR")
print(gene_list)

# OUTPUT:  ['TP53', 'BRCA1', 'MYC', 'EFGR']  <--- Modified

DNA_bases = ("A", "T", "G", "C")

# DNA_bases.append("C")  <-- This will give an attribute error, as data inside tuples can not be modified
print(DNA_bases)

gene_info = {"TP53": "Tumor Suppressor",
             "BRCA1": "DNA Repair"}   # Dictionary key-value pairs

print (gene_info)


# Type Conversion

# String to FLoat
raw_length = "1500"   # String
length_number = int(raw_length)  # convert to integer
print(length_number)

# String to Float:
raw_count = "2.567"  # String
con_number = float(raw_count)  # convert to float
print(con_number)

# Integer to string
Count = 42
count_string = str(Count)  # convert to string
print (count_string)


# OPERATORS

# Arithmetic
a = 2
b =2
print (a+b)  # addition
print (a/b)  # division
print (a//b) # division
print (a*b)

# Comparision
a = 10
b = 5

print ("Equal", a == b)
print ("Not Equal", a != b)
print ("Greater", a>b)
print ("Less Than", a<b)


# Logical Operators: AND OR NOT
# AND = If both conditions are true
a = 12
b = 15
print(a>b and b<10)

print (a==b or b<10)

print (not a==b)

# Assignment operators
a = 10
print("a=", a)

# Identity
x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)
print (x is z)



# Script
print ("welcome to DNA analyzer")
sequence = "ATGCTGCATAGCA"
print ("Sequence:", sequence)
print ("Length is:", len(sequence))


# Libraries
# MAKE SURE LIBRARY IS ALREADY INSTALLED IF NOT USE "pip install Biopython"
from Bio.Seq import Seq

seq = Seq("ATGCTGCATA")
# REVERSE COMPLEMENT
print("Reverse Complement:", seq.reverse_complement())

import pandas as pd
data = {"Gene": ["TP53", "BRCA1"],
        "Expression": [2.9, 6.7]}
df= pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
Genes= ["TP53", "BRCA1"]
Expression= [2.9, 6.7]
plt.bar(Genes, Expression)
plt.xlabel("Gene")
plt.ylabel("Gene Expression")
plt.show()
