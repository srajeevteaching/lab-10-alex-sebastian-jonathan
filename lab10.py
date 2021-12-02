# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: December 2nd, 2021
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs:

def load_morse_dictionary(data_file):
    key_value_file = open(data_file)
    list_of_keys = []
    list_of_values = []
    for line in key_value_file:
        line_entry = line.strip().split("	")
        # print(line_entry, end="")
        list_of_keys.append(line_entry[1])
        list_of_values.append(line_entry[0])
    key_value_file.close()
    # print(list_of_keys)
    # print(list_of_values)
    dictionary = {list_of_keys[i]: list_of_values[i] for i in range(len(list_of_keys))}
    return dictionary


# def decode_file(dictionary, filename):
#     listed_morse_code = []
#     coded_file = open(filename)
#     for line in coded_file:
#         line_entry = line.split()
#         listed_morse_code.extend(line_entry)


morse_dictionary = load_morse_dictionary("morsecode.txt")
listed_morse_code = []
listed_morse_decode = []
coded_file = open("morse1.txt")
for line in coded_file:
    line_entry = line.split()
    listed_morse_code.extend(line_entry)

print(listed_morse_code)
print(listed_morse_decode)
