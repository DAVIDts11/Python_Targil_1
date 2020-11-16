
import csv
import json


def myMode(values):
    """

    :param values:
    :return:
    """
    pass


def Groups_By(set_of_names,group_by,List_csv_dict):
    """
    :describtion : This function takes the dict from csv file , and group the information
        to the list of lists by "group_by" parameter .
    :param set_of_names:  set of all posible names in the "groupBy" column
    :param group_by: key to groupBy param
    :param List_csv_dict:  dict list from csv file
    :return: data_of_all_groups (list of lists each one of these contain all the data of the group)
    """
    data_of_all_groups = []
    for group_name in set_of_names:
        data_of_this_groups = []
        for row in List_csv_dict:
            group_data = []
            if row[group_by] == group_name:
                group_data.append(row)
            else:
                continue
            data_of_this_groups.append(group_data)
        data_of_all_groups.append(data_of_this_groups)
    return  data_of_all_groups





def get_columns_from_group(group_data,features):
    """

    :param group_data:
    :param features:
    :return: dictinary {"feature[0]" : [ list with column[0] content ] ,"feature[1]" : [ list with column[1] content ]  .... .}
    """
    columns_content = {}
    for feature in features :
        column=[]
        for row in group_data :
            column.append(row[0][feature])
        columns_content.update({feature:column})
    return  columns_content




class Group:
    def __init__(self):
        self.name =''
        self.group_members={}




class Summary :
    """

    """
    def __init__(self,csv_file,json_file):
        self.csv_File=csv_file
        self.json_File=json_file
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            self.features = tuple(next(reader))
        with open(json_file, "r") as file:
            self.json_data = json.load(file)
            self.group_By =self.json_data['groupby']

    def getGroups(self):
        List_csv_dict = []
        with open(self.csv_File, 'r') as file:
            csv_dict = csv.DictReader(file)
            for row in csv_dict:
                List_csv_dict.append(dict(row))
            set_of_names =set()
            for row in List_csv_dict :
                set_of_names.add(row[self.group_By])
            data_of_all_groups = Groups_By(set_of_names,self.group_By,List_csv_dict)
            # print(*data_of_all_groups,sep="\n\n")
            group_columns = []
            for group_data in data_of_all_groups :
                group_columns.append(get_columns_from_group(group_data, self.features))
            # print(group_columns)

            list_of_results_group = []        ###
            features_dict ={}
            for feature in self.json_data['features']:
                features_dict.update(feature)
            # print(features_dict,"\n")
            for group in group_columns :
                print(group,"\n")
                result_group = Group()
                for key,value in group.items():

                    # result_group.group_members.update({key:value})
                    # print ("test 2 = " ,result_group.group_members)
                    if key != self.group_By:
                        if features_dict[key]['type'] == 'categorical' :
                            if features_dict[key]['aggregate'] ==  'mode':             #####
                                result_group.group_members.update({key:myMode(value)})
                            elif features_dict[key]['aggregate'] ==  'union':
                                set_from_value= set(value)
                                group_value = ";".join(set_from_value)
                                # test = {}                                              #####
                                # test.update({key:group_value})
                                # print("test = " , test)
                                result_group.group_members.update({key:group_value})
                            elif features_dict[key]['aggregate'] == 'unique':

                                set_from_value = set(value)
                                result_group.group_members.update({key:len(set_from_value)})
                            elif features_dict[key]['aggregate'] == 'count':
                                result_group.group_members.update({key:len(value)})
                        elif features_dict[key]['type'] ==  'numerical' :
                            if features_dict[key]['aggregate'] ==  'min':
                                result_group.group_members.update({key:min(value)})
                            elif features_dict[key]['aggregate'] ==  'max':

                                result_group.group_members.update({key: max(value)})
                            elif features_dict[key]['aggregate'] == 'median':
                                value.sort()
                                mid = len(value) // 2
                                res = (value[mid] + value[~mid]) / 2

                                result_group.group_members.update({key:res})
                            elif features_dict[key]['aggregate'] == 'mean':
                                if len(value) == 0 :                                  ###### prevent  divviation by 0
                                    result_group.group_members.update({key:0})
                                else :
                                    res = sum(value) / len (value)
                                    result_group.group_members.update({key:res})
                            elif features_dict[key]['aggregate'] == 'sum':
                                result_group.group_members.update({key:sum(value)})
                            elif features_dict[key]['aggregate'] == 'mode':
                                result_group.group_members.update({key:myMode(value)})
                            elif features_dict[key]['aggregate'] == 'count':
                                result_group.group_members.update({key:len(value)})

                    else: result_group.name = value[0]
                list_of_results_group.append(result_group)
                    # print(result_group.group_members)

            for g in list_of_results_group:
                print("\n name is:  ",g.name,"\n value is : ",g.group_members)











sum =  Summary('csvFile.csv','jsonFile.json')
sum.getGroups()





# with open('csvFile.csv', 'r') as file:
#     reader = csv.reader(file)
#     features = next(reader)
#     print(features)
#     file.seek(0)
#     csv_dict = csv.DictReader(file)
#     List_csv_dict = []
#     for row in csv_dict:
#         List_csv_dict.append(dict(row))
#         print(List_csv_dict)

with open("jsonFile.json","r") as file:
    data = json.load(file)


# In[ ]:




print(data['groupby'])
# print(data['features'][0])


# list1=[value for value in data['features'][0].values()]
# list2=[value for value in data['features']]
# keys=[]
# for i in list2 :
#     keys.append(i.keys())
# print(keys)

# print(list1[0]['type'])
# print(list1[0]['aggregate'])















#list=['lla','aa','ss','bb','ff']
#list1=list.sort()


# def getGroups(self):
#     with open(self.csv_File, 'r') as file:
#         reader = csv.reader(file)
#         groupList = next(reader)
#         group = Group()  # h   ??????????????
#         group.group_members = groupList  # ???????????????
#         groupList.sort()
#         return groupList