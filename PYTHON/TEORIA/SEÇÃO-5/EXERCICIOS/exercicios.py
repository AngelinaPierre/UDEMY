# Q1
# print('Type to numbers:')
# a = float(input())
# b = float(input())
#
# if a > b:
#     print(f'Numero a = {a} eh maior que numero b {b}')
# else:
#     print(f'Numero b = {b} é maior que numero a = {a}')

# Q2
# print('Type a number:')
# number = float(input())
#
# if number > 0:
#     sqr = pow(number,1/2)
#     print(f'sqr of number {number} = {sqr}')
# else:
#     print('Invalid number')

# Q3

# print('Type a real number:')
# r_nbm = float(input())
#
# if r_nbm > 0:
#     sqr = pow(r_nbm,1/2)
#     print(f'SQR of real number {r_nbm} = {sqr}')
# else:
#     number_two = r_nbm ** 2
#     print(f'Real number {r_nbm} ^2 = {number_two}')

# Q4

# print('Type a number:')
# number = float(input())
#
# if number > 0:
#     number_t = number ** 2
#     sqr_number = pow(number,1/2)
#     print(f'Number {number} ^2 = {number_t} | nSQR = {sqr_number}')

# Q5

# print('Type a number')
# number = int(input())
#
# if number % 2 == 0:
#     print(f'Numero {number} par')
# else:
#     print(f'Numero {number} impar')

# Q6

# print(' Type two numbers:')
# n1 = int(input())
# n2 = int(input())
#
# if n1 > n2:
#     dif = n1 - n2
#     print(f'n1 {n1} is bigger | Diference of = {dif}')
# else:
#     dif = n2-n1
#     print(f'N2 {n2} is bigger | diference = {dif}')

# Q7

# print('Type two numbers:')
# n1 = float(input())
# n2 = float(input())
#
# if n1 > n2:
#     print(f'N1 {n1} is bigger')
# elif n2 > n1:
#     print(f'N2 {n2} is bigger')
# else:
#     print('Equal numbers')

# Q8

# print('Type two grades:')
# n1 = float(input())
# n2 = float(input())

# if n1 < 0.0:
#     print('Invalid Grade')
# elif n1 > 10.0:
#     print('Invalid Grade')
# elif n2 < 0.0:
#     print('Invalid Grade')
# elif n2 > 10.0:
#     print('iNvalid grade')
# else:
#     med = (n1 + n2)/2
#     print(f'Grade = {med}')

# another way

# if n1 < 0.0 or n1 > 10.0:
#     print('Invalid Grade')
# elif n2 < 0.0 or n2 > 10.0:
#     print('Invalid Grade')
# else:
#     med = (n1 + n2)/2
#     print(f'Grade = {med}')

# Q9
# print('Type your salary and the loan installment:')
# sal = float(input())
# loan = float(input())
#
# perc_sal = sal*0.2
#
# if loan > perc_sal:
#     print('unsecured loan')
# else:
#     print('Loan Granted')


# Q10
# print('Type your hight and sex(M/W):')
# height = float(input())
# sex = input()
#
# if sex == 'M' or sex == 'm':
#     ideal_weight = (72.7 * height) - 58
#     print(f'Ideal Weight for {sex} = {ideal_weight}')
# else:
#     ideal_weight = (62.1 * height) - 44.7
#     print(f'Ideal Weight for {sex} = {ideal_weight}')

# Q11
# num = int(input('Type a number: '))
# num_str = str(num)
#
# if num < 10:
#     print('Number {} Analysis:'.format(num))
#     print(f'Unity : {num_str[0]}')
#     add = int(num_str)
#     print(f'Sum = {add}')
# elif 10 <= num <= 99:
#     print(f'Number {num} Analysis:')
#     print(f'||Unity : {num_str[1]}||')
#     print(f'||Ten : {num_str[0]}||')
#     add = int(num_str[1]) + int(num_str[0])
#     print(f'||Sum = {add}||')
# elif 100 <= num <= 999:
#     print(f'Number {num} Analysis:')
#     print(f'||Unity : {num_str[2]}||')
#     print(f'||Ten : {num_str[1]}||')
#     print(f'||hundred : {num_str[0]}||')
#     add = int(num_str[1]) + int(num_str[2]) + int(num_str[0])
#     print(f'||Sum = {add}||')
# else:
#     print(f'Number {num} Analysis:')
#     print(f'||Unity : {num_str[3]}||')
#     print(f'||Ten : {num_str[2]}||')
#     print(f'||Hundred : {num_str[1]}||')
#     print(f'||Thousand : {num_str[0]}||')
#     add = int(num_str[0]) + int(num_str[1]) + int(num_str[2]) + int(num_str[3])
#     print(f'||Sum = {add}||')

# print('Unity : {}'.format(num_str[3]))
# print('Ten : {}'.format(num_str[2]))
# print('hundred : {}'.format(num_str[1]))
# print('thousand : {}'.format(num_str[0]))


# Q12
# library for utilization of math func
# math.log(a,(base))
#log(a)/Log(base)
#log2(a)
#log10(a)
#log1p(a) _> log(1+a)

# num = int(input('Type a number:'))
# import math
# if num < 0:
#     print('Invalid Number!')
# else:
#     log_num = math.log(num)
#     print(f'NAtural logarithm of number {num} = {log_num}')

# podemos usar o log10 para computar a quanntidade de digitos em um numero.
"""
print(int(math.log10(number) + 1))
"""


# Q13

# n1 = int(input('Type first grade:'))
# n2 = int(input('Type second grade:'))
# n3 = int(input('Type third grade:'))
#
# med_pond = ((n1 * 1) + (n2 * 1) + (n3 * 2))/4
#
# if med_pond < 60:
#     print('Failed student!')
# else:
#     print(f'Avarage = {med_pond}')




# # Q14

# n1 = float(input('Type first grade:'))
# n2 = float(input('Type second grade:'))
# n3 = float(input('Type third grade:'))
#
# if 0.0 < n1 > 10.0:
#     print('Invalid grades!')
# elif 0.0 < n2 > 10.0:
#     print('Invalid grades!')
# elif 0.0 < n3 > 10.0:
#     print('Invalid grades!')
# else:
#     med_pond = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10
#     print(f'Avarage = {med_pond}')


