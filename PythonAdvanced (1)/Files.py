#!/usr/bin/env python
# coding: utf-8

# # File
# Python allows easy access to files using the built in `open()` method. This method is used for openning both text and binary files for reading and writing. By default, the `open()` method creates an io text wrapper object for reading. Using the optional "b" param allows creating a buffered reader object for binary operations. The optional "w" param is used for writing, and the "a" param for appending to a file.

# In[ ]:


file = open("Lorem.txt") ## equivalent to open("Lorem.txt",rt)


# In[ ]:


file = open("lorem.txt")


# In[ ]:


print(file.read())
file.close()


# *Note: you must explicitly close the file object or Python maintains priority and may block future access*

# ### File Reading

# In[ ]:


file = open("Lorem.txt")
print(file.read())


# In[ ]:


print(file.read())


# *Note: the **file** object holds a reference to the current position in the file. Once finished reading, the reference points to the end of the file and there is no more content to read.*

# In[ ]:


file.seek(0)
print(file.read())


# In[ ]:


file.seek(0)
print(file.read(1))


# In[ ]:


print(file.read(1))


# In[ ]:


print(file.read(3))


# In[ ]:


print(file.readline())


# **We can iterate over the file reader object. This will return lines given '\n' as a seperator.**

# In[ ]:


for line in file:
    print("<----------",line,"---------->")
file.close()


# ### File Writing

# In[ ]:


wFile = open("python.txt","w")
wFile.write("Scientific programming with Python\n")
print(wFile.read())
wFile.close()


# In[ ]:


wFile.close()


# In[ ]:


file=open("python.txt")
print(file.read())
file.close()


# In[ ]:


wFile = open("python.txt","w+")
print(wFile.read())
wFile.write("Scientific programming with Python\n")
wFile.seek(0)
print(wFile.read())
wFile.close()


# *Note: writing to an already existing file will overwrite it completely and set the file pointer at the beginning of the newly empty file*

# In[ ]:


aFile = open("python.txt","a+")
print(aFile.read())
aFile.write("More scientific programming with Python!\n")
aFile.seek(0)
print(aFile.read())
aFile.close()


# In[ ]:


with open("python.txt","a+") as aFile:
    aFile.write("Even more scientific programming with Python!\n")
    aFile.seek(0)
    print(aFile.read())
aFile.seek(0)


# **Using the `with` statement, we can create a scope of code within which the file IO object exists. The file is closed automatically once the scope is exited**

# # CSV Files

# In[ ]:


import csv
with open("world_countries.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# ### We can use the CSV dictionary reader to read a csv file directly into dictionary objects

# In[ ]:


import csv
countries = []
with open("world_countries.csv", 'r') as file:
    csv_dict = csv.DictReader(file)
    for row in csv_dict:
        countries.append(dict(row))
        print(dict(row))


# In[ ]:


print(countries[0])


# In[ ]:


for row in countries:
    print(row["Country"]," - ",row["Code"])


# ### Writing to CSV file

# In[ ]:


fieldnames = [key for key in countries[0].keys()]
print(fieldnames)


# In[ ]:


with open("some_countries.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames)
    writer.writeheader()
    for i,country in enumerate(countries):
        if i % 2 == 0:
            writer.writerow(country)


# In[ ]:


with open("some_countries.csv","r") as file:
    print(file.read())


# # JSON files

# In[ ]:


import json
with open("halflife.json") as file:
    data = json.load(file)


# In[ ]:


print(data)


# In[ ]:


print(data.keys())


# In[ ]:


print(data['220'].keys())


# In[ ]:


print(data['220']['data'].keys())


# In[ ]:


output = data['220']['data']
del output['recommendations']
del output['screenshots']
del output['movies']
del output['metacritic']
print(output.keys())


# In[ ]:


with open("halflife_data.json", "w") as file:
    json.dump(output, file, indent=4)
    


# *Note: indentation is used for human readable formatting and has no affect on content*

# In[ ]:




