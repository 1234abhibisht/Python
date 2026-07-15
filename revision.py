from collections import defaultdict
# different factory functions
dd_int = defaultdict(int)        # Default value: 0
dd_list = defaultdict(list)      # Default value: []
dd_set = defaultdict(set)        # Default value: set()
dd_str = defaultdict(str)        # Default value: ''
dd_dict = defaultdict(dict)      # Default value: {}
dd_bool = defaultdict(bool)      # Default value: False
# creating a default dictionary
def_dic1 = defaultdict(int)
def_dic1['a'] = 1
def_dic1['b'] = 2
print(def_dic1['a'])  # -> 1
print(def_dic1['c'])  # -> 0, as key 'c' is not present in def_dic1 default dictionary, instead of raising error it will return a default value of integer which is 0
def_dict2 = defaultdict(list)
def_dict2["key"]
print(def_dict2["key"])