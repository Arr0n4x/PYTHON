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

# Ici, comme age vaut 16 (qui est inférieur à 18), la condition age >= 18 est fausse. Le programme exécute donc le bloc else et affiche "Vous êtes mineur". Cette structure garantit qu'une des deux actions sera toujours exécutée.

# L'instruction elif
# L'instruction elif (else if) permet de tester plusieurs conditions en séquence. C'est très utile quand vous avez plus de deux cas possibles.

note = 85

if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
elif note >= 60:
    print("Passable")
else:
    print("Insuffisant")

# Le programme évalue les conditions dans l'ordre. Avec une note de 85, la première condition (note >= 90) est fausse, mais la deuxième (note >= 80) est vraie, donc il affiche "Très bien" et ignore les conditions suivantes. Cette structure permet de créer un système de classification précis.

# Conditions complexes
# Vous pouvez combiner plusieurs conditions avec les opérateurs logiques and, or et not. Cela rend vos programmes plus sophistiqués et capables de gérer des situations plus complexes.

age = 25
permis = True

if age >= 18 and permis:
    print("Vous pouvez conduire")
elif age >= 18 and not permis:
    print("Vous devez passer le permis")
else:
    print("Vous êtes trop jeune pour conduire")

# Dans cet exemple, l'opérateur and exige que les deux conditions soient vraies simultanément. L'opérateur not inverse une condition booléenne. Ces opérateurs permettent de créer une logique métier précise qui reflète les règles du monde réel.

# Boucles
# Les boucles permettent de répéter des blocs de code plusieurs fois sans avoir à les réécrire. Python propose deux types de boucles principales : for et while. C'est un concept fondamental qui vous évite de copier-coller du code et rend vos programmes plus efficaces.

# La boucle for
# La boucle for est utilisée pour itérer sur une séquence (comme une liste, un tuple, une chaîne de caractères, etc.). Elle est particulièrement pratique quand vous savez combien de fois vous voulez répéter une action.

# Boucle for avec range()

# Afficher les nombres de 0 à 4
for i in range(5):
    print(i)

# Afficher les nombres de 1 à 5
for i in range(1, 6):
    print(i)

# Afficher les nombres pairs de 0 à 10
for i in range(0, 11, 2):
    print(i)

# La fonction range() génère une séquence de nombres. range(5) produit 0, 1, 2, 3, 4. range(1, 6) produit 1, 2, 3, 4, 5 (le dernier nombre est exclu). range(0, 11, 2) produit 0, 2, 4, 6, 8, 10 (le troisième paramètre est le pas). Cette flexibilité vous permet d'adapter la boucle à vos besoins précis.