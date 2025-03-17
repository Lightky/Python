# f strings
# user_name = 'Light'
# user_age = 24
# user_information = f'{user_name} is{user_age}  years old'
# bad_appraoch = user_name + ' is ' + str(user_age) + ' years old ' # bad approach
# print(bad_appraoch)


# Single Line if Statements

# user_name = 'Kira'
# user_age = 18
# user_status = 'Adult' if user_age >= 18 else 'Child'
# if user_age < 20:
#     user_status = 'Child'
# else:
#     user_status = 'Adult'
# print(f'{user_name} is a {user_age} year old. The person is a {'adult' if user_age >= 18 else 'child'}')

# List Comprehension
# simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a', 'b', 'c') if j == 'a']
# for i in range(0,11,1):
#     simple_list.append(i)
# print(simple_list)


# Lambda Functions
# def double_value(num):
#     return num * 2
# double_value = lambda num: num * 2
# print(double_value(23))

# Some Functions want a function as an argument
# ramdom_list = [('Ryuk', 500), ('Light', 25), ('Misa', 23)]
# sorted_list = sorted(ramdom_list, key = lambda user_tuple : user_tuple[1])
# print(sorted_list)

# Exercise 

# battleship_board = [f'{letter}{num}' for letter in ('A', 'B', 'C', 'D', 'E') for num in range(1,6) if f'{letter}{num}' != 'C3']
# print(battleship_board)