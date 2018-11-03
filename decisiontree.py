
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

class Node(object):

    def __init__(self, val):
        self.connections = {}
        self.v = val


class TreeClassifier(object):

    def __init__(self, attribute_list, categories_tags_dict, max_depth):
        self.max_depth = max_depth
        self.attribute_set = attribute_list
        self.categories_tags = categories_tags_dict
        self.root = self.induct_tree(self, self.attribute_set.copy(), self.categories_tags_dict)


    def gini_index_metric(self, attribute_list, categories_tags_dict, threshold, right, left):
        # compute the best metric
        attribute_tag_score = {}
        best_tag = None
        best_freq = None

        for tag_value_map in categories_tags_dict.values():

            distance = 0.5 *len(categories_tags_dict.keys())

            for tag in attribute_list:
                if tag_value_map[tag] > threshold:
                    if tag in tag_value_map:
                        attribute_tag_score[tag] += 1
                    else:
                        attribute_tag_score[tag] = 1


        for tag, frequency in attribute_tag_score:
            if (best_tag == None) or (abs(best_freq - distance) < abs(frequency - distance)):
                best_freq = frequency
                best_tag = tag

        for category, tag_value_map in categories_tags_dict:
            if tag_value_map[best_tag] > threshold:
                left.append({category :tag_value_map})
            else:
                right.append({category :tag_value_map})

        return Node(best_tag)

    def induct_tree(self, attribute_list, categories_tags_dict):
        if len(self.attribute_set) - len(attribute_list) >= self.max_depth:  # choose an arbitrary category
            return Node(categories_tags_dict.keys[range(len(categories_tags_dict.keys))])
        elif len(categories_tags_dict) == 1:
            return Node(categories_tags_dict.keys[0])  # make the category the root
        else:
            right, left = {}
            newNode = Node(self.gini_index_metric(self, attribute_list, categories_tags_dict, 0.5, right, left))

            attribute_list.remove(newNode.v)
            newNode.connections.add(self.induct_tree(self, attribute_list, left ))
            newNode.connections.add(self.induct_tree(self, attribute_list, right))
            newNode.connections.add(self.induct_tree(self, attribute_list, categories_tags_dict))

            return newNode

