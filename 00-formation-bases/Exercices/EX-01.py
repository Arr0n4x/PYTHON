
# EX01
# # restaurant =("ALAMBRA","18 rue du commissaire","50 €",True)

# print(type(restaurant))
# nom,adresse,prix_moyen,végétariens_bienvenus_ou_non = restaurant
# print(f"nom = {nom}, adresse{adresse}, prix moyen = {prix_moyen},végétariens welcome = {végétariens_bienvenus_ou_non}")

# price = restaurant[2]

# print(price)

# temperature = 23
# no_cloud_sky = False

# if temperature > 25 and no_cloud_sky :
#     print("Allons à la plage")
# elif temperature>25 and not no_cloud_sky:
#     print("faut voir")
# elif temperature > 20 and temperature < 25 and no_cloud_sky :
#     print("Faut voir")
# elif temperature > 20 and temperature < 25 and not no_cloud_sky : 
#     print("restons à la maison")
# else :
#     print("restons à la maisons")

#EX 02 

# compteur = 0

# while compteur < 11 : 
#     print(f'compteur = {compteur}')
#     compteur += 1


# nombre = 5
# for i in range(11):
#     if i == 11:
#         break
#     print(f"{i}x{nombre}={i*nombre}")

#FIZZBUZZ

# for i in range(1,101) : 
#     if i % 3 == 0 and i % 5 == 0 :
#         print("FizzBuzz")
#     elif i % 5 == 0 :
#         print("Buzz")
#     elif i % 3 == 0 :
#         print("Fizz")
#     else :
#         print(i)

# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"
# occurence = 0
# for i in phrase :
#     if i == lettre_a_chercher :
#         occurence += 1
# print(occurence)

# exercice reussi mais code attendu en dessous

# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"

# resultat = phrase.lower().count(lettre_a_chercher)


# mot = "Python"

# for i in range(len(mot)):
#     print(i)

# ma version de l'exercice
# import random

# for i in range(6) :
#     roll_dice = random.randint(1, 6)
#     print(roll_dice)

# peut se faire aussi de cette manière 
# import random

# lancers = []
# for _ in range(6):
#     nombre = random.choice(range(1, 7))
#     lancers.append(nombre)

# ======================= Nouvelle exercice ================
# Le but de cet exercice est de récupérer à la fois l'indice et l'élément sur lequel nous bouclons dans chaque itération de la boucle for.

liste = ["Pierre", "Paul", "Marie"]

for index, element in enumerate(liste) : 
    print(f"{index} : { element}")