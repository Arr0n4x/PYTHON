# Une liste en Python est une collection ordonnée et modifiable d'éléments, créée avec des crochets : courses = ["pain", "lait", "oeufs"]. Elle stocke plusieurs valeurs dans une seule variable, de n'importe quel type (nombres, chaînes, objets, voire d'autres listes), et vous pouvez à tout moment ajouter, supprimer ou modifier ses éléments. C'est la structure de données la plus utilisée en Python.

# Ce guide, pour développeurs débutants et intermédiaires, couvre la création, l'accès par index, le parcours, les méthodes essentielles (append, sort, index) et les compréhensions de liste.

# Ce que vous allez apprendre
# Créer une liste vide, pré-remplie ou générée avec range()
# Accéder aux éléments par index, index négatif et slicing
# Ajouter et supprimer avec append, insert, extend, remove, pop, del
# Parcourir une liste avec for, enumerate() et while
# Trouver, compter et trier avec index, count, sort et sorted
# Transformer une liste avec les compréhensions et gérer les listes imbriquées
# Pourquoi utiliser les listes ?
# Les listes sont idéales pour stocker des séquences d'éléments liés entre eux, comme des informations de suivi pour un projet, une liste de courses, ou encore des données de capteurs dans une application IoT. En Python, les listes sont simples à manipuler et intuitives, ce qui en fait un choix privilégié pour les développeurs de tous niveaux.

# Créer et initialiser une liste
# La création d’une liste en Python est très simple. Les listes se définissent en entourant les éléments par des crochets []. Ces éléments peuvent être de tout type : entiers, chaînes de caractères, booléens, voire d'autres listes, rendant les listes Python très flexibles.

# Créer une liste vide
# Pour créer une liste sans élément, utilisez simplement des crochets vides [] :

ma_liste = []

# Cela initialise une liste vide, prête à être remplie. Une liste vide peut être utile dans de nombreux contextes, par exemple lorsque l’on souhaite collecter des éléments au fur et à mesure dans une boucle.

# Créer une liste avec des valeurs initiales
# Vous pouvez également initialiser une liste avec des valeurs prédéfinies :

ma_liste = [10, 20, 30, 40, 50]

# Dans cet exemple, ma_liste contient cinq éléments de type entier. Cette méthode est idéale pour les cas où vous connaissez déjà les éléments à ajouter.

# Créer une liste avec des éléments de types différents
# Une liste en Python peut contenir des éléments de types variés, ce qui permet d'imbriquer des données de différents types dans une même collection :

ma_liste = [1, "texte", True, 3.14]

# Ici, la liste contient un entier, une chaîne de caractères, un booléen et un nombre à virgule flottante. Cette flexibilité permet de regrouper des données diverses dans une seule variable.

# Générer automatiquement des valeurs avec range()
# Si vous avez besoin d'une séquence de nombres, vous pouvez utiliser la fonction range(), souvent en combinaison avec list(). Par exemple, pour créer une liste de nombres de 0 à 9 :

ma_liste = list(range(10))

# La fonction range() génère une séquence de nombres que list() convertit en liste.

# Accéder aux éléments d’une liste
# Une fois qu'une liste est créée, vous devez savoir comment accéder à ses éléments pour les utiliser ou les modifier. Les listes Python utilisent l'indexation pour accéder à chaque élément.

# Indexation de base
# Les listes sont des séquences indexées en Python, ce qui signifie que chaque élément possède une position dans la liste, appelée index. L’indexation commence à 0, donc le premier élément d’une liste est situé à l’index 0, le deuxième à l’index 1 et ainsi de suite.

ma_liste = [10, 20, 30, 40, 50]
print(ma_liste[0])  # Affiche 10
print(ma_liste[2])  # Affiche 30

# Utilisation de l'indexation négative
# Python permet aussi d’accéder aux éléments d’une liste en utilisant des indices négatifs, ce qui est particulièrement utile pour accéder aux éléments depuis la fin de la liste. L'index -1 correspond au dernier élément, -2 à l'avant-dernier et ainsi de suite.

print(ma_liste[-1])  # Affiche 50
print(ma_liste[-2])  # Affiche 40

