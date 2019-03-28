"""
Les fonctions en python 
"""

# # Creer des interactions entre les fonctions avec pour principale  en fonction 
# #maitrequi possede une valeurs par defaut

# # fonction ajouter 
# def add(a,b):
#     return a+b

# def math(a,b, fn=add):
#     return fn(a,b)

# def subtract(a,b):
#     return a-b

# def multiplier(a,b):
#     return a*b

# a = math(2,2)# appel une fonction si aucune d'elle n'est appelé 

# b = math(2,2, substrac) #appel la fonction soustrac avec les valeurs 2 et 2

# c= math(2,6, multiplier)# appel la fonction mutiplier avec les valeur 2 et 2

# print(a)#4
# print(b)#0
# print(c)#12

# EXO/
# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)#donner la valeur de l'animal
#     if noise:
#         return noise
#     return "?"

# print(speak("duck"))



# Deux arguments dans la fonction 
# def full_name(first, lastname):
#     return (f"your name is {first} {lastname}")

# print(full_name(first="Do", lastname="John"))
# print(full_name( lastname="John", first="Do"))





# L UTILISATION DE GLOBAL  Attention a l'utilisation de global

# def test():
#     return name

# print(test())

# total = 0 

# def increment():
#     global total # Important utiliser global pour la variable existe dans la fonction aussi 
#     total += 1
#     return total

# print(increment())

# name = "Rustty" 

# def nameglob():
#     global name # Important utiliser global pour la variable existe dans la fonction aussi 
#     return name

# print(nameglob())

# def test():
#     return name

# print(test())




# utilisation de non local est preferable a global


# def outer():
#     count= 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner()

# print(outer())


# def exponent(num, power=2):
# 	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
# 	return num ** power

# print(exponent(2,3)) #8
# print(exponent(3)) #9
# print(exponent(7)) #49

# print(exponent.__doc__)





# return_day exo 

# EXO1----------------------------------------------------------------------------------
#Creer un tableau de 1 a 7 pour les cles
# tab=[i for i in range(1,8)]
# # print(tab)
# # inserer le tableau cles au tableau jours pour avoir les bonnes cles valeur
# d = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
# days = {tab[i]: d[i] for i in range(0,7)}
# # print(days)

# def day_is(a):
#     return days.get(a)
# print(day_is(7))

# EXO2----------------------------------------------------------------------------------

# retourne le dernier element d'une liste si vide envois le message empty

# tab=[i for i in range(1,8)]
# tab2 =["a","b","c","d","e"]
# tab3 = []
# def last_element(a):
#     # return len(a)-1 #ici on a la longueur 
#     # return a[-1]# ici on affiche le dernier element de la liste
#     # facon numero 1:=<
#     if a:
#         return a[-1]
#     return None

#     # facon numero 2:=<
#     if len(a) == 0:
#         return None
#     else:
#         return a[-1]

# print(last_element(tab))
# print(last_element(tab2))
# print(last_element(tab3))

# # EXO3----------------------------------------------------------------------------------
# '''
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,0) # "First is greater"
# number_compare(2,4) # "Second is greater"
# '''

# def number_compare(a, b):
#     if a > b :
#         return "First is greater"
#     elif a< b:
#         return "Second is greater"
#     else:
#         return "Numbers are equal"

# # def number_compare(a,b):
# #     if a > b:
# #         return "First is greater"
# #     elif b > a:
# #         return "Second is greater"
# #     return "Numbers are equal"
# print(number_compare(1,1))
# print(number_compare(1,0))
# # print(number_compare(2,4))


# # EXO4----------------------------------------------------------------------------------
# '''
# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3
# '''

# def single_letter_count(a,b):
#     # return a.upper().count(b)
#     return a.lower().count(b.lower())

# print(single_letter_count("Hello World", "h"))
# print(single_letter_count("Hello World", "z"))
# print(single_letter_count("Hello World", "l"))
# n= "Hello World"
# print(n.lower())#minuscule
# print(n.upper())#majuscule

# # EXO5----------------------------------------------------------------------------------

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
# def multiple_letter_count(string):
    
#     # return dict.fromkeys(string)
   

  
# def multiple_letter_count(string):
#     # return {letter: string.count(letter) for letter in string}
#     # {'v': 1, 'a': 1, 's': 1, 'y': 1, 'A': 1, 'r': 2, 'e': 2, 't': 1}
#     # return {string[i]: i for i in range(0, len(string))}
#     return {i : string[i] for i in range(0, len(string))}
# print(multiple_letter_count("vasyArrete"))

