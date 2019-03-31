# """
 
#    ______   _______ _   _  ___  _   _ 
#   |  _ \ \ / /_   _| | | |/ _ \| \ | |
#   | |_) \ V /  | | | |_| | | | |  \| |
#   |  __/ | |   | | |  _  | |_| | |\  | 
#   |_|    |_|   |_| |_| |_|\___/|_| \_|
                                      
 
# """

# # for letter in "hello":
# #     print(letter)

# # for letter in "hello":
# #     print(letter*5)

# for i in range(1,20):
#     print(i+ 1)

# for i in range(1,10,2):
#     print(i) 

# tab= ["Salut", "aziz", "sana", "adam"]
# for i in tab:
#     print(i)

# letter = "hello World"
# # imprimer plusieur =s fois la phrase
# for i in range(5):
#     print(letter)

# nbreDeFois = input(" entrer un chiffre : \n ")
# mot = input("ecrire un mot\t")
# nbr = int(nbreDeFois)

# for i in range(nbr):
#     # print(mot)
#     # print(f"le nombre de fois est de {nbr}: le mot est {mot} ")
#     print(f"le nombre de fois est de {i+1}: le mot est {mot} ")

# # Exo pair et impair



# import random
# nbr=random.randrange(1,20)
# print(nbr)


# for num in range(1,11):
#     if(num == 9):
#         print(f"{num} => est success ......ooooooooooooooooooooo.....")
#     elif(num == 7 or num ==3):
#         print(f"{num} => est ODD .........xxxxxxxxxxxxxxxxxxxxxx....")
#     elif(num%2 == 0):
#         print(f"{num} => est pair")
#     else:
#         print(f"{num} => est impair")


# for num in range(1,11):
#     if num == 9:
#         state= "Success"
#     elif num == 7 or num == 3:
#         state = "ODD"
#     elif num % 2 == 0:
#         state = "pair"
#     else:
#         state="impair"
#     print(f" {num} est {state}")


# for num in range(1, 11):
#     count= 1
#     smiley= ""
#     while count<=num:
#         smiley += "\U0001f600"
#         count +=1
#     # print(f" {smiley}\n {count}\r {num}\r")
#     print(f" {smiley}")

# motDePass = "123"
# print("""le mot de pass est : 123 \n
#     ecrit ton chiffre *** pour deverouilliez    
#     """)
# hackMotPass = input("entrer le mot hacker: \n")
# while hackMotPass != motDePass:
#     print("Wrong")
#     hackMotPass = input("entrer le mot hacker: \n")
#     o = str(hackMotPass)
#     if o !=motDePass:
#         print("Wrong")
#     else:
#         print("Unlocked Great")
# print("\U0001f600"*3)


# times = 1
# espace = 11
# while times < 11:
#     x = "\t"
#     espace-=1
#     print(f"{x* espace}\U0001f600"* times)
#     times+=1


# x = int(input("tape ton chiffre: \n"))
# num = 3
# while x != num:
#     print("wrong")
#     x = int(input("tape ton chiffre: \n"))
#     # print(num)
#     if x == num:
#         break
#     else:
#         print("ressayer")

# print("yes")


# # // retrouver un numero 
# import random
# x = random.randrange(1,10)
# while True:
#     v = int(input("entrer un chiffre :\n"))
#     print(f"le chiffre a trouver est : \t ....=> {x}")
#     if  x == v:
#         print("tu as trouvé le bon numero")
#         y= input("Souhaites tu recommencer : (y/n)\n")
#         if y == "y":
#             x = random.randrange(1,10)
#         else:
#             break;
#     elif v > x:
#         print("PLUS PETIT")
#     else:
#         print("PLUS GRAND")
    
# print("End game...")



# import random
# x = random.randrange(1,10)
# essai = 1
# # game= True

# while True:
#     print(essai)
#     v = int(input("entrer un chiffre :\n"))
#     print(f"le chiffre a trouver est : \t ....=> {x}")
#     if (x == v or essai == 3):
#         if essai == 3:
#             print("trois chance echouer")
#         y= input("Souhaites tu recommencer : (y/n)\n").lower()
#         if y== "no" or y=="n":
#             break 
#         else:
#             x = random.randrange(1,10)
#             essai=1
#     elif v > x:
#         essai += 1
#         print(f"essai est de :=>  {essai}")
#         print("PLUS PETIT")
#     else:
#         essai += 1
#         print(f"essai est de :=>  {essai}")
#         print("PLUS GRAND") 
# print("End game...")



# tab= list(range(1,6))
# # [1, 2, 3, 4, 5]
# print(tab)
# print(len(tab))#5
# print(tab[1])
# print(tab[-1])

# x= tab[1]
# print(x in tab)#true

# if 1 in tab:
#     print("yes")#yes

# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# for name in people:
#     print(name)

# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# index= 0

# while index < len(people):
#     # print(people[index])
#     print(f"index : {index } => valeur: { people[index]}")
#     index+=1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
#     print(result)
# # super
# # supercali
# # supercalifragil
# # supercalifragilistic
# # supercalifragilisticexpi
# # supercalifragilisticexpiali
# # supercalifragilisticexpialidocious
# result = result.upper()
# print(result)#SUPERCALIFRAGILISTICEXPIALIDOCIOUS




# mu= [1, 2, 3, 4, 5]
# for number in mu:
#     print(number*2)


# mu= [1, 2, 3, 4, 5]
# i= 0

# while i < len(mu):
#     print(mu[i])
#     i+=1

