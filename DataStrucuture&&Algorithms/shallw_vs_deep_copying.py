import copy

# there are 3 ways to copy
# first way - alias
def alias_copy():

    origin_list = [2, 3, 4]
    new_list = origin_list

    print(origin_list is new_list)
    #both identifiers reference to the list
    # new_list.pop();
    # for i in origin_list:
    #     print(i)

#second way - shallow copy
def shallow_copy():
    origin_list = [[1, 2], 3, 4]
    new_list = list(origin_list)

    print(origin_list is new_list)

    # new_list.pop()
    #avoid to manipulate the same list

    # the object instance inside the list still can be changed since they hold the same
    # new_list[0].append(3)

    # for i in origin_list:
    #     print(i)
    #
    # print(new_list[0] is origin_list[0])
def deep_copy():
    origin_list = [[1, 2], 3, 4]
    new_list = copy.deepcopy(origin_list)
    # new_list[0].append(3)
    #
    # for i in origin_list:
    #     print(i)
    print(new_list[0] is origin_list[0])

# key is different reference
if __name__ == '__main__':
    alias_copy()
    # shallow_copy()
    # deep_copy()


