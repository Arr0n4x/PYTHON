
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

# liste = ["Pierre", "Paul", "Marie"]

# for index, element in enumerate(liste) : 
#     print(f"{index} : { element}")


# =====================EXERCICE============================
# Dans cet exercice, nous avons une liste qui contient 50 nombres.

# Le but de cet exercice est de récupérer dans la liste nombres_pairs, uniquement les nombres pairs de la liste nombres.

# nombres = range(51)
# nombres_pairs =[pair for pair in nombres if pair % 2 == 0]
# print(nombres_pairs)

# a faire aussi de cette manière 

# nombres = range(51)
# nombres_pairs = []

# for i in nombres:
#     if i % 2 == 0:
#         nombres_pairs.append(i)

# =====================EXERCICE==============================
# Dans cet exercice, nous sommes en présence d'une boucle while infinie !

# En l'état actuel, le script ne s'arrêtera jamais et la phrase 'Exercice réussi !' ne sera jamais assignée à la variable resultat.

# Vous devez modifier la boucle while afin d'en sortir et d'assigner la phrase 'Exercice réussi !' à la variable resultat.

# i = 0

# while i < 10:
# 	i +=1

# resultat = "Exercice fini"

# print(resultat)

# ========================EXERCICE============================
# Dans cet exercice, vous devez additionner toutes les valeurs du dictionnaire ensemble.

# Votre script doit donc retourner le nombre entier 8700 dans la variable resultat.

# employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}

# resultat = sum(employes.values())

# print(f"resultat : {resultat}")

# =========================================exercice==========
# Dans cet exercice, nous allons récupérer la valeur de la clé "prenom", contenue dans le dictionnaire employes.

# Votre script doit donc retourner la chaîne de caractères "Pierre" dans la variable resultat.

# employes = {
#             "01": {
#                 "identite": {
#                     "prenom": "Pierre",
#                     "nom": "Dupont"
#                     }
#                 }
#             }

# resultat = employes["01"]["identite"]["prenom"]

# print(resultat)