# numb=[1,6,7,1,99]
# numb.append(5)
# print(numb)
# numb.extend([3,4,12,11,10,9,7])#[1, 6, 7, 1, 99, 5, 3, 4, 12, 11, 10, 9, 7]
# print(numb)
# numb.insert(2,3333)#[1, 6, 3333, 7, 1, 99, 5, 3, 4, 12, 11, 10, 9, 7]
# print(numb)
# numb.insert(len(numb),55555)#[1, 6, 3333, 7, 1, 99, 5, 3, 4, 12, 11, 10, 9, 7, 55555]
# print(numb)
# numb.clear()
# print(numb)#[]
# numb=[3,4,12,11,10,9,7,3,11,15,14]
# numb.pop(0)
# print(numb)#[4, 12, 11, 10, 9, 7] plus de 3
# numb.remove(4)
# print(numb)#[12, 11, 10, 9, 7]plus le chiffre 4

# print(numb.index(10))#3
# print(numb.index(11, 2))#4
# print(numb.count(11))# apparait deux fois
# print(numb.reverse())#[14, 15, 11, 3, 7, 9, 10, 11, 12, 4, 3]
# print(numb)#[14, 15, 11, 3, 7, 9, 10, 11, 12, 4, 3]
# numb.sort()#
# print(numb)#[3, 3, 4, 7, 9, 10, 11, 11, 12, 14, 15]

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# print(''.join(sounds))#supercalifragilisticexpialidocious
# print('/'.join(sounds))#super/cali/fragil/istic/expi/ali/docious

#   #   0  1  2  3  4  5  6  7  8  9   10  11
# nb = [3, 3, 4, 7, 9, 10, 11, 11, 12, 14, 15]
# #   -11 -10 -9 -8 -7 -6  -5  -4  -3  -2  -1

# print(nb[4:])#[9, 10, 11, 11, 12, 14, 15]
# print(nb[4:-1])#[9, 10, 11, 11, 12, 14]
# print(nb[4:8])#[9, 10, 11, 11]
# print(nb[-4:])#[11, 12, 14, 15]
# print(nb[-4:-3])#[11]
# print(nb[-4:8])#[11]
# print(nb[:-9])#[3, 3]
# print(nb[:-11])#[]
# print(nb[2::2])#[ 4, 9, 11, 12, 15]
# print(nb[::2])#[3, 4, 9, 11, 12, 15]


# n= [1,2,3,4,5,6]
# print(n[1::-1])#[2, 1]
# print(n[:1:-1])#[6, 5, 4, 3]
# print(n[1::-1])#[2, 1]

# n[1:3]=['a','b','c']
# print(n)#[1, 'a', 'b', 'c', 4, 5, 6]

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# print(sounds[5][::-1])#ila


# s = ["super", "cali"]
# s[0],s[1]=s[1],s[0]
# print(s)#Avant=> ["super", "cali"] apres =>['cali', 'super']



# # Comprehension list ----------------------------------------------------------New CHAPITRE ______--------------------------------------------------------------------------
# # [_(3)_ for _(1)_ in _(2)_ ]
# # (1)pour chaque : [char, numero, mots....]
# # (2)present dans :[char, le tableau, la liste, le mot ]
# # (3)on va le :[l'ajouter, le multiplier, l'additionner, le mettre en capitale, ......]

# # exemple: 
# name= 'colt'
# [char.upper() for char in name]
# resultat= ['C', 'O', 'L', 'T']

# # autres exemple:
# friends= ['ashley', 'matt', 'michael']
# [friend[0].upper() for friend in friends]
# resultat= ['Ashley', 'Matt', 'Michael']

# numbers = [1,2,3,4,5,6]

# # Pair 
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)
# # impair 
# odds = [ num for num in numbers if num % 2 != 0]
# print(odds)

# # Ou

# c=[num *2 if num % 2 == 0 else num/2 for num in numbers]
# print(c)

# with_vowels = "This is so much fun !"
# d = ''.join(char for char in with_vowels if char not in "aeiou")
# print(d)

# answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
# # ['E', 'T', 'M']
# answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
# # [2, 4, 6]
# answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
# #the slice [::-1] is a quick way to reverse a string
# answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
# # ['eile', 'mit', 'ttam']

# answer = [[i for i in range(0,3)] for num in range(0,3)]
# # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# answer = [[i for i in range(0,10)] for num in range(0,10)]

# # [
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
# #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #  ]


# # Creer un dictionnaire 
# dog = dict(name = "joo", age= 2.5, dangerous= True)
# print(dog)
# user_info = {"city": "Paris", "temperature": 59.0, "is_raining": True}
# print(user_info["city"])#acceder a la valeur city 
# print("---------------values-------------------\n")
# for values in user_info.values():
#     print(values)
# print("------------ keys----------------------\n")
# for keys in user_info.keys():
#     print(keys)
# print("------------ keys Capitale----------------------\n")
# c = [keys.upper() for keys in user_info.keys()]
# print(c)


# # return list tuple a partir d'un dictionnaire 
# print(user_info.items())#dict_items([('city', 'Paris'), ('temperature', 59.0), ('is_raining', True)])

# for key, value in user_info.items():
#     print(key, value)
#         # city Paris
#         # temperature 59.0
#         # is_raining True

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# somme= [v for v in donations.values()]
# print(somme)
# print(somme[0])

# somme= [25.0, 88.99, 13.0, 99.5, 150.0, 50.25, 10.0]
# result = 0
# i=0
# for i in somme:
#     result += i
# print(result)#436.74

# total_donations = sum(donation for donation in donations.values())
# print(total_donations)

# print("sam" in donations)#True
# print("sam" in donations.keys())#True
# print(88.99 in donations.values())#True


# # Dictionnairy methode *************************************-----------------------------------------------
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # donations.clear()#effacer tous les valeurs 
# d = donations.copy() # copier le tableau existant 
# print(d.pop('sam')) # effacer une valeur du dictionnaire 
# print(d)
# print(d.popitem()) # effacer la derniere  valeur du dictionnaire 
# print(d)
# newUser = {}.fromkeys(['name','score', 'email', 'profile'], 'unknown')#{'email': 'unknown'}
# print(newUser)#{'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile': 'unknown'}
# print(newUser.get('name'))
# c = {"City": "Paris"}
# c.update(newUser)#Rajoute au valeur deja existant du dictionnaire les valeur d'un autres dict
# print(c)#{'City': 'Paris', 'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'profile': 'unknown'}