# Extraire une sous-liste avec le slicing
# Le slicing permet de sélectionner une partie de la liste (une sous-liste). Cette technique est particulièrement utile pour obtenir une série d'éléments situés à des indices consécutifs.

sous_liste = ma_liste[1:4]
print(sous_liste)  # Affiche [20, 30, 40]

# Utilisation du pas (step) dans le slicing
# En ajoutant un troisième argument au slicing, vous pouvez spécifier un pas pour sauter des éléments.

sous_liste = ma_liste[0:5:2]
print(sous_liste)  # Affiche [10, 30, 50]

# Avec le slicing ma_liste[0:5:2], on sélectionne les éléments de la liste en sautant un élément sur deux.

# Ajouter et supprimer des éléments
# Python offre différentes méthodes pour ajouter ou supprimer des éléments d’une liste, rendant la modification de listes très flexible.

# Ajouter un élément avec append()
# La méthode append() ajoute un élément à la fin de la liste :

ma_liste.append(60)
print(ma_liste)  # Affiche [10, 20, 30, 40, 50, 60]

# Insérer un élément à une position spécifique avec insert()
# Pour insérer un élément à une position précise, utilisez insert(index, element) :

ma_liste.insert(1, 15)
print(ma_liste)  # Affiche [10, 15, 20, 30, 40, 50, 60]

# Ajouter plusieurs éléments avec extend()
# Pour ajouter plusieurs éléments en une fois, extend() est idéal :

ma_liste.extend([70, 80])
print(ma_liste)  # Affiche [10, 15, 20, 30, 40, 50, 60, 70, 80]

# Supprimer un élément avec remove()
# La méthode remove() supprime la première occurrence d'un élément :

ma_liste.remove(15)
print(ma_liste)  # Affiche [10, 20, 30, 40, 50, 60, 70, 80]

# Supprimer un élément avec pop()
# pop() supprime un élément à une position donnée et le retourne. Si aucun index n'est précisé, il retire et retourne le dernier élément :

dernier_element = ma_liste.pop()
print(dernier_element)  # Affiche 80
print(ma_liste)         # Affiche [10, 20, 30, 40, 50, 60, 70]

# Supprimer un élément avec del
# L’instruction del permet de supprimer un élément par son index, ou même un groupe d'éléments avec le slicing :

del ma_liste[0]
print(ma_liste)  # Affiche [20, 30, 40, 50, 60, 70]

del ma_liste[1:3]
print(ma_liste)  # Affiche [20, 50, 60, 70]

# Modifier les éléments d’une liste
# Les listes en Python sont modifiables (ou mutables), ce qui signifie que vous pouvez changer la valeur des éléments existants.

# Modifier un élément spécifique
# Pour modifier un élément, accédez à sa position avec son index et assignez-lui une nouvelle valeur :

ma_liste[1] = 45
print(ma_liste)  # Affiche [20, 45, 60, 70]

# Modifier plusieurs éléments avec le slicing
# Vous pouvez utiliser le slicing pour modifier plusieurs éléments à la fois :

ma_liste[1:3] = [35, 55]
print(ma_liste)  # Affiche [20, 35, 55, 70]

# Ajouter ou supprimer des éléments avec le slicing
# Le slicing permet également d’ajouter ou de supprimer des éléments en une opération :

ma_liste[2:2] = [40, 50]
print(ma_liste)  # Affiche [20, 35, 40, 50, 55, 70]

# Ici, 40 et 50 sont insérés à l’index 2.

# Fonctions intégrées utiles pour les listes
# Python propose de nombreuses fonctions intégrées pour manipuler les listes de manière efficace. Ces fonctions permettent d’obtenir des informations sur une liste ou d’effectuer des opérations courantes comme le comptage, le tri ou l'inversion des éléments.

# Longueur de la liste avec len()
# La fonction len() est utilisée pour obtenir le nombre d'éléments présents dans une liste, ce qui peut être pratique dans des boucles ou pour vérifier si une liste est vide :

ma_liste = [10, 20, 30, 40, 50]
print(len(ma_liste))  # Affiche 5

# Ici, len(ma_liste) renvoie 5 car la liste contient cinq éléments.

