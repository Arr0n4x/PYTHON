# Variables et Types de Données
# Les variables sont un élément essentiel de la programmation. Elles permettent de stocker et de manipuler des données. En Python, les variables sont très flexibles, car vous n'avez pas besoin de déclarer explicitement leur type. Dans ce chapitre, nous allons explorer la déclaration de variables et les types de données de base en Python.

# Déclaration de Variables
# En Python, la déclaration d'une variable est simple. Vous pouvez utiliser un nom de variable significatif et Python déterminera automatiquement le type de données en fonction de la valeur que vous lui attribuez. Voici un exemple :

# nom = "Alice"  # Une variable de type chaîne de caractères (str)
# age = 30       # Une variable de type entier (int)
# taille = 1.75  # Une variable de type flottant (float)
# est_majeur = True  # Une variable de type booléen (bool)

# Les noms de variables sont sensibles à la casse (par exemple, nom et Nom sont considérés comme deux variables distinctes).
# Vous pouvez utiliser des lettres, des chiffres et des caractères de soulignement _ dans les noms de variable, mais ils ne doivent pas commencer par un chiffre.
# Les noms de variable doivent être choisis de manière significative pour faciliter la compréhension du code.
# Types de Données de Base
# Python offre plusieurs types de données de base que vous utiliserez fréquemment. Voici les principaux :

# Entier (int) : Utilisé pour stocker des nombres entiers, positifs ou négatifs.
# Flottant (float) : Utilisé pour stocker des nombres décimaux (avec une virgule flottante).
# Chaîne de caractères (str) : Utilisé pour stocker du texte, entouré de guillemets simples (') ou doubles (").
# Booléen (bool) : Utilisé pour représenter des valeurs de vérité (True ou False).
# Exemples d'utilisation de ces types de données :

# entier = 42
# flottant = 3.14
# chaine = "Bonjour, Python !"
# est_vrai = True

# Conversion entre Types de Données
# Vous pouvez convertir des variables d'un type à un autre en utilisant des fonctions de conversion. Par exemple :

# nombre_texte = "123"  # Une chaîne de caractères
# nombre_entier = int(nombre_texte)  # Convertit en entier
# nombre_flottant = float(nombre_texte)  # Convertit en flottant

# # Vous pouvez également convertir des nombres en chaînes de caractères
# age = 30
# age_texte = str(age)

# Assurez-vous de comprendre les types de données, car ils sont fondamentaux pour la manipulation des données en Python.

# Utilisation de Commentaires
# Les commentaires sont un moyen d'ajouter des explications dans votre code Python. Ils sont ignorés lors de l'exécution du programme. Utilisez le symbole # pour commencer un commentaire.

# Exemple :

# # Ceci est un commentaire
# nom = "Alice"  # Ceci est également un commentaire

# Les commentaires sont utiles pour expliquer votre code aux autres programmeurs (ou à vous-même) et pour rendre le code plus lisible.

# Opérations de Base
# En Python, vous pouvez effectuer un large éventail d'opérations sur les variables pour manipuler des données et effectuer des calculs. Dans cette section, nous allons explorer les opérations de base telles que les opérations mathématiques, la manipulation de chaînes de caractères et les opérations logiques.

# Opérations Mathématiques
# Python prend en charge les opérations mathématiques courantes que vous attendez d'un langage de programmation. Voici quelques exemples :

# Addition (+) : Utilisée pour ajouter deux nombres.
# Soustraction (-) : Utilisée pour soustraire un nombre d'un autre.
# Multiplication (*) : Utilisée pour multiplier deux nombres.
# Division (/) : Utilisée pour diviser un nombre par un autre.
# Modulo (%) : Utilisée pour obtenir le reste de la division de deux nombres.
# Exemples :

# a = 10
# b = 3

# addition = a + b  # 13
# soustraction = a - b  # 7
# multiplication = a * b  # 30
# division = a / b  # 3.333... (flottant)
# modulo = a % b  # 1

# Manipulation de Chaînes de Caractères
# Python offre de nombreuses opérations pour manipuler des chaînes de caractères (texte). Voici quelques-unes des opérations de base :

# Concaténation : Combinez deux chaînes de caractères en les ajoutant ensemble.
# Longueur : Obtenez la longueur d'une chaîne de caractères en utilisant la fonction len().
# Indexation : Accédez à des caractères spécifiques dans une chaîne en utilisant des indices (attention : l'index commence à 0).
# Découpage : Obtenez une sous-chaîne en spécifiant une plage d'indices.
# Exemples :

# chaine1 = "Bonjour"
# chaine2 = "Python"