# # [_(4):(3)_ for _(1)_ in _(2)_ ]
# # (1)pour chaque : [char, numero, mots....]
# # (2)present dans :[char, le tableau, la liste, le mot ]
# # (3)on va le :[l'ajouter, le multiplier, l'additionner, le mettre en capitale, ......]
# # (4) keys ou autres 

# # exemple: 
# t = dict(first= 1, second= 2, third= 3)
# s = {key: value*2 for key, value in t.items()}
# print(s)# resutat {'first': 2, 'second': 4, 'third': 6}

# w ={num: num*2 for num in [1,2,3,4,5]}
# print(w)#{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# str1 = 'ABC'
# str2 = '123'
# o = {str1[i]: str2[i] for i in range(0, len(str1))}#DE LA POSITION 0 A LONGUEUR DU TABLEAU 
# print(o)#{'A': '1', 'B': '2', 'C': '3'}

# x= [1,2,3,4,5]
# y= {num: ("pair" if num % 2 == 0 else "Impair") for num in x}
# # ou y= {num: ("pair" if num % 2 == 0 else "Impair") for num in range(1, 100)}
# print(y)#{1: 'Impair', 2: 'pair', 3: 'Impair', 4: 'pair', 5: 'Impair'}

# hlist = {'city':'Paris', 'name':'unknown', 'score': 'unknown', 'email':'unknown', 'profile': 'unknown'}
# print(hlist)

# p = {(n.upper() if n is "name" else n):(v.upper() if v is 'unknown' else v ) for n,v in hlist.items() }
# print(p)#{'city': 'Paris', 'NAME': 'UNKNOWN', 'score': 'UNKNOWN', 'email': 'UNKNOWN', 'profile': 'UNKNOWN'}

# # Creer a partir d'une liste un dictionnaire
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {thing[0]: thing[1] for thing in person}
# print(answer)#{'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

# answerB = dict.fromkeys("aeiou", 0)
# print(answerB)#{'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# answerC = {count: chr(count) for count in range(65,91)}
# print(answerC)#{65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}



# string= "hello"
# c= {string[i]: i for i in range(0, len(string))}
    
# print(c)
# """
# return {string[i]: i for i in range(0, len(string))}
#  {'v': 0, 'a': 1, 's': 2, 'y': 3, 'A': 4, 'r': 6, 'e': 9, 't': 8}

#  return {i : string[i] for i in range(0, len(string))}                                       
#  {0: 'v', 1: 'a', 2: 's', 3: 'y', 4: 'A', 5: 'r', 6: 'r', 7: 'e', 8: 't', 9: 'e'}

 
#  return {letter: string.count(letter) for letter in string}
#  {'v': 1, 'a': 1, 's': 1, 'y': 1, 'A': 1, 'r': 2, 'e': 2, 't': 1}
# """ 
# str = string.replace(" ", "")# amanaplan acanalpanama => amanaplanacanalpanama


# print("How many kilometers did you cycle today?")
# kms = input()  # get user input
# miles = float(kms) / 1.60934  # convert from string to float and divide
# miles = round(miles, 2)  # round the result
# print(f"Your {kms}km ride was {miles }miles ")

# # ROUND SYNTAX:
# # round(thing to round, how many decimal points)


# # # # 11. WRITE A CODE THAT TAKES CELSIUS TEMPERATURE AND CONVERT IT TO FAHRENHEIT
# # # F = 9/5*C+32

# # # # 12. WRITE A CODE THAT CONVERTS FROM KM/H INTO MILES PER HOUR (REFER TO THE EQUATION BELOW)
# # # MPH = 0.6214 * KMH


# # # # NOW YOU SHOULD BE FAMILIAR WITH VARIABLES, VARIABLE ASSIGNMENTS, PRECEDENCE AND BASIC MATHEMATICAL OPERATIONS, GREAT JOB!

# # # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# # # ABSOLUTE BEGINNER LEVEL
# # # PRINT AND USER INPUT OPERATION
# # # 1. WRITE A CODE THAT TAKES A SPEED INPUT FROM A USER IN KMS PER HOUR, CONVERTS IT INTO MILES PER HOUR, AND PRINT BOTH SPEEDS TO THE SCREEN
# # # Enter speed in km/h: 30
# # # Speed in Km per hour = 30 KM/H
# # # Speed in Miles per hour = 18.642 MPH
# # # MPH = 0.6214 * KMH

# # # kmh = (input("enter votre kilometrage: "))
# # # k = int(kmh)
# # # mph = 0.6214 * k
# # # print(round(mph))

# # # 2. PRINT THE CALENDAR FOR THIS MONTH (RESEARCH IMPORT CALENDAR)
# # # import calendar
# # # calendar.month(theyear, themonth)¶
# # #       May 2018
# # # Mo Tu We Th Fr Sa Su
# # #     1  2  3  4  5  6
# # #  7  8  9 10 11 12 13
# # # 14 15 16 17 18 19 20
# # # 21 22 23 24 25 26 27
# # # 28 29 30 31

# # # import calendar

# # # print(calendar.month(theyear= 1980, themonth= 6))


# # # 3. EXPAND ON THE CODE ABOVE TO GET THE YEAR AND MONTH INFORMATION FROM THE USER
# # # Enter year [i.e.: 2019]: 2019
# # # Enter month [i.e.: 03]: 03
# # #      March 2019
# # # Mo Tu We Th Fr Sa Su
# # #              1  2  3
# # #  4  5  6  7  8  9 10
# # # 11 12 13 14 15 16 17
# # # 18 19 20 21 22 23 24
# # # 25 26 27 28 29 30 31

# # # import calendar

# # # year = int(input("Enter your year: "))
# # # month = int(input("Enter your month: "))
# # # print(calendar.month(year, month))


