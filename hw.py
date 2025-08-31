import random

# create three list of alphabets , numbers and symbols 
# user se input krvana ki kitne digit ka password bnvana ki kitne no. alpha and symbols chaiye 
# and password randomly print honna chayie hr baar alag 


# random_float = random.uniform(1.5, 5.5)
# print(random_float)

# random_number = random.randrange(0, 10, 2)
# print(random_number)

# rand_password = random.choices(num),random.choices(alpha),random.choices(symbol)
# print(rand_password)

num = list('0123456789')
# print(type(num))
small_alpha = list('abcdefghijklmnopqrstuvwxyz')
capital_alpha = list('ABCDEFJHIJKLMNOPQRSTUVWXYZ')
symbol = list('!@#$%^&*()-_=+[{]}|;:,.<>?/')

select_num = int(input("Enter how many numbers u wanted in ur password: "))
select_small_alpha = int(input("Enter how many small alphaets u wanted in ur password: "))
select_capital_alpha = int(input("Enter how many capital alphabets u wanted in ur password: "))
select_symbol = int(input("Enter how many symbols u wanted in ur password: "))
print("\n")
h = select_capital_alpha + select_num + select_symbol + select_small_alpha

rand_num = random.choices(num, k=select_num)
rand_capital_alpha = random.choices(capital_alpha, k=select_capital_alpha)
rand_small_alpha = random.choices(small_alpha, k=select_small_alpha)
rand_symbol = random.choices(symbol, k=select_symbol)

if h < 6:
    print("YOU HAVE TO SELECT MORE THAN 6 DIGITS !!")

elif h > 16:
    print("YOU CAN ONLY SELECT BETWEEN 6-15")

else:
    pass_list = rand_num + rand_capital_alpha + rand_symbol + rand_small_alpha
    random.shuffle(pass_list)
    final_pass = ''.join(pass_list)
    print(f"the randomly {h} digit password is: {final_pass}")