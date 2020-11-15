
import csv
import json

class Group:
    def __init__(self):
        self.name =''
        self.group_members=[]
    def sortGroupmembers(self):
        self.group_members.sort()


class Summary :
    def __init__(self,csv_file,json_file):
        self.csv_File=csv_file
        self.json_File=json_file

    def getGroups(self):
        with open(self.csv_File, 'r') as file:
            reader = csv.reader(file)
            groupList =  next(reader)
            group = Group()
            group.group_members = groupList
            groupList.sort()
            return groupList




sum =  Summary('csvFile.csv','jsonFile.json')
list=sum.getGroups()
print(list)



















#list=['lla','aa','ss','bb','ff']
#list1=list.sort()