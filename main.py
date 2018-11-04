import decisiontree
import splitting_metrics





def main():
    attributes = {"growing", "cultivating", "running", "sports", "swag", "technology", "excellence"}
    categories = {
                            "BNY Mellon": {"growing":0, "cultivating":1, "running":0, "sports":1, "swag":1, "technology":0, "excellence":0},
                            "Martin Shrekli": {"growing":0, "cultivating":1, "running":0, "sports":1, "swag":1, "technology":1, "excellence":1},
                            "Mon Santo":  {"growing":1, "cultivating":0, "running":1, "sports":0, "swag":0, "technology":0, "excellence":1},
                            "Big Pharma":  {"growing":0, "cultivating":0, "running":1, "sports":0, "swag":0, "technology":1, "excellence":0},
                            "Greasy Oil":  {"growing":1, "cultivating":1, "running":1, "sports":1, "swag":1, "technology":1, "excellence":1}
                            }

    tree = decisiontree.TreeClassifier(attributes, categories, 4)
    tree.print_tree()



if __name__ == "__main__":
    main()