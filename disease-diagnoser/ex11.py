import itertools
class Node:
    '''a class that makes the object Node object with its attributes:
    data is a symptom or disease
    positive_child is a positive answer
    negative_child is a negative answer'''
    def __init__(self, data, pos=None, neg=None):
        '''this metod is the cunstructor of the class Node'''
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def is_leaf(self):
        '''this method checks if the node given is a leaf'''
        if self.positive_child == None and self.negative_child == None:
            return True
        return False


class Record:
    '''a class that makes the object Record with its attributes:
    illness and the symptoms that diagnose the illness'''
    def __init__(self, illness, symptoms):
        '''this function is the cunstructor of the class Record'''
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    '''this function opens a txt file, every line in the file is a new object of class Record
    which has an illness and symptoms and returns alist of objects'''
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    '''a class that makes the object of the tree with its attributes:
    the root if the tree from where we start the diagnose'''
    def __init__(self, root):
        '''this method is the cunstructor of the class Diagnoser'''
        self.root = root

    def diagnose(self, symptoms):
        '''this method recieves a list of symptoms and returns the illness that fits
        acoording to the symptoms given'''
        return self.diagnose_helper(self.root, symptoms)

    def diagnose_helper(self, root, symptoms):
        '''this method checks if the symptom in the root is in the list given if true
        moves to the positive child of the root if not moves to the negative child
        until it reaches to a leaf and returns the illness'''
        if root.positive_child is None and root.negative_child is None:
            return root.data
        if root.data in symptoms:
            root = root.positive_child
            return self.diagnose_helper(root, symptoms)
        else:
            root = root.negative_child
            return self.diagnose_helper(root, symptoms)

    def calculate_success_rate(self, records):
        '''this method returns the success rate according to the number of times we found
        the correct illness divided by the number of illness we are given'''
        counter = 0
        for record in records:
            result = self.diagnose(record.symptoms)
            if result == record.illness:
                counter += 1
        success_rate = float(counter) / float(len(records))
        return success_rate

    def all_illnesses(self):
        '''this method returns a list of all the illness on the leafs of the tree'''
        lst = []
        illnesses = dict()
        dictionary = self.all_illnesses_helper(self.root, illnesses)
        while len(dictionary) != 0: #makes a list sorted as the most common illness in the start of the lst
            highest_illness_count = max((illnesses.values()))
            for illness in dictionary:
                if dictionary[illness]==highest_illness_count:
                    lst.append(illness)
                    del dictionary[illness]
                    break
        return lst

    def all_illnesses_helper(self, root, illnesses):
        '''this method moves down the tree and checks if the root is a leaf if true
        adds it to a dictionary and returns the dictionary'''
        if root.is_leaf():
            if root.data not in illnesses:
                illnesses[root.data] = 0
            if root.data in illnesses:
                illnesses[root.data] += 1 #a dictionary of every illness with the number of times it appears
            return illnesses
        else:
            self.all_illnesses_helper(root.positive_child, illnesses)
            self.all_illnesses_helper(root.negative_child, illnesses)
        return illnesses

    def most_rare_illness(self, records):
        '''this method recieves a list of objects each has an illness and symptoms
        and finds the illness that we found lesser times when we run the tree
        if there is an illness that is not found by ruuning the tree that it is the
        most rare illness'''
        illnesses = dict()
        all_illnesses = self.all_illnesses()
        for record in records:
            result = self.diagnose(record.symptoms)
            if result not in illnesses:
                illnesses[result] = 0
            if result in illnesses:
                illnesses[result] += 1
        for i in all_illnesses:
            if i not in illnesses:
                return i
        rarest_illness_count = min((illnesses.values()))
        for illness in illnesses:
            if illnesses[illness]==rarest_illness_count:
                return illness

    def paths_to_illness(self, illness):
        '''this method returns a list of paths to get to a given illness'''
        return self.paths_to_illness_helper(self.root,illness,[],[])

    def paths_to_illness_helper(self,root, illness,lst,temp_lst):
        '''this method recieves a root to start the run on the tree, an illness
        and 2 empty lists, runs on all the paths on the tree and if the path leads
        to the given illness it appends it to the lst and returns the lst'''
        if root.is_leaf():
            if root.data == illness:
                lst.append(temp_lst)
            return lst
        else:
            temp_lst = temp_lst[:]
            temp_lst.append(True)
            self.paths_to_illness_helper(root.positive_child, illness,lst,temp_lst)
            temp_lst = temp_lst[:]
            temp_lst.pop()
            temp_lst = temp_lst[:]
            temp_lst.append(False)
            self.paths_to_illness_helper(root.negative_child, illness,lst,temp_lst)
        return lst

def build_tree(records, symptoms):
    '''this function builds a tree that every root is a symptom and a leaf is an illness'''
    root = Node(symptoms[0],None,None)
    build_tree_symptoms_hepler(root, symptoms,1)
    build_tree_illnesses(root,records,symptoms)
    return root

def build_tree_symptoms_hepler(root, symptoms, pointer):
    '''this function returns a tree with all the symptoms given'''
    if pointer == len(symptoms):
        return
    if root.is_leaf():
        root.positive_child = Node(symptoms[pointer])
        root.negative_child = Node(symptoms[pointer])
    else:
        build_tree_symptoms_hepler(root.positive_child, symptoms, pointer + 1)
        build_tree_symptoms_hepler(root.negative_child, symptoms, pointer + 1)

def build_tree_illnesses(root,records,symptoms):
    '''this function runs on all the records and calls the helper function'''
    sorted_lst = sort_records(records)
    for record in sorted_lst:
        build_tree_illnesses_helper(root,record,symptoms)

def sort_records(records):
    '''this function sorts the list given and if the some records have the same symptoms it puts at first
    the record with the illness that is most common'''
    sorted_lst = []
    dictionary = dict()
    for record in records:
        dictionary[record] = 0
    for record1 in records:
        for record2 in records:
            if record1.illness == record2.illness and record1.symptoms == record2.symptoms:
                dictionary[record1] += 1
    dictionary = sorted(dictionary.items(), key = lambda x:x[1])
    for root in dictionary:
        sorted_lst.append(root[0])
    return sorted_lst[::-1]

def build_tree_illnesses_helper(root,record,symptoms):
    '''this function recieves a record and makes a leaf of the illness inside the record
    in the place where every symptom in the record answered true and all the other
    symptoms answered false'''
    if root:
        if root.data == symptoms[len(symptoms)-1]:
            if root.data in record.symptoms and root.positive_child is None:
                root.positive_child = Node(record.illness)
                return
        if root.data == symptoms[len(symptoms)-1]:
            if root.data not in record.symptoms and root.negative_child is None:
                root.negative_child = Node(record.illness)
                return
        if root.data in record.symptoms:
            build_tree_illnesses_helper(root.positive_child,record,symptoms)
        if root.data not in record.symptoms:
            build_tree_illnesses_helper(root.negative_child, record,symptoms)

def optimal_tree(records, symptoms, depth):
    '''this function returns the root of the tree with the combination of symptoms
    with the highest rate of success'''
    dictionary = {}
    organized_combinations = []
    all_combinations = itertools.combinations(symptoms,depth)
    for combination in all_combinations:
        organized_combinations.append(list(combination))
    for combination in organized_combinations:
        root = build_tree(records, combination)
        diagnoser = Diagnoser(root)
        rate = diagnoser.calculate_success_rate(records)
        dictionary[root] = rate
    highest_rate_count = max((dictionary.values()))
    for key in dictionary:
        if dictionary[key]==highest_rate_count:
           return key