# # # 4. WRITE A CODE THAT TAKES TWO INTEGERS FROM THE USER AND PRINT OUT THE SUMMATION AND MULTIPLICATION
# # # Enter any integer number: 4
# # # Enter another integer number: 5
# # # Multiplication = 20, addition = 9

# # # x = int(input("enter your number : "))
# # # y = int(input("enter your number : "))
# # # a = x*y
# # # b = x+y
# # # print("la multiplication de  {} * {} donnes =>{}".format(x,y,a))
# # # print("l'addition de  {} +  {} donnes =>{}".format(x,y,b))

# # # 5. WRITE A CODE THAT TAKES A VALUE FROM THE USER AND PRINTS OUT THE NUMBER, ITS SQUARE AND ITS CUBIC VALUE
# # # Enter any integer number: 4
# # # 4 16 64
# # # import math


# # # v = int(input("Enter any integer number: "))
# # # print("the number is {}, this square is {} and this cube is {}".format(v,round(math.sqrt( v )), v**3))


# # # 6. WRITE A CODE THAT TAKES A TEMPERATURE INPUT FROM A USER IN CELSIUS AND CONVERTS IT INTO FAHRENHEIT
# # # Enter Temperature in Degree Celsius: 30
# # # Temperature in Celsius: 30 degC
# # # Temperature in Fahrenheit: 86.0  F
# # # import math
# # # v = int(input("Enter Temperature in Degree Celsius: "))
# # # f = 9/5*v+32
# # # print("Temperature in Celsius:{} degC,\n Temperature in Fahrenheit:{} F".format(v, round(f)))





# # # 7. WRITE A CODE THAT TAKES THE LENGTH AND WIDTH OF A RECTANGE FROM THE USER AND PRINTS THE AREA AND PERIMETER
# # # image.png

# # # Enter Width: 4
# # # Enter Length: 5
# # # Area = 20, Perimeter = 18
# # # 20

# # # import math
# # # w = int(input(" Enter Width: "))
# # # l = int(input(" Enter Length: "))
# # # area = w*l
# # # perimetre = 2*(w+l)
# # # print("Area {} m,\n le perimetre est de {} M ".format(area, perimetre))







# # # 8. WRITE A CODE THAT TAKES THE RADIUS OF A CIRCLE FROM THE USER AND PRINTS THE AREA, DIAMETER, AND CIRCUMFERENCE
# # # image.png
# # # Enter radius of a circle: 3
# # # circle diameter: 6
# # # circle area: 28.274333882308138
# # # circle circumference: 18.84955592153876


# # # import math
# # # r = int(input(" Enter rayon: "))

# # # area = math.pi *r**2
# # # diametre= 2*r
# # # circonference= 2 * math.pi * r

# # # print("Area {} m,\n diametre {},\n  circonference {} \n".format("%.2f" %area, diametre, "%.2f" %circonference))






# # # 9 SPLIT LE MOT ENTRERPAR LE USER 

# # # x = input("enter word :")
# # # # y = x.split()
# # # # print(y)#['aziz', 'est', 'parti']

# # # # x = input("enter word :")
# # # # y = [c for c in x]
# # # # ['a', 'z', 'i', 'z']
# # # # print(y)

# # # myList=["john", "katie", "carl", "alexi"]
# # # for i , element in enumerate(myList):
# # #     print(i , element)
# # # # 0 john
# # # # 1 katie
# # # # 2 carl
# # # # 3 alexi
# # # for i , element in enumerate("myList"):
# # #     print(i , element)
# # # # 0 m
# # # # 1 y
# # # # 2 L
# # # # 3 i
# # # # 4 s
# # # # 5 t

# # # for i in reversed(range(5)):
# # #     print(i)
# # # # 4
# # # # 3
# # # # 2
# # # # 1
# # # # 0
# # # listy=[i for i in range(1,10)]
# # # for i in listy(range(0,10)):
# # #     print(i)
# # # print(listy)
# # # # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # for i in listy:
# # #     if i % 2  == 0:
# # #         continue
# # #     print(i)

# # # resultaTab1 = [ i for i in listy if i % 2 == 0]# [2, 4, 6, 8]
# # # resultaTab = [ i for i in listy if i % 2 != 0] #[1, 3, 5, 7, 9]
# # # print(resultaTab1)
# # # print(resultaTab)


# # # tabledemutiplication
# # # for x in range(1,6):
# # #     for y in range(1,6):
# # #         print(f"{x} * {y} = {x*y}")

# # # tab=[(f"{x} * {y} = {x*y}") for x in range(1,6) for y in range(1,6)]
# # # print(tab)
# # # ['1 * 1 = 1', '1 * 2 = 2', '1 * 3 = 3', '1 * 4 = 4', '1 * 5 = 5', 
# # # '2 * 1 = 2', '2 * 2 = 4', '2 * 3 = 6', '2 * 4 = 8', '2 * 5 = 10', 
# # # '3 * 1 = 3', '3 * 2 = 6', '3 * 3 = 9', '3 * 4 = 12', '3 * 5 = 15',
# # #  '4 * 1 = 4', '4 * 2 = 8', '4 * 3 = 12', '4 * 4 = 16', '4 * 5 = 20', 
# # # '5 * 1 = 5', '5 * 2 = 10', '5 * 3 = 15', '5 * 4 = 20', '5 * 5 = 25']


# # # telephone=["samsung", "iphone", "googlephone"]
# # # color=["black", "red", "green"]

# # # for i in telephone:
# # #     for j in color:
# # #         if i =='samsung' and j == 'red':
# # #             continue
# # #         print(i, j)

# # # temp_C = [23,34,54,2,13]
# # # temp_F=["%.2f" %(9/5*c+32) for c in temp_C]
# # # print(temp_F)# ['73.40', '93.20', '129.20', '35.60', '55.40']


