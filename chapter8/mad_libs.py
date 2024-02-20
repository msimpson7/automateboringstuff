import re
# This program will create a mad libs comic for fun


# get the file and create the list of data to ask for
def get_info(input_data):
    ml_result = []
    ml_regex = re.compile(r'([A-Z]{2,})')
    for line in input_data:
        ml_result += ml_regex.findall(line)
    return ml_result


# request from the user the different requests for the different parts of the sentence
def get_words(pos):
    replacement_words = []
    for word in pos:
        article = 'an' if word[0] in ['A','E','I','O','U'] else 'a'
        replacement_words.append(input(f'Enter {article} {word.lower()}: '))
    return replacement_words


# replace the parts of speech with the words from the user and print
def print_result(input_data, replacement_words):
    result = ''
    for line in input_data:
        result += line
    ml_regex = re.compile(r'([A-Z]{2,})')
    for i in range(len(replacement_words)):
        se_result = ml_regex.search(result)
        result = result.replace(se_result[0], replacement_words[i], 1)
    print(f'The resulting phrase is:\n{result}')


input_file = "mad_libs\\test1.txt"
with open(input_file, 'r') as my_file:
    file_info = my_file.readlines()

listing = get_info(file_info)
input_words = get_words(listing)
print_result(file_info, input_words)
