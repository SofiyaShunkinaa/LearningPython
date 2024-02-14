# string = " СТРОКА ШАЛАШ   КАПИТАН АННА  ПАСПОРТ ОБЛАКО "
#
# start = ""
# end = ""
# count = 0
#
# for i in range(0, len(string)):
#     if i < len(string)-1:
#         if string[i] == " " and string[i + 1] != " ":
#             start = string[i + 1]
#         if string[i] != " " and string[i + 1] == " ":
#             end = string[i]
#     if start == end and string[i] != " ":
#         count = count + 1
# print(count)


# string = " СТРОКА ШАЛАШ   КАПИТАН АННА  ПСПОРТ ОБЛАКО "
#
# start = ""
# end = ""
# count = 0
# word = ""
#
# for i in range(0, len(string)):
#
#     if i > 0:
#
#         if string[i] != " ":
#             word += string[i]
#
#         if string[i] == " " and string[i-1] != " ":
#             if "А" in word:
#                 count = count + 1
#             print(word)
#             word = ""
#
# print(count)


# string = " СТРОКА ШАЛАШ   КАПИТАН АННА  ПСПОРТ ОБЛАКО "
#
# length = 0
# word = ""
#
# for i in range(0, len(string)):
#
#     if i > 0:
#
#         if string[i] != " ":
#             word += string[i]
#
#         if string[i] == " " and string[i-1] != " ":
#             if length == 0:
#                 length = len(word)
#             if length > len(word):
#                 length = len(word)
#             print(word)
#             word = ""
#
# print(length)

# string = "Программа"
# second_part = ''
# new_string = ""
# for i in range(1,(len(string))+1):
#     if i % 2 == 0:
#         new_string += string[i-1]
#     else:
#         second_part += string[i-1]
# for i in range(len(second_part)-1,-1,-1):
#     new_string += second_part[i]
#
# print(new_string)

# string = " СТРОКА ШАЛАШ   КАПИТАН АННА  ПСПОРТ ОБЛАКО "
#
# word = ""
# new_string = ''
# result =""
# for i in range(0, len(string)):
#
#     if string[i] != " ":
#         word += string[i]
#
#     if string[i] == " " and string[i - 1] != " ":
#         new_string += word + "."
#         word = ""
# for i in range(len(new_string)-1):
#     result+=new_string[i]
#
# print(result)

# import os
# path = os.path.abspath('1.py ')
# print(path)
#
# pos_start = path.rfind('\\')
# pos_end = path.rfind('.')
# name = ''
#
# for i in range(pos_start+1, pos_end):
#     name += path[i]
# print(name)

# string = "hello world! This is my not first Python program. It is third lab"
# symbol = string[0]
# new_string = symbol
# new_string += string[1:].replace(symbol,'$')
# print(new_string)

# string = input("Enter some text: ")
# # string[::-1] can be used for string inverting
# new_string = string
# if len(string) > 3:
#     if string[-3:] == 'ing':
#         new_string += 'ly'
#     else:
#         new_string += 'ing'
# print(new_string)



