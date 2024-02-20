
# This will return a comma-separated list in a string with 'and' before the last item

def separate_comma(my_list):
    str = ''
    for i in range(len(my_list)-1):
        str += my_list[i] + ', '
    str += 'and ' + my_list[len(my_list)-1]
    return str


alist = ['cat', 'dog', 'monkey', 'rabbit']
print(separate_comma(alist))