# Trouver la position d'un élément avec index()
# La méthode index() permet de trouver la première position d'un élément spécifique dans une liste. Si l'élément n'est pas trouvé, Python génère une erreur ValueError :

position = ma_liste.index(30)
print(position)  # Affiche 2

# Dans cet exemple, index() renvoie 2 car l'élément 30 se trouve à l’index 2 dans la liste.

# Vérifier la présence d'un élément avec in
# Vous pouvez utiliser l'opérateur in pour vérifier si un élément existe dans une liste. Cela renvoie True si l'élément est trouvé et False sinon :

print(20 in ma_liste)  # Affiche True
print(60 in ma_liste)  # Affiche False

# Compter les occurrences d'un élément avec count()
# La méthode count() permet de compter le nombre d'occurrences d'un élément spécifique dans la liste. Cela peut être utile pour analyser des données ou trouver les doublons :

ma_liste = [10, 20, 20, 30, 20]
print(ma_liste.count(20))  # Affiche 3

# Dans cet exemple, count() retourne 3 car le nombre 20 apparaît trois fois dans la liste ma_liste.

# Trier une liste avec sort()
# La méthode sort() trie les éléments d'une liste dans l'ordre croissant par défaut, mais elle peut également trier en ordre décroissant en utilisant l’argument reverse=True :

ma_liste = [30, 10, 20, 50, 40]
ma_liste.sort()
print(ma_liste)  # Affiche [10, 20, 30, 40, 50]

ma_liste.sort(reverse=True)
print(ma_liste)  # Affiche [50, 40, 30, 20, 10]

# Le tri est fait en place, ce qui signifie que la liste d'origine est modifiée. Si vous souhaitez conserver la liste initiale, utilisez la fonction sorted() pour créer une nouvelle liste triée.

# Inverser une liste avec reverse()
# La méthode reverse() permet d’inverser l'ordre des éléments dans une liste. Contrairement à sort(), cette méthode ne trie pas mais retourne simplement les éléments dans l'ordre opposé :

ma_liste.reverse()
print(ma_liste)  # Affiche [10, 20, 30, 40, 50] dans l’ordre inverse

# Boucles et itérations sur une liste
# Parcourir les éléments d’une liste est une opération fréquente en Python, notamment pour appliquer des opérations à chaque élément. Cette section vous montre comment utiliser les boucles pour itérer sur les éléments d’une liste.

# Parcourir une liste avec une boucle for
# La manière la plus simple et la plus courante de parcourir une liste est d’utiliser une boucle for. Elle vous permet d’accéder à chaque élément de la liste :

ma_liste = [10, 20, 30, 40, 50]
for element in ma_liste:
    print(element)

# Dans cet exemple, chaque élément de ma_liste est affiché un par un. C’est la méthode privilégiée pour des opérations simples.

# Utiliser enumerate() pour obtenir les index et les éléments
# Parfois, vous avez besoin de l’index de chaque élément en plus de sa valeur. Dans ce cas, utilisez la fonction enumerate() qui vous permet de récupérer à la fois l'index et l'élément :

for index, element in enumerate(ma_liste):
    print(f"Index {index} : {element}")

# enumerate() renvoie des couples index, valeur pour chaque élément de la liste, ce qui est pratique dans les cas où la position de l’élément est importante pour le traitement.

# Parcourir une liste avec une boucle while
# Une autre méthode pour parcourir une liste est d’utiliser une boucle while. Elle peut être utile si vous voulez parcourir la liste jusqu’à ce qu’une condition spécifique soit remplie :

index = 0
while index < len(ma_liste):
    print(ma_liste[index])
    index += 1

# Ici, nous utilisons un compteur index pour accéder aux éléments de ma_liste jusqu'à ce que tous les éléments aient été parcourus.

# Listes imbriquées (listes de listes)
# Les listes imbriquées sont des listes qui contiennent d'autres listes comme éléments. Elles permettent de créer des structures de données plus complexes, comme des matrices ou des tableaux multidimensionnels.

# Créer une liste imbriquée
# Pour créer une liste imbriquée, il suffit d'inclure des sous-listes au sein d'une liste principale :

ma_liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Ici, ma_liste est une liste de trois sous-listes, chacune contenant trois éléments.

