# _*_ coding : utf-8 _*_
# @Time : 5/19/2022 11:44 AM
# @Author : Min Li
# @File : Test7
# @Project : SeleniumProjet1

# les différents types de varibales: int,float,boolean,string,list,tuple,dictionary

print('Bonjour, tout le monde!')

weather = 'Bonjour, toute le monde!'
print(weather)

# int
money = 5000

# float
money1 = 1.2

# boolean
# sex /gender:True-M; False-F
sex = True
gender = False

# string
s = 'Bonjour'
s1 = "Bonjour"
s2 = '"Bonjour"'
s3 = "'Bonjour'"
# s4 = ""Bonjour""; s5 = ''Bonjour''; ce sont fauts.

# list
name_list = ['Bonjour','Salut']
print(name_list)

# tuple
age_tuple = (18,19,21)
print(age_tuple)

# dict
# variable = (key: valeur,key1:valeur1)
person = {'name':'James','age':18}
print(person)

# verifier le type de variable : type(variable)
print(money)
print(type(money))

print(money1)
print(type(money1))

print(sex)
print(type(sex))

print(s)
print(type(s))

print(name_list)
print(type(name_list))

print(age_tuple)
print(type(age_tuple))

print(person)
print(type(person))

# trasformer un type de variable a l autre
a = '123'
int(a)
print(int(a))
b = int(a)
print(type(b))

a1 = 1.23
print(type(a1))
b1 = int(a1)
print(type(b1))
print(b1) # valeur avant vitgule

print('------------------------')
a2 = True # true = 1, false=0
print(type(a2))
b2 = int(a2)
print(b2)
print(type(b2))

# 12.23, 12b , ne peuvent pas etre transforme a int

print('--------------------')
a3 = True
print(type(a3))
b3 = str(a3)
print(b3)
print(type(b3))

print('-----------------')

# un variable <>0---> True   0 = false   0.0 = false  string variable< a un contenu--->ture, si vide--->false
a4 = 2
b4 = bool(a4)
print(b4)
print(type(b4))
print('----------------------')

a5 = 'Bonjour'
b5 = bool(a5)
print(b5)
print(type(b5))
print('-----------------------')

a6 = ''
b6 = bool(a6)
print(b6)
print(type(b6))