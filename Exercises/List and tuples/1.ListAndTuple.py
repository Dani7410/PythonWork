#Create a function that takes a string as a parameter and returns a list.

#The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

#--------------------------
Str1 = 'hej med dig'
def sortcons(s):
    for i in ['a','e','i','o','u','y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)


print(sortcons("hello world"))
#--------------------------

#Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])

l = ['Claus', 'Ib', 'Per']
print(l)

#Sort this list by using the sorted() build in function.
print(sorted(l))


#Sort the list in reversed order.

print(sorted(l, reverse=True))

#Sort the list on the lenght of the name.

print(sorted(l, key=len))

#Sort the list based on the last letter in the name.


def getLastLetter(l):
    a = [x[:-1]for x in l]
    return a    
   
print(getLastLetter(l))

def reverse_list(s):
    return s[::-1]
print(sorted(l,key=reverse_list))

#print(sorted(l, reverse=True))

#Sort the list with the names where the letter ‘a’ is in the name first.

# sort a list

def a_in(x):
    if 'a' in x.lower():
        return True
    return False

print(sorted(l, key = a_in))