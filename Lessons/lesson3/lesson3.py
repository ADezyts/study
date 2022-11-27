# list_of_users = {
#     'Nick' : {
#         'email': 'Nick@mail.com',
#         'password': '1111'
#     },
#     'Anna' : {
#         'email': 'Anna@mail.com',
#         'password': '1111'
#     },
#     'Tanya' : {
#         'email': 'Tanya@mail.com',
#         'password': '1111'
#     },
# }

# # print(f"{list_of_users['Tanya']}") - первый вариант решения

# for key in list_of_users :
#     if key == 'Tanya' :
#         print(list_of_users['Tanya']) - второй вариант решения






# first_number = int(input('Введите число 1: '))
# second_number = int(input('Введите число 2: '))

# for i in (first_number, second_number):
#     if i % 2 == 0:
#         key = i
#         value = i ** 2
#         x = {key: value}
#         print(x)


# from random import randint
# # x = randint(0, 99)

# N = 10
# a = []

# # 1 step - random number generator

# for i in range (N):
#     a.append(randint(1, 99))
# print(a)


# # 2 step - sorting

# # for i in range(N-1):
# #     for j in range(N-i-1):
# #         if a[j] > a[j+1]:
# #             a[j], a[j+1] = a[j+1], a[j]

# # print('sorted' + str(a))




# # 2 alternative step - sorting

# i = 0
# while i < N - 1:
#     j = 0
#     while j < N - 1 -i:
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#         j += 1
#     i += 1
# print('sorted by while' + str(a))




# ----------------------
# Functions
# -----------------------

def sum(a,b,c):
    return a ** b * c
print (sum(1,3,2))





