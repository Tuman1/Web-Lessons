# Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates


person = {'name':'Jenn', 'age': 23}

# WRONG example
# Sentence = 'My name is ' + person['name'] + ' and i am ' + str(person['age']) + ' years old.'
# print(Sentence)

# Sentence = 'My name is {} and i am {} years old.'.format(person['name'], person['age'])
# print(Sentence)

# Sentence = 'My name is {1} and i am {0} years old.'.format(person['name'], person['age'])
# print(Sentence)

# tag = "h1"
# text = "This is a headline"
#
# Sentence = '<{0}><{1}></{0}>'.format(tag, text)
# print(Sentence)

# Sentence = 'My name is {1[name]} and i am {0[age]} years old.'.format(person, person)
# print(Sentence)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('Jack', '33')
#
# Sentence = 'My name is {0.name} and i am {0.age} years old.'.format(p1)
# print(Sentence)

# Sentence = 'My name is {name} and i am {age} years old.'.format(name = "Garold", age = "33")
# print(Sentence)

#One of the most convinient way to print dictionary
# Sentence = 'My name is {name} and i am {age} years old.'.format(**person)
# print(Sentence)

#Formatting number
# for x in range(1, 11):
#     sentence = "The value is {:03}".format(x)
#     print(sentence)

# pi = 3.14159265
#
# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)

# sentence = '1 Mb is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)

import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)

# print(my_date)

# Example what we need -> March 01 2016

# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)

# Example what we need -> March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print(sentence)
