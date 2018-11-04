
# list of attribute [home, electronic, appliance, etc.] along with potential values in a hash set to linked list
# some of these quesitons will be hyper-specific to category at one point => when we'll enter a different solver
# possibly even more
# a list of NAICs codes => plan to stop at 4-digits for now


#   if node is just single then return me of potential elements
#   metric evaluate best attribute (use this metric to split the categories) create a node with the metric specified and the value
#   connect its pointers to another build-tree(node)
#   at leaf node you must make a decision


# use the highest gini index value
# https://dataaspirant.com/2017/01/30/how-decision-tree-algorithm-works/


# a map of category names to a map of attributes with values (nested dictionary)

import queue as queue
import random
import splitting_metrics


class Node(object):

    def __init__(self, val):
        self.children = []
        self.value = val

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


class TreeClassifier(object):

    def __init__(self, attribute_list, categories_tags_dict, max_depth, split_metric=splitting_metrics.even_split_metric):
        self.max_depth = max_depth
        self.attribute_set = attribute_list
        self.categories_tags = categories_tags_dict
        self.split_metric = split_metric
        self.root = self.induct_tree(self.attribute_set.copy(), self.categories_tags)
        print(split_metric)


    def induct_tree(self, attribute_list, categories_tags_dict):
        if len(categories_tags_dict.keys()) == 0:
            return Node("EMPTY")
        if len(categories_tags_dict) == 1:
            return Node(list(categories_tags_dict.keys())[0])  # make the category the root
        elif len(attribute_list) == 0 or len(self.attribute_set) - len(attribute_list) >= self.max_depth - 1:  # choose an arbitrary category
            return Node(random.choice(list(categories_tags_dict.keys())))
        else:
            right = {}
            left = {}
            new_node = Node(self.split_metric(attribute_list, categories_tags_dict, 0.5, right, left))

            list_copy = attribute_list.copy()
            # print(str(attribute_list))
            # print(str(new_node.v))
            # print(list_copy)
            list_copy.remove(new_node.value)

            new_node.children.append(self.induct_tree(list_copy, left))
            new_node.children.append(self.induct_tree(list_copy, right))
            new_node.children.append(self.induct_tree(list_copy, categories_tags_dict))

            return new_node


    def print_tree(self):
        print(self.root)







