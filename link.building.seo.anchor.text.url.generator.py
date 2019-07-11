import re
import csv

# Load Your Keywords Text File From https://semantic.io
filename = r'Desktop/Python/autoparts.txt'

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
anchors = re.sub(r"\n ", ",", file)

# Debug Out
# print(anchors)

# Start Creating a New List
keyword_list = anchors

# Make The List By Splitting Srtings With New Line
keyword_list = keyword_list.split('\n')

# Debug 
print(keyword_list)

# Little Regex Replace Hyphens With Spaces
# Here We're Building The Key Part of The Dictionary, You Know Key:Value, Here Value Being Achor Text and Key Full URL
anchors = re.sub(r"-", " ", anchors)

# Debug
print(anchors)

# Build URL
for i in range(len(keyword_list)):
    keyword_list[i] = "https://chadsautoparts.com/" + keyword_list[i] + "/"

print(keyword_list)

# Little Regex Replace Spaces With Hyphens
anchors = re.sub(r" ", "-", anchors)

#Debug
print(anchors)

link_friendly_list = ''.join(anchors)

# Debug, Check The List Output
print(link_friendly_list)

# Make A List, By Splitting With New Line
link_friendly_list = link_friendly_list.split('\n')

# Build URL
for i in range(len(link_friendly_list)):
    link_friendly_list[i] = "https://chadsautoparts.com/" + link_friendly_list[i] + "/"

print(link_friendly_list)

# Test The Data Type
""" <class 'str'> """
print(type(link_friendly_list))

# Debug, Verify Your Anchors
print(anchors)

# Have To Edit The Old Anchor Variable and Replace Those Hyphens With Spaces For Key In 
# The Dictionary Pair
anchors = re.sub(r"-", " ", anchors)

# Split Anchors To Add To a New List For Exporting and Building The Dictionary Pair
anchors = anchors.split('\n')

# Debug, Verify Your Anchors, Should Be In a List This Time
print(anchors)

# Export and Build Dictionary Pair
final_export = dict(zip(anchors, keyword_list))

# Debug, Inspect
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



