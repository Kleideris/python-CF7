from collections import Counter

def count_with_dict_comprehension(my_list):
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print(frequency_dict)  # giati ta bgazei me diaforetikh seira TODO na to psaksw.

def count_with_manual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict.keys():  # vazw to .keys() parolo pou den xreiazetai giati einai pio readable
            frequency_dict[item] += 1  # an den eixa to else ti tha ekane update? tha petage error TODO na to dw
        else:
            frequency_dict[item] = 1
    print(frequency_dict)

                                                # for item in range(my_list):
                                                #     frequency_dict[f"{my_list[item]}"] = 1
                                                #     if frequency_dict[f"{my_list[item]}"] == my_list[item]:
                                                #         frequency_dict[f"{my_list[item]}"] += 1  TODO na tsekarw an douleyei
def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    print(frequency_dict)

def count_with_counter(my_list):
    frequency_list = Counter(my_list)
    sorted_freq_dict = frequency_list.most_common()
    print(sorted_freq_dict)  #TODO na dw pws na ta kanw dict eukola

def main():
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    count_with_dict_comprehension(my_list)
    count_with_manual_loop(my_list)
    count_with_get_method(my_list)
    count_with_counter(my_list)

if __name__ == "__main__":
    main()    