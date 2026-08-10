# Les structures de contrôle décident du déroulement d'un programme Python (conditions if/elif/else, boucles for/while), et les collections stockent des ensembles de valeurs (listes, tuples, dictionnaires). Ce sont les briques qui font passer d'un script linéaire à un programme capable de prendre des décisions, de répéter des actions et d'organiser des données.

# Ce guide, pour développeurs débutants, donne une vue d'ensemble de ces concepts ; chaque collection dispose ensuite d'un guide dédié plus complet.

# Ce que vous allez apprendre
# Prendre des décisions avec if, elif et else
# Répéter des actions avec les boucles for et while
# Contrôler les boucles avec break, continue et pass
# Choisir la bonne collection entre liste, tuple et dictionnaire
# Créer et manipuler chacune de ces collections


# Prérequis
# Avant de commencer ce guide, assurez-vous de maîtriser :

# L'installation de Python
# Les variables et types de données de base
# Les opérations mathématiques et logiques
# L'écriture de scripts Python avec shebang
# Revoir les fondamentaux si nécessaire

# Instructions Conditionnelles
# Les instructions conditionnelles permettent à votre programme de prendre des décisions en fonction de certaines conditions. En Python, nous utilisons principalement if, elif et else. Ces structures sont fondamentales car elles permettent à votre programme d'adapter son comportement selon les circonstances.

# L'instruction if
# L'instruction if exécute un bloc de code uniquement si une condition est vraie. C'est comme dire "si cette condition est remplie, alors fais cela".

age = 18

if age >= 18:
    print("Vous êtes majeur")