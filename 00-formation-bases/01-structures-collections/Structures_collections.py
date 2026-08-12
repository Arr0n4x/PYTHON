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

# Boucle for avec une chaîne de caractères

mot = "Python"
for lettre in mot:
    print(lettre)
    
# Cette boucle parcourt chaque caractère de la chaîne "Python" et l'affiche séparément. C'est très pratique pour analyser ou traiter du texte caractère par caractère.

# La boucle while
# La boucle while répète un bloc de code tant qu'une condition reste vraie. Elle est idéale quand vous ne savez pas à l'avance combien d'itérations seront nécessaires.

compteur = 0
while compteur < 5:
    print(f"Compteur : {compteur}")
    compteur += 1
    
# Cette boucle affiche la valeur du compteur et l'incrémente à chaque itération. Elle s'arrête quand compteur atteint 5. Il est crucial d'inclure une instruction qui modifie la condition (ici compteur += 1) pour éviter une boucle infinie.

# Instructions de contrôle des boucles
# Python offre trois instructions spéciales pour contrôler le comportement des boucles : break, continue, et pass. Ces instructions vous donnent un contrôle précis sur l'exécution de vos boucles.

# break
# L'instruction break permet de sortir immédiatement de la boucle, même si la condition n'est pas encore fausse.

for i in range(10):
    if i == 5:
        break
    print(i)
# Affiche 0, 1, 2, 3, 4

# Cette boucle devrait normalement afficher les nombres de 0 à 9, mais break l'interrompt dès que i égale 5. C'est utile pour arrêter une recherche dès qu'on trouve ce qu'on cherche.

# continue
# L'instruction continue permet de passer à l'itération suivante en ignorant le reste du code dans la boucle courante.

for i in range(10):
    if i % 2 == 0:  # Si le nombre est pair
        continue
    print(i)
# Affiche 1, 3, 5, 7, 9

# Cette boucle ignore les nombres pairs (grâce à continue) et n'affiche que les nombres impairs. L'opérateur % calcule le reste de la division : si un nombre divisé par 2 donne un reste de 0, il est pair.

# Listes
# Les listes sont des collections ordonnées et modifiables d'éléments. Elles sont l'une des structures de données les plus utilisées en Python car elles sont très flexibles et permettent de stocker plusieurs valeurs dans une seule variable. Ce survol suffit pour démarrer ; le guide dédié Listes Python détaille toutes les méthodes (insert, sort, compréhensions, listes imbriquées).

# Création de listes
# Liste vide
ma_liste = []

# Liste avec des éléments
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["hello", 42, True, 3.14]

# Une liste peut contenir n'importe quel type d'éléments, y compris des types différents dans la même liste (comme dans mixte). Les crochets [] définissent une liste, et les éléments sont séparés par des virgules.

# Accès aux éléments

fruits = ["pomme", "banane", "orange"]

# Accès par index (commence à 0)
print(fruits[0])  # "pomme"
print(fruits[1])  # "banane"
print(fruits[-1])  # "orange" (dernier élément)
print(fruits[-2])  # "banane" (avant-dernier élément)

# L'indexation en Python commence à 0, ce qui signifie que le premier élément est à l'index 0. Les indices négatifs permettent d'accéder aux éléments depuis la fin : -1 pour le dernier, -2 pour l'avant-dernier, etc.

# Modification de listes

fruits = ["pomme", "banane", "orange"]

# Modifier un élément
fruits[1] = "mangue"
print(fruits)  # ["pomme", "mangue", "orange"]

# Ajouter un élément à la fin
fruits.append("kiwi")
print(fruits)  # ["pomme", "mangue", "orange", "kiwi"]

# Supprimer un élément
fruits.remove("mangue")
print(fruits)  # ["pomme", "orange", "kiwi"]

# Les listes étant modifiables, vous pouvez changer leurs éléments après création. append() ajoute un élément à la fin, remove() supprime la première occurrence d'un élément spécifique.

# Cas d'usage courants des listes
# Les listes sont particulièrement adaptées pour stocker des collections d'éléments similaires qui peuvent évoluer au cours du temps. Elles sont idéales pour gérer des listes de tâches à faire, où vous ajoutez régulièrement de nouveaux éléments et en supprimez d'autres une fois terminés.

# Les listes conviennent parfaitement pour collecter des données saisies par l'utilisateur, comme une série de notes d'étudiants, des réponses à un questionnaire, ou des mesures prises lors d'une expérience scientifique. Leur caractère modifiable permet d'ajuster, corriger ou compléter les données facilement.