# # # my_string = 'T am becoming a python master 30 ans'
# # # c= [i for i in my_string if i.isdigit()]
# # # print(c)#['3', '0']

# # # exo 1: 
# # # for x in range(1,11):
# # #     print(f"{x: 2d}|   {x*x: 3d} |  {x*x*x: 4d}|")

# # # #    1|     1 |     1|
# # # #    2|     4 |     8|
# # # #    3|     9 |    27|
# # # #    4|    16 |    64|
# # # #    5|    25 |   125|
# # # #    6|    36 |   216|
# # # #    7|    49 |   343|
# # # #    8|    64 |   512|
# # # #    9|    81 |   729|
# # # #   10|   100 |  1000|


# # # exo 2: 
# # # import random
# # # keep= 'y'
# # # while keep == 'y':
# # #     print("Rolling the dice,please wait .....")
# # #     des1 = random.randrange(1, 7)
# # #     des = random.randrange(1, 7)
# # #     print(f"Rolling result of dice: {des1}")
# # #     print(f"Rolling result of dice: {des}")
# # #     if des == des1:
# # #         print("You win....")
# # #         break
# # #     keep= input("do you play again? Y or N \n")
# # #     if keep !='y': 
# # #         break
# # # print('END Game')

# # # exo 3:
# # # number = int(input("Choisit ta table multiplication : \n "))

# # # for i in range(1, 11):
# # #     print(f"{number} * {i} = {i*number}")

# # # exo 4:
# # # min= int(input("enter chiffre min: "))
# # # max= int(input("enter chiffre max: "))
# # # v= int(input("enter chiffre a additionner a chaque fois : "))
# # # while min < max:
# # #     min+=v
# # #     print(min)

# # # exo5
# # # for i in 'hello World':
# # #     if i == 'o':
# # #         continue
# # #     print(i)
# # # result
# # # h
# # # e
# # # l
# # # l

# # # W
# # # r
# # # l
# # # d

# # # # exo 6:
# # # print("ENTER LIST OF VALUE SEPERATE BY SPACE: ")
# # # # 52 45 12 36 89 42 11 02  45
# # # temp_C= [int(x) for x in input().split()]
# # # print(temp_C)# [52, 45, 12, 36, 89, 42, 11, 2, 45]

# # # exo 7:

# # # print("ENTER LIST OF VALUE SEPERATE BY SPACE: ")

# # # temp_C= [int(x) for x in input().split()]
# # # print(temp_C)#
# # # temp_F = [round(9/5*i+32, 2) for i in temp_C]
# # # print(temp_F)

# # # exo 8:
# # # import string
# # # import random

# # # print(string.digits)# 0123456789
# # # print(string.ascii_letters)# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# # # print(string.punctuation)# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# # # print(string.printable)# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# # # password= ""
# # # char =  string.punctuation+ string.ascii_letters + string.digits
# # # v= random.randrange(6,16)
# # # print(v)
# # # for i in range(1, v):
# # #     password = password + random.choice(char)

# # # print(password)#%<Y(moD*+1x&Z


# # # # exo 10:
# # # d = []
# # # c = input("enter votre phrase : \n")
# # # d = c.split(" ")
# # # print(d.sort())
# # # for i in d:
# # #     print(i)


# # # EXO 11
# # # color_phone=['red', "black",'gold','white']
# # # phone_name=['iphone', 'nexus', 'google', 'samsung']
# # # list_item =[(i,j) for i in phone_name for j in color_phone]
# # # print(list_item)
# # # [('iphone', 'red'), ('iphone', 'black'), ('iphone', 'gold'),
# # #  ('iphone', 'white'), ('nexus', 'red'), ('nexus', 'black'), 
# # #  ('nexus', 'gold'), ('nexus', 'white'), ('google', 'red'), 
# # #  ('google', 'black'), ('google', 'gold'), ('google', 'white'), 
# # #  ('samsung', 'red'), ('samsung', 'black'), ('samsung', 'gold'), ('samsung', 'white')]

# # # EXO 12:
# # # string_test = input("enter your string : \n")
# # # c =string_test.replace(" ", "")
# # # i= 0
# # # for letter in c:
# # #     if letter  == letter.upper() :
# # #         i+=1
# # # print(f" the string is : '{string_test}' with {len(c)} letters")
# # # print(f"total letter of lowerCase: {len(c) - i}\ntotal letter of UpperCase : {i}")


# # # EXO 13
# # # import time
# # # string_sign = input("enter your name : \n")

# # # i = 0
# # # while True:
# # #     i+=1
# # #     if i < 5:
# # #         # print(i)
# # #         print("i love you ", string_sign)
# # #         time.sleep(2)
# # #     else:
# # #         break

# # # EXO 14
# # # import string
# # # while True:
# # #     password=input("enter your password :")

# # #     if len(password) >= 10 and any(char.isupper() for char in password) and any(char.isdigit() for char in password) :
# # #         print("this password is succefully")
# # #         break
# # #     else:
# # #         print("password does not correct")
# # # enter your password :uhuh
# # # password does not correct
# # # enter your password :jjujihAZ
# # # password does not correct
# # # enter your password :ohiohAZK34ksjkj
# # # this password is succefully  



# # # EXO 15

# # # print("enter the number for calculate average")
# # # n= 1
# # # avg= 0
# # # while True:
# # #     x = int(input("enter the number : "))
# # #     n += 1
# # #     avg = (avg *(n-1)+x)/n
# # #     print('curent average is :', round(avg, 2))
# # #     print('number is : ',round(avg, 2))
# # #     if n == 4:
# # #         break


# # # ////////////////////FUNCTION ////////////////////////////////////////////

# # # Exo 16: 

# # # list1 =[1,3,5]
# # # list2 =[5,8,11]

# # for i, j in zip(list1, list2):
# # #     print(i, j)
# # # 1 5
# # # 3 8
# # # 5 11

# # #     print(i + j)
# # # # 6
# # # # 11
# # # # 16