# string= "hello"
# c= {string[i]: i for i in range(0, len(string))}
    
# print(c)

#------------------------------------------------------
#------------------------------------------------------------
# EXO FONCTIONS QUI INTERAGIS ENTRE ELLES 
#------------------------------------------------------
#------------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------------



# '''
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
# '''

# def list_manipulation(collection, command, location, value=None):
#     if(command == "remove" and location == "end"):
#         return collection.pop()#EFFACER A LA FIN 
#     elif(command == "remove" and location == "beginning"):
#         return collection.pop(0)#EFFACER AU DEBUT 
#     elif(command == "add" and location == "beginning"):
#         collection.insert(0,value)# AJOUR AU DEBUT 
#         return collection
#     elif(command == "add" and location == "end"):
#         collection.append(value)# AJOUTER A LA FIN 
#         return collection
    


#EXO 6--------------------------------------------------6
# def is_palindrome(string):
#     str = string.replace(" ", "")
#     if str[::-1] == str:
#         return True
#     return False

# def is_palindrome2(string):
#     stripped = string.replace(" ", "")
#     return stripped == stripped[::-1]

# print(is_palindrome('ZeamanaplaEnacanalpanama'))#False
# print(is_palindrome('amanaplanacanalpanama'))#True
# print(is_palindrome('amanaplan acanalpanama'))#True
# print(is_palindrome2('amanaplan acanalpanama'))#True
# print(is_palindrome2('ZeamanaplaEnacanalpanama'))#False
# print(is_palindrome2('amanaplana canalpanama'))#True
# '''
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True
# '''



#EXO 6--------------------------------------------------6

# '''
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1
# '''

# def frequency(list,freq):
#     return list.count(freq)

# print(frequency([True, False, True, True], False))  

#EXO 7 --------------------------------------------------6


'''
'''

# def multiply_even_numbers(l):
#     for i in l:
#        return total 

# multiply_even_numbers([2,3,4,5,6]) # 48
# il faut trouver la valeur 48 en multipliant seulement avec les valeur pair
# l = [2,3,4,5,6]
# total= 1
# for i in l:
#     if i % 2 == 0:
#         print(i)
#         total = total * i
# print(total)

# EXO 9 ---------------------------------------------------------------------

# '''
# capitalize("tim") # "Tim"
# capitalize("matt") # "Matt"
# '''

# def capitalize(string):
#     c= string[0:1].upper()
#     return c
    

# print(capitalize("matt")) # "Matt"




# ////////////////////////////////////////LAMBDA///////////////////////////////////////


def addition(a,b):
    return a + b
print(addition(2,5))#7

def addition2(*args):
    return sum(args)
print(addition2(1,2,6,4))#13






nums = [2,3,4,6]
doubles = list(map(lambda x : x*2, nums))
print(doubles)#[4, 6, 8, 12]
people= ["Name", "Jared","Job", "Musician"]
peeps= list(map(lambda item: item.upper(), people))
print(peeps)#['NAME', 'JARED', 'JOB', 'MUSICIAN']

names=[
    {'first': 'John', 'last':'steele'},
    {'first': 'Jenna', 'last':'steele'},
    {'first': 'Maro', 'last':'steele'},
    {'first': 'Marc', 'last':'steele'},
    {'first': 'Sandy', 'last':'steele'},
    {'first': 'Brad', 'last':'steele'}
]

first_names = list(map(lambda item : item['first'], names))
print(first_names)#['John', 'Jenna', 'Maro', 'Marc', 'Sandy', 'Brad']


#create fonction 
def soustract(x): return x - x/2
doubles= list(map(soustract, nums))
print(doubles)#[1.0, 1.5, 2.0, 3.0]






user=[
    {'first': 'John', 'last':'steele', 'tweet':['hello','i live in ']},
    {'first': 'Jenna', 'last':'steele', 'tweet':[]},
    {'first': 'Maro', 'last':'steele', 'tweet':['batman','Spiderman....']},
    {'first': 'Marc', 'last':'steele', 'tweet':[]},
    {'first': 'Sandy', 'last':'steele', 'tweet':[]},
    {'first': 'Brad', 'last':'steele', 'tweet':['I vote','i m different the all people']}
]

checktwitos = [list(map())]



playlist = {
	'title': 'patagonia bus', 
	'author': 'colt steele', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(total_length)





from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")



