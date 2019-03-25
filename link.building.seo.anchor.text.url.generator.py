import re
import csv

# Load Your Keywords Text File From http://www.semantic.IO
filename = r'C:\Users\googl\Desktop\Python\3a - Scripts\2a - Natural Language Processing\1a - Keyword Generator\autoparts.txt'

# Open The File
with open(filename) as f:
    lines = f.readlines()
    print(lines)

file = ''.join(lines)

# Test The Data Type
""" For example: <class 'str'>, <class 'list'>"""
print(type(file))

# Debug Output
# print(file)

# Little Regex Replace Spaces With Urls
file = re.sub(r"\n ", ",", file)

# Debug Out
# print(file)

keyword_list = file

keyword_list = keyword_list.split('\n')

# Debug 
# print(keyword_list)

# Build URL
for i in range(len(keyword_list)):
    keyword_list[i] = "https://chadsautoparts.com/" + keyword_list[i] + "/"

print(keyword_list)

# Little Regex Replace Spaces With Urls
file = re.sub(r"-", " ", file)

anchors = file

# Test The Data Type
""" <class 'str'> """
print(type(file))

# 
anchors = anchors.split('\n')
print(anchors)

# 
final_export = dict(zip(anchors, keyword_list))

#
print(final_export)

# Write To File, Name It Whatever You Want
filename = 'anchors.and.urls.csv'

with open(filename, 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in final_export.items():
       writer.writerow([key, value])


# Open The File and Inspect
with open('anchors.and.urls.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)