# # # Exo17
# # # def greeting_fonction(name, greeter):
# # #     print(f"happy new years {name}, it very day {greeter}")


# # # list_name=["jade", "Mohamed", "denis", "sam"]
# # # list_greet =["happy","Sucess", "love", "wait"]

# # # for i, j in zip(list_name, list_greet):
# # #     greeting_fonction(i,j)
# # # happy new years jade, it very day happy
# # # happy new years Mohamed, it very day Sucess
# # # happy new years denis, it very day love
# # # happy new years sam, it very day wait


# # # Exo18:

# # # y= lambda *args:sum(args)
# # # print(y(1,2,3))


# # # # Exo19:
# # # a= [23,3,4,56]
# # # b= [3,36,34,6]
# # # c= [243,3,2,99]
# # # def summation(*args):
# # #     return sum(args)
# # # y = list(map(summation,a,b,c))
# # # print(y) #[269, 42, 40, 161]

# # # list_v = list(map(lambda x: x*x,a))
# # # print(list_v)#[529, 9, 16, 3136]


# # # # Exo20:
# # # a= [23,3,4,56]
# # # b= [3,36,34,6]


# # # y = list(map(lambda a,b : a*b , a,b))# a et b decrit les liste aue l on va utiliser
# # # print(y)#[69, 108, 136, 336]


# # # # EXO 21/
# # # list_t = [1, 20, 30,34, 99, 56, 10]
# # # out= list(filter(lambda x : (x%2 == 0), list_t))
# # # print(out)#[20, 30, 34, 56, 10]

# # # # EXO 22/

# # # age =[5,15,18,21,22,24,39,35]

# # # out = list( filter(lambda x : (x >=20 and x <=25), age))

# # # print(out)

# # # # # EXO 23

# # # print("enter your number :")
# # # c = int(input())

# # # def squarFunc(x):
# # #     return x*x

# # # print(f"the square de {c} is : {squarFunc(c)}")

# # # # # # EXO 24
# # # print("enter your number :")
# # # c = int(input("value one => "))
# # # print("enter your number :")
# # # d = int(input("value two => "))
# # # def add(a,b):
# # #     return a+b

# # # # def multip(a,b):
# # # #     return a*b
# # # v = (lambda a,b : a*b)
# # # print(f"multiplication egale {v(c,d)}\naddition egale : {add(c,d)}")

# # #  EXO 25
# # # import math

# # # c = int(input(" enter your number: "))
# # # # y = math.factorial(c)
# # # def f_factorial(x):
# # #     if x == 0:
# # #         return 1
# # #     return x * f_factorial(x-1)
# # # print(F"LE FACTORIAL DE {c} EST {f_factorial(c)}")
# # # 4! = 1 × 2 × 3 × 4 = 24

# # # # EXO 26
# # # list_t= range(1,21)
# # # f=[x**2 for x in list_t]
# # # print(f)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]



# # # EXO 26

# # # user_lowerbound = int(input("enter lower bound : "))
# # # user_upperbound = int(input("enter upper bound : "))

# # # c = range(user_lowerbound, user_upperbound)
# # # # list_positif = [ x for x in c if x %2 ==0  and x >0] ou la version en dessou 
# # # list_positif = list(filter(lambda x : (x %2 == 0  and x >0), c))
# # # print(list_positif)
# # # # enter lower bound : -30
# # # # enter upper bound : 50
# # # # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

# # # exo 27:

# # # a=[6,17,55,12,120,59,220,200]

# # # # c = [x for x in a if x %2==0]
# # # c = list(filter(lambda x : (x%2 ==0 ), a))
# # # print(c)#[6, 12, 120, 220, 200]



# # # # EXO 30 ///////////////////////////////////////////////////////////////////////////////////////////////////////////
# # # import numpy as np


# # # def matrix_operation(a,b):
# # #     # print("Matrice addition = \n", np.add(a,b))#Matrix addition = [[ 5 12][ 9 12]]
# # #     # print("Matrice subtract = \n", np.subtract(a,b))#Matrice subtract =[[ 1  6][ 7 -2]]
# # #     # print("Matrice multiply = \n", np.multiply(a,b))#Matrice multiply =[[ 6 27][ 8 35]]
# # #     # print("Matrix Transpose = \n", a.T) #Matrix Transpose =[[3 8][9 5]]
# # #     # print("Matrix multiply = \n", b.T)#Matrix multiply =[[2 1][3 7]]
# # #     # print("Matrice dot multiply = \n", np.dot(a,b))#Matrice dot multiply =[[15 72][21 59]]
# # #     print("Sqrt of Matrix  = \n", np.sqrt(a))#Sqrt of Matrix  =[[1.73205081 3.        ][2.82842712 2.23606798]]

# # # x = np.array([[3,9], [8,5]])
# # # y = np.array([[2,3], [1,7]])



# # # matrix_operation(x,y)


# # # EXO 31 ///////////////////////////////////////////////////////////////////////////////////////////////////////////

# # c_min = int(input("Enter number min :"))
# # c_max = int(input("Enter number max :"))


# # my_number=[]

# # for i in range(c_min,c_max):
# #     if (i %4 ==0 and i %3!=0):
# #         my_number.append(i)
# # print(my_number)
# # # Enter number max :200
# # # Enter number min :30
# # # [32, 40, 44, 52, 56, 64, 68, 76, 80, 88, 92, 100, 104, 112, 116, 124, 128, 136, 140, 148, 152, 160, 164, 172, 176, 184, 188, 196]




# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# """
# Les fonctions en python 
# """

# # # Creer des interactions entre les fonctions avec pour principale  en fonction 
# # #maitrequi possede une valeurs par defaut

# # # fonction ajouter 
# # def add(a,b):
# #     return a+b

# # def math(a,b, fn=add):
# #     return fn(a,b)

# # def subtract(a,b):
# #     return a-b

# # def multiplier(a,b):
# #     return a*b

