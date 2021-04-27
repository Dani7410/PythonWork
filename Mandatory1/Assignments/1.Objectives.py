#1. Model 
#an organisation of employees, management and board of directors in 3 sets.
#Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

#Management: Tine, Trunte, Rane

#Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

#who in the board of directors is not an employee?
#who in the board of directors is also an employee?
#how many of the management is also member of the board?
#All members of the managent also an employee
#All members of the management also in the board?
#Who is an employee, member of the management, and a member of the board?
#Who of the employee is neither a memeber or the board or management?
#-----------------------------------------------------------------------------
#Code
bod = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels","Anna","Tine", "Ole","Trunte","Bent","Rane", "Allan","Stine","Clause","James","Lars"}


print(bod)
print(management)
print(employees)
print("")
a = bod.difference(employees)
b = management.intersection(bod)
c = bod.intersection(employees)
d = management.intersection(employees)
e = management.intersection(bod)
f = set.intersection(bod, management, employees)
g = employees.difference(bod,management)


print("These are not employees: ", a)
print("These are also employees: " , b)
print("There are this many from the management in the board: ", len(c))
print("all members of the management that are also and employee: ",d)
print("all members of the management that are also in the board: ",e)
print("These are members of all ranks",f)
print("employees who's neither board or management: ",g)

print("")






#-----------------------------------------------------------------------------
#2. Using a list comprehension create a list of tuples from the folowing datastructure
#{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
#-----------------------------------------------------------------------------
#Code
print("------List and Tuples---------")

firstDict = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

tuplesList = [(k,v) for k,v in firstDict.items()]

print(tuplesList)

print("")

#-----------------------------------------------------------------------------
#3. From these 2 sets:
#{'a', 'e', 'i', 'o', 'u', 'y'}

#{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
#-----------------------------------------------------------------------------
 #code

setOne = {'a', 'e', 'i', 'o', 'u', 'y'}

setTwo = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}



#-----------------------------------------------------------------------------
print("")



#Of the 2 sets create a:

#Union:
#----
print("-------------Union-----------")
UnionOne = setOne.union(setTwo)
print(UnionOne)
print("")

#Symmetric difference
#----
print("----------Symmetric difference---------------")
print(setOne^setTwo)
print(setTwo^setOne)
print("")

#difference
#----
print("------------Difference-----------------------")
print(setOne.difference(setTwo))
#Doestn print the difference between these two list in the first, because a set (setOne) doesnt have a 
print(setTwo.difference(setOne))
print("")
#disjoint
#----
print("-------------disjoin--------------------")
print(setOne.isdisjoint(setTwo))
print(setTwo.isdisjoint(setTwo))
#Is not disjoint because bot sets have elements in common

print("")

print("-----------Date decoder-------------")
# 4. Date Decoder

#A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

#Create a dict suitable for decoding month names to numbers.
month = {1 : 'JAN', 2 : 'FEB', 3 : 'MAR', 4 : 'APR', 5 : 'MAY', 6 : 'JUN', 7 : 'JUL', 8 : 'AUG', 9 : 'SEP', 10 : 'OKT', 11 : 'NOV', 12 : 'DEC' }
month = {'JAN' : 1, 'FEB' : 2, 'MAR':3, 'APR' : 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP' : 9, 'OKT': 10, 'NOV' : 11, 'DEC' : 12 }

#Create a function which uses string operations to split the date into 3 items using the "-" character.

s = "8-MAR-85"
print(s.split('-'))

def my_split_function(s):
    return s.split('-')

print(my_split_function("01-02-20"))

def translateMonth(s):
    i = month.get(s)
    return i

#Translate the month, correct the year to include all of the digits.

def correct_the_year(i):
    if i<=21 and i>=00:
        i += 2000
    else :
        i += 1900
    return i


print(correct_the_year(19))
print(correct_the_year(85))

#The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d )

def date_function(s):
    a = my_split_function(s)
    b = translateMonth(a[1])
    c = correct_the_year(int(a[2]))
    return (str(c) + str(b) + a[0])

print(date_function("01-FEB-20"))
