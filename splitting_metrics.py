def even_split_metric(attribute_list, categories_tags_dict, threshold, right, left):
    # compute the best metric
    tag_frequencies = {}  # map frequencies of tags
    best_tag = None
    best_freq = None
    distance = 0.5 * len(categories_tags_dict.keys())

    for tag_value_map in categories_tags_dict.values():  # list of all attributes and values
        for tag in attribute_list:  # iterate over all viable splitting attributes
            if tag_value_map[tag] > threshold:
                if tag in tag_frequencies:
                    tag_frequencies[tag] += 1
                else:
                    tag_frequencies[tag] = 1

    for tag, frequency in tag_frequencies.items():
        if (best_tag == None) or (abs(best_freq - distance) > abs(frequency - distance)):  # best splitter
            best_freq = frequency
            best_tag = tag

    for category, tag_value_map in categories_tags_dict.items():
        if tag_value_map[best_tag] > threshold:
            left[category] = tag_value_map
        else:
            right[category] = tag_value_map

    return best_tag