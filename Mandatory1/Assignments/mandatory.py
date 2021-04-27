def sets1():
    print("-----------------------------------------------FIRST EXERCISE-----------------------------------------------")
    directors = set(["Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Soren"])
    management = set(["Tine", "Trunte", "Rane"])
    employees = set(["Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James"])
    print("In The Board of Directors but Not an Employee: ")
    print(directors.difference(employees))
    print("In the board of  directors and also an employee: ")
    print(directors.intersection(employees))
    print("In The management and also a member of the board of directors: ")
    print(management.intersection(directors))
    print("All memeber of the management also an employee ? : ")
    print(management.issubset(employees))
    print("All members of the management also in the board of directors? : ")
    print(management.issubset(directors))
    print("An Employee, member of the management and a member of the board of directors: ")
    res = set.intersection(directors, management, employees)
    print(res)
    print("Employee neither a member on the board or management: ")
    print(employees-directors-management)

def sets2():
    print("-----------------------------------------------SECOND EXERCISE-----------------------------------------------")
    dict = {'a':'Alpha', 'b':'Beta', 'g':'Gamma'}
    listOfTuples = [(initial, greek) for initial, greek in dict.items()]
    print(listOfTuples)
    return(listOfTuples)

def sets3():
    print("-----------------------------------------------THIRD EXERCISE-----------------------------------------------")
    set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
    set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}
    
    print("Union:")
    union = set1.union(set2)
    print(union)

    print("Symetric Diff:")
    symdiff = set1.symmetric_difference(set2)
    print(symdiff)

    print("Difference")
    diff = set1.difference(set2)
    print(diff)

    print("Disjoint")
    dis = set1.intersection(set2)
    print(dis)

def sets4(date):
    print("-----------------------------------------------FOURTH EXERCISE-----------------------------------------------")
    monthDict = {'JAN' : '01', 'FEB' : '02', 'MAR' : '03', 'APR' : '04', 'MAY' : '05', 'JUN' : '06', 'JUL' : '07', 'AUG' : '08', 'SEP' : '09', 'OCT' : '10', 'NOV' : '11', 'DEC' : '12'}
    splited = date.split('-')
    day = splited[0]
    month = splited[1]
    year = splited[2]
    
    newMonth = monthDict[month]

    def yearToNewYear(year):
        if int(year) > 21:
            nYear = "19" + year
            return nYear
        else:
            nYear = "20" + year
            return nYear

    newYear = yearToNewYear(year)

    

    tuple = (newYear, newMonth, day)
    return tuple


    







sets1()
sets2()
sets3()
print(sets4("8-MAR-85"))