# Accéder aux éléments d'une liste imbriquée
# Pour accéder aux éléments d'une liste imbriquée, vous utiliserez deux niveaux d'indexation. Le premier index sélectionne la sous-liste, le second sélectionne l'élément dans cette sous-liste.

print(ma_liste[0])      # Affiche [1, 2, 3]
print(ma_liste[0][1])   # Affiche 2

# Dans cet exemple, ma_liste[0] renvoie la première sous-liste [1, 2, 3], et ma_liste[0][1] renvoie le deuxième élément de cette sous-liste, soit 2.

# Parcourir une liste imbriquée avec des boucles
# Pour parcourir tous les éléments d'une liste imbriquée, utilisez des boucles imbriquées : une première boucle pour parcourir les sous-listes et une seconde pour parcourir les éléments de chaque sous-liste.

for sous_liste in ma_liste:
    for element in sous_liste:
        print(element)

# Chaque sous_liste est parcourue dans la boucle externe et chaque element dans la boucle interne.

# Utiliser des compréhensions de liste avec des listes imbriquées
# Les compréhensions de liste peuvent être imbriquées pour manipuler des listes imbriquées de manière concise. Par exemple, pour aplatir une liste imbriquée en une liste simple :

ma_liste_imbriquee = [[1, 2, 3], [4, 5], [6, 7, 8]]
aplatie = [element for sous_liste in ma_liste_imbriquee for element in sous_liste]
print(aplatie)  # Affiche [1, 2, 3, 4, 5, 6, 7, 8]

# Dans cet exemple, chaque element est extrait de chaque sous_liste pour créer une liste aplanie, aplatie.

# Les compréhensions de liste
# Les compréhensions de liste permettent de créer de nouvelles listes de manière concise et lisible. Elles sont particulièrement utiles pour effectuer des transformations ou des filtrages rapides.

# Syntaxe de base des compréhensions de liste
# La syntaxe de base d'une compréhension de liste consiste en une expression suivie d'une boucle for. Par exemple, pour créer une liste des carrés des éléments d’une liste existante :

ma_liste = [1, 2, 3, 4, 5]
carres = [x ** 2 for x in ma_liste]
print(carres)  # Affiche [1, 4, 9, 16, 25]

# Utiliser des conditions dans les compréhensions de liste
# Les compréhensions de liste peuvent inclure des conditions pour filtrer les éléments :

pairs = [x for x in ma_liste if x % 2 == 0]
print(pairs)  # Affiche [2, 4]

# Ici, seuls les éléments pairs de ma_liste sont inclus dans la nouvelle liste pairs.

# Compréhensions de liste imbriquées
# Les compréhensions de liste imbriquées permettent de manipuler les listes imbriquées de manière concise. Par exemple, pour obtenir les carrés des éléments d’une liste imbriquée :

ma_liste_imbriquee = [[1, 2], [3, 4]]
carres = [[x ** 2 for x in sous_liste] for sous_liste in ma_liste_imbriquee]
print(carres)  # Affiche [[1, 4], [9, 16]]

# Chaque sous-liste est parcourue pour calculer les carrés des éléments.

# Méthodes avancées sur les listes
# Enfin, Python propose des méthodes avancées pour copier, fusionner et transformer les listes de manière efficace, notamment avec map() et filter().

# Copier une liste
# Pour créer une copie d’une liste, vous pouvez utiliser copy() ou le slicing [:]. Cela évite de modifier la liste d’origine par inadvertance :

ma_liste = [1, 2, 3]
copie = ma_liste.copy()

# Fusionner des listes
# Pour fusionner deux listes, utilisez l'opérateur + ou la méthode extend(). La différence est importante : + construit une nouvelle liste et laisse les deux originales intactes, alors que extend() modifie la liste sur laquelle vous l'appelez.

# fusion = liste1 + liste2

# Utiliser map() et filter()
# map() applique une fonction à chaque élément d’une liste, tandis que filter() sélectionne les éléments répondant à une condition :

ma_liste = [1, 2, 3]
carres = list(map(lambda x: x ** 2, ma_liste))
pairs = list(filter(lambda x: x % 2 == 0, ma_liste))