# concatenation = chaine1 + ", " + chaine2  # "Bonjour, Python"
# longueur = len(chaine1)  # 7
# premier_caractere = chaine1[0]  # "B"
# sous_chaine = chaine2[0:3]  # "Pyt"

# Opérations Logiques
# Les opérations logiques sont couramment utilisées pour prendre des décisions dans les structures de contrôle conditionnelles. Les opérations logiques de base sont :

# Et logique (and) : Vrai seulement si les deux conditions sont vraies.
# Ou logique (or) : Vrai si au moins l'une des conditions est vraie.
# Non logique (not) : Inverse la valeur logique d'une condition.
# Exemples :

# vrai = True
# faux = False

# resultat_et = vrai and faux  # Faux
# resultat_ou = vrai or faux  # Vrai
# resultat_non = not vrai  # Faux

# Priorités des Opérations
# Lorsque vous effectuez plusieurs opérations dans une expression, Python suit un ordre de priorité standard. Cependant, vous pouvez utiliser des parenthèses pour spécifier l'ordre d'évaluation.

# Exemple :

# resultat = 5 + 2 * 3  # 11 (la multiplication a une priorité plus élevée)
# resultat_parentheses = (5 + 2) * 3  # 21 (les parenthèses changent l'ordre)

# Bonnes Pratiques pour l'écriture de scripts Python
# Lorsque vous créez des scripts Python destinés à être exécutés directement depuis un terminal, il est important de respecter certaines conventions pour assurer une bonne organisation et lisibilité de votre code.

# Le Shebang (#!/usr/bin/env python3)
# Le shebang est une ligne spéciale qui doit se trouver en première position dans votre fichier Python. Il indique au système quel interpréteur utiliser pour exécuter le script, permettant ainsi de le lancer directement depuis le terminal sans avoir à invoquer explicitement l'interpréteur Python.

# Exemple de Shebang pour Python 3 :

# #!/usr/bin/env python3

# Dans cet exemple, /usr/bin/env est une commande qui localise l'interpréteur Python 3 sur le système, quel que soit son emplacement exact, garantissant ainsi que le script fonctionne sur différentes configurations. Si votre fichier est enregistré sous le nom mon_script.py, vous pouvez exécuter directement ce script après lui avoir donné les permissions d'exécution (voir plus bas).

# Structure d'un en-tête de script
# Un bon script Python commence généralement par un en-tête qui donne des informations sur l'auteur, la date et une description générale du script. Cela aide à la compréhension et à la maintenance du code à long terme.

# Exemple d'en-tête :

# #!/usr/bin/env python3
# # Auteur : Jean Dupont
# # Date : 2024-09-04
# # Description : Ce script lit un fichier, gère les exceptions et affiche un message de bienvenue.

# Cet en-tête est placé immédiatement après le shebang et contient des commentaires sur le but et le contexte du script. Il est particulièrement utile dans les grands projets ou dans les environnements collaboratifs où plusieurs développeurs travaillent ensemble.

# Les commentaires dans le code
# Les commentaires en Python commencent par le symbole # et permettent de documenter le code. Ils sont essentiels pour expliquer la logique ou les décisions de conception, rendant le code plus facile à comprendre et à maintenir.

# Commentaires en ligne : Ils expliquent des portions spécifiques de code.

# # Calculer la somme de deux nombres
# somme = 5 + 3

# Commentaires de bloc : Utilisés pour expliquer des sections plus longues ou plus complexes.

# # Cette fonction prend un nom en entrée et retourne
# # une chaîne de caractères qui inclut ce nom dans une salutation.
# def dire_bonjour(nom):
#     return f"Bonjour, {nom} !"

# Rendre le script exécutable
# Une fois votre script Python écrit avec un shebang en tête, vous pouvez le rendre exécutable sur un système de type UNIX (Linux, macOS). Cela signifie que vous pouvez l'exécuter comme n'importe quel autre programme, sans avoir à spécifier python3 avant le nom du fichier.

# Ajouter le shebang (comme mentionné ci-dessus).
# Changer les permissions du fichier pour le rendre exécutable à l'aide de la commande chmod :
# Fenêtre de terminal
# chmod +x mon_script.py

# Exécuter le script directement depuis le terminal :
# Fenêtre de terminal
# ./mon_script.py

# Cela permet d'exécuter le script sans avoir à appeler explicitement Python. Si vous n'ajoutez pas de shebang, vous devrez toujours exécuter le script en appelant l'interpréteur directement :

# Fenêtre de terminal
# python3 mon_script.py