# # a = math(2,2)# appel une fonction si aucune d'elle n'est appelé 

# # b = math(2,2, substrac) #appel la fonction soustrac avec les valeurs 2 et 2

# # c= math(2,6, multiplier)# appel la fonction mutiplier avec les valeur 2 et 2

# # print(a)#4
# # print(b)#0
# # print(c)#12

# # EXO/
# # def speak(animal="dog"):
# #     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
# #     noise = noises.get(animal)#donner la valeur de l'animal
# #     if noise:
# #         return noise
# #     return "?"

# # print(speak("duck"))



# # Deux arguments dans la fonction 
# # def full_name(first, lastname):
# #     return (f"your name is {first} {lastname}")

# # print(full_name(first="Do", lastname="John"))
# # print(full_name( lastname="John", first="Do"))





# # L UTILISATION DE GLOBAL  Attention a l'utilisation de global

# # def test():
# #     return name

# # print(test())

# # total = 0 

# # def increment():
# #     global total # Important utiliser global pour la variable existe dans la fonction aussi 
# #     total += 1
# #     return total

# # print(increment())

# # name = "Rustty" 

# # def nameglob():
# #     global name # Important utiliser global pour la variable existe dans la fonction aussi 
# #     return name

# # print(nameglob())

# # def test():
# #     return name

# # print(test())




# # utilisation de non local est preferable a global


# # def outer():
# #     count= 0
# #     def inner():
# #         nonlocal count
# #         count += 1
# #         return count
# #     return inner()

# # print(outer())


# # def exponent(num, power=2):
# # 	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
# # 	return num ** power

# # print(exponent(2,3)) #8
# # print(exponent(3)) #9
# # print(exponent(7)) #49

# # print(exponent.__doc__)





# # return_day exo 

# # EXO1----------------------------------------------------------------------------------
# #Creer un tableau de 1 a 7 pour les cles
# # tab=[i for i in range(1,8)]
# # # print(tab)
# # # inserer le tableau cles au tableau jours pour avoir les bonnes cles valeur
# # d = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
# # days = {tab[i]: d[i] for i in range(0,7)}
# # # print(days)

# # def day_is(a):
# #     return days.get(a)
# # print(day_is(7))

# # EXO2----------------------------------------------------------------------------------

# # retourne le dernier element d'une liste si vide envois le message empty

# # tab=[i for i in range(1,8)]
# # tab2 =["a","b","c","d","e"]
# # tab3 = []
# # def last_element(a):
# #     # return len(a)-1 #ici on a la longueur 
# #     # return a[-1]# ici on affiche le dernier element de la liste
# #     # facon numero 1:=<
# #     if a:
# #         return a[-1]
# #     return None

# #     # facon numero 2:=<
# #     if len(a) == 0:
# #         return None
# #     else:
# #         return a[-1]

# # print(last_element(tab))
# # print(last_element(tab2))
# # print(last_element(tab3))

# # # EXO3----------------------------------------------------------------------------------
# # '''
# # number_compare(1,1) # "Numbers are equal"
# # number_compare(1,0) # "First is greater"
# # number_compare(2,4) # "Second is greater"
# # '''

# # def number_compare(a, b):
# #     if a > b :
# #         return "First is greater"
# #     elif a< b:
# #         return "Second is greater"
# #     else:
# #         return "Numbers are equal"

# # # def number_compare(a,b):
# # #     if a > b:
# # #         return "First is greater"
# # #     elif b > a:
# # #         return "Second is greater"
# # #     return "Numbers are equal"
# # print(number_compare(1,1))
# # print(number_compare(1,0))
# # # print(number_compare(2,4))


# # # EXO4----------------------------------------------------------------------------------
# # '''
# # single_letter_count("Hello World", "h") # 1
# # single_letter_count("Hello World", "z") # 0
# # single_letter_count("HelLo World", "l") # 3
# # '''

# # def single_letter_count(a,b):
# #     # return a.upper().count(b)
# #     return a.lower().count(b.lower())

# # print(single_letter_count("Hello World", "h"))
# # print(single_letter_count("Hello World", "z"))
# # print(single_letter_count("Hello World", "l"))
# # n= "Hello World"
# # print(n.lower())#minuscule
# # print(n.upper())#majuscule

# # # EXO5----------------------------------------------------------------------------------

# '''
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
# '''

# # flesh out multiple_letter count:
# # def multiple_letter_count(string):
    
# #     # return dict.fromkeys(string)
   

  
# # def multiple_letter_count(string):
# #     # return {letter: string.count(letter) for letter in string}
# #     # {'v': 1, 'a': 1, 's': 1, 'y': 1, 'A': 1, 'r': 2, 'e': 2, 't': 1}
# #     # return {string[i]: i for i in range(0, len(string))}
# #     return {i : string[i] for i in range(0, len(string))}
# # print(multiple_letter_count("vasyArrete"))

# # string= "hello"
# # c= {string[i]: i for i in range(0, len(string))}
    
# # print(c)

# #------------------------------------------------------
# #------------------------------------------------------------
# # EXO FONCTIONS QUI INTERAGIS ENTRE ELLES 
# #------------------------------------------------------
# #------------------------------------------------------------
# #------------------------------------------------------
# #------------------------------------------------------------



# # '''
# # list_manipulation([1,2,3], "remove", "end") # 3
# # list_manipulation([1,2,3], "remove", "beginning") #  1
# # list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# # list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
# # '''

# # def list_manipulation(collection, command, location, value=None):
# #     if(command == "remove" and location == "end"):
# #         return collection.pop()#EFFACER A LA FIN 
# #     elif(command == "remove" and location == "beginning"):
# #         return collection.pop(0)#EFFACER AU DEBUT 
# #     elif(command == "add" and location == "beginning"):
# #         collection.insert(0,value)# AJOUR AU DEBUT 
# #         return collection
# #     elif(command == "add" and location == "end"):
# #         collection.append(value)# AJOUTER A LA FIN 
# #         return collection
    


