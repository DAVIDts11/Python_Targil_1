
import csv
import json

def MySort(group):
    return group.name

def myMode(list_of_values):
    # """
    # describtion : this function recive list and return a mone of the list
    #         {the value that appears the most in it }
    # :param list of values:
    # :return:  – value which appears most (ties broken by lowest / first in alphabetical order value)
    # """
    # values  = list_of_values            #  to protect list  from chanches
    # maxItm = -1
    # maxVal = None
    # for i in range(len(values)):
    #     temp = values[i]
    #     counter = 0
    #     for j in range(len(values)):
    #         if (values[j] == temp) and (values[j] != None):
    #             values[j] = None
    #             counter += 1
    #     if counter > maxItm:
    #         maxItm = counter
    #         maxVal = temp
    #     elif counter == maxItm:
    #         if temp < maxVal:
    #             maxVal = temp
    # return maxVal
    return max(set(list_of_values), key=list_of_values.count)

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
        self.featur_aggregate_dict = {}

    def __getitem__(self, key):
        res = None
        list = []
        for k, v in self.group_members.items():
            list.append({k: v})
        if type(key) == int and -len(list) <= key < len(list):
            res = list[key]
        elif type(key) == str and key in self.group_members.keys():
            res = self.group_members.get(key)
        return res

    def __iter__(self):
        members_tuple = [(k, v) for k, v in self.group_members.items()]
        return iter(members_tuple)

    def __str__(self):
        str ="{self.name} -".format(self=self)
        for key,value in self.group_members.items():
            str+= " {} ({}):{},".format(key,self.featur_aggregate_dict[key],value)
        str = str[:-1]
        return  str



class Summary :
    """

    """
    def __init__(self,csv_file,json_file):
        self.csv_File=csv_file
        self.json_File=json_file
        self.set_of_names = set()
        self.groups = []
        self.features = ()
        try :
            file_c = open(csv_file, 'r')
            file_j = open(json_file, "r")
        except:
            print("At least one of the fies doesn't not exist")
        else:
            reader = csv.reader(file_c)
            self.features = tuple(next(reader))
            file_j = open(json_file, "r")
            self.json_data = json.load(file_j)
            self.group_By =self.json_data['groupby']
            file_c.close()
            file_j.close()
            self.makeGroups()


    def getGroups(self):
        return self.groups

    def makeGroups(self):
        List_csv_dict = []
        with open(self.csv_File, 'r') as file:
            csv_dict = csv.DictReader(file)
            for row in csv_dict:
                List_csv_dict.append(dict(row))
            for row in List_csv_dict :
                self.set_of_names.add(row[self.group_By])
            data_of_all_groups = Groups_By(self.set_of_names,self.group_By,List_csv_dict)
            group_columns = []
            for group_data in data_of_all_groups :
                group_columns.append(get_columns_from_group(group_data, self.features))
            list_of_results_group = []        ###
            features_dict ={}
            for feature in self.json_data['features']:
                features_dict.update(feature)
            for group in group_columns :
                result_group = Group()
                for key,value in group.items():
                    if key != self.group_By:
                        if features_dict[key]['type'] == 'categorical' :
                            value = [("NA" if v == "" else v ) for v  in value]
                            if features_dict[key]['aggregate'] ==  'mode':             #####
                                result_group.group_members.update({key:myMode(value)})
                            elif features_dict[key]['aggregate'] ==  'union':
                                set_from_value= set(value)
                                group_value = ";".join(set_from_value)
                                result_group.group_members.update({key:group_value})
                            elif features_dict[key]['aggregate'] == 'unique':
                                set_from_value = set(value)
                                result_group.group_members.update({key:len(set_from_value)})
                            elif features_dict[key]['aggregate'] == 'count':
                                result_group.group_members.update({key:len(value)})
                        elif features_dict[key]['type'] ==  'numerical' :
                            value = [(0 if v == "" else int(v) )for v in value]      ### if the value is numerical-turn it to integer
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
            list_of_results_group.sort(key=MySort)
            self.groups = list_of_results_group
            self.getSpec()
            return  list_of_results_group

    def getSpec(self):
        result = {}
        for feature in self.features :
            if feature == self.group_By:
                result.update({feature: 'group by'})
            else :
                for f in self.json_data['features']:
                    aggr = f.get(feature)
                    if aggr != None:
                        if aggr['type'] == 'textual':
                            result.update({feature: 'textual(no aggr)'})
                        else : result.update({feature:aggr['aggregate']})
        for g in self.groups:
            g.featur_aggregate_dict.update(result)
        return result

    def saveSummary(self, filename,delimiter = ','):
        if not self.groups:
            print("There is no groups in this Summary object ")
            return
        file_to_write= open(filename,"w")
        features_list = list(self.features)
        features_list.remove(self.group_By)
        file_to_write.write(self.group_By)
        file_to_write.write(delimiter)
        str1= "{}".format(delimiter) # join(self.features)
        str1 = str1.join(features_list)
        str1+="\n"
        file_to_write.write(str1)
        str2 = ""
        for group in self.groups :
            str2+=group.name


    def __getitem__(self, key):
        res = None
        gpoups_dict = {}
        for group in self.groups:
            gpoups_dict.update({group.name: group})
        for group in self.groups:
            gpoups_dict.update({group.name: group})
        if type(key) == int and -len(self.groups) <= key < len(self.groups):    ### extention
            res = self.groups[key]
        elif type(key) == str and key in self.set_of_names:
            res = gpoups_dict[key]
        return res

    def __iter__(self):
        return iter(self.groups)

    def __str__(self):
        str=""
        for group in self.groups:
            str+="{} \n".format(group)
        return str

# [{color: [red,red,blue], kilometors: [10000,15000,55000],.... }]






sum =  Summary('csvFile.csv','jsonFile.json')

# for g in sum.groups:
#     print("\n name is:  ",g.name,"\n value is : ",g.group_members)

# print("\n" , sum[-3].name ,"\n", sum[-3].group_members )
dict1= sum.getSpec()
print(dict1)
a = sum.getGroups()
print(sum)

sum.saveSummary("lala.csv")

#
# for i in a[0]:         ### to check it
#     print(i)
#
# print(a[0])





# In[ ]:
# print(data['features'][0])


# list1=[value for value in data['features'][0].values()]
# list2=[value for value in data['features']]
# keys=[]
# for i in list2 :
#     keys.append(i.keys())
# print(keys)

# print(list1[0]['type'])
# print(list1[0]['aggregate'])














