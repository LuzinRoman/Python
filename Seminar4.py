# Задача №25. Решение в группах Напишите программу, 
# которая принимает на вход строку, и отслеживает, сколько раз 
# каждый символ уже встречался. Количество повторов добавляется к символам с 
# помощью постфикса формата _n.
#  Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

# str = "a a a b c a a d c d d"
# my_list = str.split()
# letters = list()
# for i in range(len(my_list)):
#     if my_list[i] not in letters:
#         letters.append(my_list[i])
#     else:
#         letters.append(my_list[i])
#         my_list[i] += f"_{letters.count(my_list[i])-1}"
# print(" ".join(my_list))

# Задача №27. Решение в группах Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько 
# различных слов содержится в этом тексте. Input: She sells sea shells on the 
# ea shore The shells that she sells are sea shells I'm sure.So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea shore shells 
# Output: 13
user_input = "She sells sea shells on the sea shore The shells \
that she sells are sea shells I'm sure. So if she sells sea \
shells on the sea shore I'm sure that the shells are sea \
shore shells"
# example output: 19

list_input = user_input.split()

for i in range(len(list_input)):
    list_input[i] = list_input[i].lower()
    if list_input[i][-1] in [".", ",", "!", "?"]:
        list_input[i] = list_input[i][:len(list_input[i]) - 1]

unique_words = set(list_input)
print(len(unique_words))