# #EXO 6--------------------------------------------------6
# # def is_palindrome(string):
# #     str = string.replace(" ", "")
# #     if str[::-1] == str:
# #         return True
# #     return False

# # def is_palindrome2(string):
# #     stripped = string.replace(" ", "")
# #     return stripped == stripped[::-1]

# # print(is_palindrome('ZeamanaplaEnacanalpanama'))#False
# # print(is_palindrome('amanaplanacanalpanama'))#True
# # print(is_palindrome('amanaplan acanalpanama'))#True
# # print(is_palindrome2('amanaplan acanalpanama'))#True
# # print(is_palindrome2('ZeamanaplaEnacanalpanama'))#False
# # print(is_palindrome2('amanaplana canalpanama'))#True
# # '''
# # is_palindrome('testing') # False
# # is_palindrome('tacocat') # True
# # is_palindrome('hannah') # True
# # is_palindrome('robert') # False
# # is_palindrome('amanaplanacanalpanama') # True
# # '''



# #EXO 6--------------------------------------------------6

# # '''
# # frequency([1,2,3,4,4,4], 4) # 3
# # frequency([True, False, True, True], False) # 1
# # '''

# # def frequency(list,freq):
# #     return list.count(freq)

# # print(frequency([True, False, True, True], False))  

# #EXO 7 --------------------------------------------------6


# '''
# '''

# # def multiply_even_numbers(l):
# #     for i in l:
# #        return total 

# # multiply_even_numbers([2,3,4,5,6]) # 48
# # il faut trouver la valeur 48 en multipliant seulement avec les valeur pair
# # l = [2,3,4,5,6]
# # total= 1
# # for i in l:
# #     if i % 2 == 0:
# #         print(i)
# #         total = total * i
# # print(total)

# # EXO 9 ---------------------------------------------------------------------

# # '''
# # capitalize("tim") # "Tim"
# # capitalize("matt") # "Matt"
# # '''

# # def capitalize(string):
# #     c= string[0:1].upper()
# #     return c
    

# # print(capitalize("matt")) # "Matt"




# # ////////////////////////////////////////LAMBDA///////////////////////////////////////


# def addition(a,b):
#     return a + b
# print(addition(2,5))#7

# def addition2(*args):
#     return sum(args)
# print(addition2(1,2,6,4))#13






# nums = [2,3,4,6]
# doubles = list(map(lambda x : x*2, nums))
# print(doubles)#[4, 6, 8, 12]
# people= ["Name", "Jared","Job", "Musician"]
# peeps= list(map(lambda item: item.upper(), people))
# print(peeps)#['NAME', 'JARED', 'JOB', 'MUSICIAN']

# names=[
#     {'first': 'John', 'last':'steele'},
#     {'first': 'Jenna', 'last':'steele'},
#     {'first': 'Maro', 'last':'steele'},
#     {'first': 'Marc', 'last':'steele'},
#     {'first': 'Sandy', 'last':'steele'},
#     {'first': 'Brad', 'last':'steele'}
# ]

# first_names = list(map(lambda item : item['first'], names))
# print(first_names)#['John', 'Jenna', 'Maro', 'Marc', 'Sandy', 'Brad']


# #create fonction 
# def soustract(x): return x - x/2
# doubles= list(map(soustract, nums))
# print(doubles)#[1.0, 1.5, 2.0, 3.0]






# user=[
#     {'first': 'John', 'last':'steele', 'tweet':['hello','i live in ']},
#     {'first': 'Jenna', 'last':'steele', 'tweet':[]},
#     {'first': 'Maro', 'last':'steele', 'tweet':['batman','Spiderman....']},
#     {'first': 'Marc', 'last':'steele', 'tweet':[]},
#     {'first': 'Sandy', 'last':'steele', 'tweet':[]},
#     {'first': 'Brad', 'last':'steele', 'tweet':['I vote','i m different the all people']}
# ]

# checktwitos = [list(map())]



# playlist = {
# 	'title': 'patagonia bus', 
# 	'author': 'colt steele', 
# 	'songs': [
# 		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
# 		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
# 		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
# 	]
# }

# total_length = 0
# for song in playlist['songs']:
# 	total_length += song['duration']

# print(total_length)





# from random import randint
# # print("Rock...")
# # print("Paper...")
# # print("Scissors...")

# player = input("Player, make your move: ").lower()
# rand_num = randint(0,2)
# if rand_num == 0:
# 	computer = "rock"
# elif rand_num == 1:
# 	computer = "paper"
# else:
# 	computer = "scissors"

# print(f"Computer plays {computer}" )

# if player == computer:
# 	print("It's a tie!")
# elif player == "rock":
# 	if computer == "scissors":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "paper":
# 	if computer == "rock":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")
# elif player == "scissors":
# 	if computer == "paper":
# 		print("player wins!")
# 	else:
# 		print("computer wins!")	
# else:
# 	print("Please enter a valid move!")






# ////////////////////////////////////////////////////////////////////////////////////////////////////////////

# faire d'un mot qu'il soit iterable 
# def iterString(x):
#     c = iter(x)
#     while True:
#         try:
#             print(next(c))
#         except StopIteration:
#             print("End Of Iterator")
#             break


# jouer avec iter en inserant des func
# def iterString(x, func):
#     c = iter(x)
#     while True:
#         try:
#             test = next(c)
#         except StopIteration:
#             print("End Of Iterator")
#             break
#         else:
#             func(test)

# def square(x):
#     print(x*x)

# iterString("Oprah", print)
# iterString([1,2,3,4,5], square)

# Result
# O
# p
# r
# a
# h
# End Of Iterator
# 1
# 4
# 9
# 16
# 25
# End Of Iterator


class Counter:
    def __init__(self, low , high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

c = Counter(1,10)
v = iter(c)
print(next(v))






























