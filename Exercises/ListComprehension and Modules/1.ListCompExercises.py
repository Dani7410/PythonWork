#Create a list of capital letters in the english alphabet
#--
alphabet = [chr(x) for x in range(65,91)]
print(alphabet)


print("-------------------")


#Create a list of capital letter from the english aplhabet,
#  but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
#--
CapitalL = [chr(x) for x in range(65,91) if x not in range(70,75,80)]
print(CapitalL)

print("----------------------")

#Create a list of capital letter from from the english aplhabet,
#  but exclude every second between F & O
#--
CapitalF = [chr(x) for x in range(65,91) if x not in range(70,80,2)]
print(CapitalF)