# Dans le domaine du traitement de données, les listes servent à maintenir des historiques d'actions (logs), stocker des résultats de calculs intermédiaires, ou gérer des files d'attente de tâches à traiter. Elles sont également essentielles pour implémenter des algorithmes de tri et de recherche, permettant de réorganiser et filtrer les informations selon différents critères.

# Tuples
# Les tuples sont des collections ordonnées et immuables d'éléments. Une fois créés, vous ne pouvez pas modifier leurs éléments. Cette immuabilité les rend plus sûrs pour stocker des données qui ne doivent pas changer. Pour approfondir, voir le guide dédié Tuples Python.

# Création de tuples
# Tuple vide
tuple_vide = ()

# Tuple avec des éléments
coordonnees = (10, 20)
couleurs = ("rouge", "vert", "bleu")

# Tuple avec un seul élément (attention à la virgule)
singleton = (42,)

# Les parenthèses () définissent un tuple. Pour un tuple à un seul élément, la virgule est obligatoire pour le distinguer d'une simple expression entre parenthèses.

# Déballage de tuples
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")  # x = 10, y = 20

# Échange de variables
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 10, b = 5

# Le déballage permet d'extraire les valeurs d'un tuple dans des variables séparées. C'est particulièrement élégant pour échanger les valeurs de deux variables sans variable temporaire.

# Cas d'usage courants des tuples
# Les tuples sont parfaits pour représenter des données qui vont ensemble de manière logique et qui ne doivent pas changer, comme des coordonnées géographiques (latitude, longitude), des points dans l'espace (x, y, z), ou des informations d'identification (nom, prénom, date de naissance).

# Ils sont très utiles pour retourner plusieurs valeurs depuis une fonction sans avoir à créer une structure complexe. Les tuples servent également de clés dans les dictionnaires quand vous avez besoin d'une clé composite, par exemple pour indexer des données par plusieurs critères simultanément.

# Dans les applications de configuration système, les tuples permettent de stocker des paramètres fixes qui ne doivent pas être modifiés accidentellement. Ils sont aussi employés pour représenter des enregistrements de données issus de bases de données, où chaque tuple correspond à une ligne avec ses différents champs.

# Dictionnaires
# Les dictionnaires sont des collections de paires clé-valeur. Ils permettent un accès rapide aux valeurs via leurs clés uniques. C'est comme un annuaire téléphonique où le nom est la clé et le numéro est la valeur. Le guide dédié Dictionnaires Python couvre toutes les méthodes (get, update, parcours, dictionnaires imbriqués).

# Création de dictionnaires
# Dictionnaire vide
dict_vide = {}

# Dictionnaire avec des éléments
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 30,
    "ville": "Paris"
}

# Les accolades {} définissent un dictionnaire. Chaque élément est une paire clé-valeur séparée par deux points :. Les clés doivent être uniques et de type immutable (chaînes, nombres, tuples).
# Accès aux valeurs

personne = {"nom": "Dupont", "prenom": "Jean", "age": 30}

# Accès direct
print(personne["nom"])  # "Dupont"

# Méthode get() (plus sûre)
print(personne.get("age"))  # 30
print(personne.get("email", "Non défini"))  # "Non défini"

# L'accès direct avec [] génère une erreur si la clé n'existe pas. La méthode get() est plus sûre : elle retourne None ou une valeur par défaut si la clé est absente.

# Cas d'usage courants des dictionnaires
# Les dictionnaires excellent dans la gestion d'informations structurées où chaque donnée est identifiée par un nom ou une étiquette unique. Ils sont indispensables pour créer des profils utilisateurs, fiches produits, ou configurations d'applications où chaque propriété a sa propre clé descriptive.

# Ils constituent la structure idéale pour implémenter des systèmes de cache et des index de recherche rapide, permettant de retrouver instantanément une information par sa clé. Les dictionnaires sont également essentiels pour compter et catégoriser des éléments, comme analyser la fréquence d'apparition de mots dans un texte ou regrouper des données par catégories.

# Dans le développement d'applications, ils servent à mapper des relations, comme associer des codes d'erreur à leurs messages explicatifs, ou lier des identifiants à des objets complexes. Les dictionnaires facilitent aussi la conversion entre différents formats de données et la création de tables de correspondance pour traduire des valeurs d'un système à un autre.

