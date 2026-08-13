# Un tuple en Python est une collection ordonnée et immuable de valeurs, créée avec des parenthèses : point = (48.85, 2.35). Une fois créé, un tuple ne peut plus être modifié, ce qui le distingue de la liste et le rend idéal pour des données fixes : coordonnées, valeurs de retour d'une fonction, ou clés de dictionnaire.

# Ce que vous allez apprendre
# Créer un tuple et comprendre le cas piège du tuple à un seul élément
# Accéder aux éléments par index, index négatif et slicing
# Différencier tuple et liste : immuabilité, performance, cas d'usage
# Utiliser les opérations de base : concaténation, in, count(), index()
# Employer les namedtuples pour nommer les champs d'un tuple
# Retourner plusieurs valeurs d'une fonction avec un tuple et les déballer
# Qu'est-ce qu'un tuple en Python ?
# Un tuple en Python est une collection ordonnée et immuable de valeurs. Il ressemble à une liste, mais ses éléments ne peuvent pas être modifiés une fois le tuple créé. Cette immuabilité est sa caractéristique centrale : elle garantit que les données restent constantes et permet d'utiliser un tuple comme clé de dictionnaire, ce qu'une liste ne permet pas.

# Pourquoi utiliser des tuples ?
# Les tuples sont utiles dans de nombreux cas, notamment lorsque vous avez besoin d'une collection de valeurs qui ne doit pas être modifiée. Les tuples sont également plus rapides que les listes, car ils sont immuables et ne nécessitent pas de gestion de la mémoire supplémentaire.

# Comment créer un tuple ?
# Python offre trois façons de fabriquer un tuple : les parenthèses, la virgule seule et la fonction tuple(). Les trois produisent le même objet, mais elles ne se valent pas à la lecture. Un cas mérite une attention particulière, celui du tuple à un seul élément, où oublier la virgule ne déclenche aucune erreur et donne simplement autre chose que ce que vous attendiez.

# Créer un tuple en Python
# La création de tuples en Python est simple et repose sur l’utilisation de parenthèses et de virgules pour rassembler les éléments. Contrairement aux listes, les tuples sont immuables, ce qui signifie qu’ils ne peuvent pas être modifiés après leur création. Cette caractéristique en fait un excellent choix pour stocker des données fixes ou des éléments que vous ne voulez pas modifier accidentellement au cours du programme.

# Pour créer un tuple, il suffit de mettre les éléments entre parenthèses et de les séparer par des virgules. Voici quelques exemples simples de tuples en Python :

# Création d'un tuple de plusieurs éléments
mon_tuple = (1, 2, 3, 4)
print(mon_tuple)  # Output : (1, 2, 3, 4)

# Création d'un tuple contenant des types variés
tuple_mixte = (1, "Python", 3.14, True)
print(tuple_mixte)  # Output : (1, 'Python', 3.14, True)

# La syntaxe du tuple est très proche de celle de la liste, à la différence près que les tuples utilisent des parenthèses () alors que les listes utilisent des crochets [].

# Python permet également de créer des tuples sans utiliser les parenthèses. Si vous écrivez une suite de valeurs séparées par des virgules, Python les interprétera automatiquement comme un tuple.

tuple_sans_parentheses = 10, 20, 30
print(tuple_sans_parentheses)  # Output : (10, 20, 30)

# Cependant, pour des raisons de clarté, il est recommandé d’utiliser des parenthèses, surtout lorsque le tuple est plus complexe ou contient plusieurs types d’éléments.

# Pour un tuple contenant un seul élément, il est essentiel de mettre une virgule après cet élément, même si cela peut sembler contre-intuitif. Sans cette virgule, Python ne reconnaît pas la structure comme un tuple et interprète simplement l’élément comme son type de base.

# Tuple avec un seul élément
tuple_seul_element = (42,)
print(tuple_seul_element)  # Output : (42,)

# Sans virgule, ce n'est pas un tuple
pas_un_tuple = (42)
print(pas_un_tuple)  # Output : 42

# Cette particularité est importante pour éviter les erreurs lorsque vous créez des tuples à élément unique. La virgule informe Python que l'élément est dans un tuple et non isolé.

# Vous pouvez aussi utiliser la fonction tuple() pour créer un tuple à partir d’autres types itérables, comme une liste ou une chaîne de caractères. C’est particulièrement utile lorsque vous souhaitez convertir un type mutable en une structure immuable :

# Créer un tuple à partir d'une liste
liste_exemple = [1, 2, 3, 4]
tuple_a_partir_liste = tuple(liste_exemple)
print(tuple_a_partir_liste)  # Output : (1, 2, 3, 4)

# Créer un tuple à partir d'une chaîne
chaine = "Python"
tuple_a_partir_chaine = tuple(chaine)
print(tuple_a_partir_chaine)  # Output : ('P', 'y', 't', 'h', 'o', 'n')

# Accéder aux éléments d’un tuple
# Une fois qu’un tuple est créé, il est souvent nécessaire d’accéder aux éléments qu’il contient pour les manipuler ou les utiliser dans le code. Comme les tuples sont des séquences indexées, chaque élément possède une position unique, appelée index, qui permet d'y accéder facilement. Dans ce chapitre, nous verrons les différentes techniques pour accéder aux éléments d’un tuple en Python.

# Accéder aux éléments par index
# L’indexation est la méthode la plus courante pour accéder aux éléments d’un tuple. Chaque élément d’un tuple est repéré par un index, qui commence à 0 pour le premier élément et augmente de un pour chaque élément suivant. L’utilisation de l’index est simple et directe :

mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[0])  # Output : 10
print(mon_tuple[2])  # Output : 30

# Dans cet exemple, mon_tuple[0] renvoie le premier élément (10) et mon_tuple[2] renvoie le troisième élément (30).

# Indexation négative
# Python offre la possibilité d’utiliser des index négatifs pour accéder aux éléments en partant de la fin du tuple. L’index -1 représente le dernier élément, -2 l’avant-dernier et ainsi de suite. Cette méthode est pratique lorsque vous souhaitez accéder aux derniers éléments sans connaître la longueur exacte du tuple.

mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[-1])  # Output : 50
print(mon_tuple[-3])  # Output : 30

# Ici, mon_tuple[-1] renvoie le dernier élément (50) et mon_tuple[-3] renvoie le troisième élément en partant de la fin (30).

# Extraction de sous-tuples (slicing)
# L’extraction de sous-tuples (ou slicing) permet de récupérer une portion spécifique d’un tuple en utilisant une syntaxe basée sur les indices. La syntaxe pour le slicing est tuple[start:stop:step] :

# start est l’indice de début (inclus).
# stop est l’indice de fin (exclu).
# step est le pas entre chaque élément.
# Voici quelques exemples pour illustrer cette fonctionnalité :

mon_tuple = (10, 20, 30, 40, 50)

# Extraire les trois premiers éléments
print(mon_tuple[0:3])  # Output : (10, 20, 30)

# Extraire du deuxième au quatrième élément
print(mon_tuple[1:4])  # Output : (20, 30, 40)

# Extraire tous les éléments avec un pas de 2
print(mon_tuple[::2])  # Output : (10, 30, 50)

# Le slicing est très flexible et permet d’obtenir des sous-parties d’un tuple sans devoir le modifier. Notez que comme les tuples sont immuables, le slicing retourne toujours un nouveau tuple.

# Accéder aux éléments dans un tuple imbriqué
# Les tuples imbriqués sont des tuples qui contiennent d’autres tuples. Pour accéder à un élément spécifique dans un tuple imbriqué, il suffit de combiner plusieurs index pour naviguer dans les différentes couches de la structure :

tuple_imbrique = (1, 2, (3, 4, 5), (6, 7), 8)

# Accéder à l'élément 3 dans le sous-tuple (3, 4, 5)
print(tuple_imbrique[2][0])  # Output : 3

# Accéder à l'élément 7 dans le sous-tuple (6, 7)
print(tuple_imbrique[3][1])  # Output : 7

# Dans cet exemple, tuple_imbrique[2][0] accède au premier élément du sous-tuple (3, 4, 5), tandis que tuple_imbrique[3][1] renvoie le deuxième élément du sous-tuple (6, 7).

# Erreurs courantes d'indexation
# Étant donné que les tuples sont immuables, il est impossible de modifier un élément directement via son index. Toute tentative de modification d’un élément d’un tuple entraîne une erreur. Voici un exemple d’erreur courante liée à l’indexation :

mon_tuple = (1, 2, 3, 4)

# Essayer de modifier un élément
mon_tuple[0] = 10  # Error : TypeError: 'tuple' object does not support item assignment

# Python renverra une TypeError pour indiquer que l'objet tuple ne peut pas être modifié. Si vous devez modifier des valeurs, vous devrez créer un nouveau tuple avec les valeurs souhaitées.

# Les opérations de base sur les tuples
# Les tuples en Python, bien qu’immutables, permettent d’effectuer plusieurs opérations pratiques pour manipuler et interroger leur contenu. Dans ce chapitre, nous explorerons les opérations courantes, les fonctions intégrées et les techniques pour utiliser efficacement les tuples dans vos programmes.

# Concaténation de tuples
# La concaténation permet de combiner plusieurs tuples pour en former un nouveau. L’opérateur + est utilisé pour joindre deux tuples en un seul, sans modifier les tuples d'origine.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple_concatenation = tuple1 + tuple2
print(tuple_concatenation)  # Output : (1, 2, 3, 4, 5, 6)

# Dans cet exemple, tuple_concatenation est un nouveau tuple contenant les éléments des deux tuples d'origine, tuple1 et tuple2.

# Répétition d’un tuple
# L’opérateur * permet de répéter un tuple plusieurs fois pour en créer un plus grand contenant des éléments identiques en série. Cette opération est utile pour créer des structures régulières ou des motifs répétitifs.

tuple_repetition = (1, 2) * 3
print(tuple_repetition)  # Output : (1, 2, 1, 2, 1, 2)

# Le tuple (1, 2) est répété trois fois pour former tuple_repetition, sans affecter le tuple original.

# Vérification de l’appartenance avec in
# L’opérateur in est utilisé pour vérifier si un élément spécifique est présent dans un tuple. Cette opération renvoie True si l’élément est trouvé, sinon False.

tuple_elements = (1, 2, 3, 4, 5)

# Vérifier si 3 est dans le tuple
print(3 in tuple_elements)  # Output : True

# Vérifier si 6 est dans le tuple
print(6 in tuple_elements)  # Output : False

# L’opérateur in est pratique pour effectuer des vérifications rapides dans des structures de données immuables comme les tuples.

# Utilisation des fonctions intégrées len(), min() et max()
# Python propose plusieurs fonctions intégrées pour travailler avec les tuples, notamment :

# len() : renvoie le nombre d’éléments dans le tuple.
# min() : renvoie la plus petite valeur présente dans le tuple.
# max() : renvoie la plus grande valeur présente dans le tuple.
# Ces fonctions permettent d’obtenir des informations essentielles sur les tuples.

mon_tuple = (10, 20, 30, 40)

# Nombre d'éléments dans le tuple
print(len(mon_tuple))  # Output : 4

# Valeur minimale
print(min(mon_tuple))  # Output : 10

# Valeur maximale
print(max(mon_tuple))  # Output : 40

# Ces fonctions sont particulièrement utiles pour traiter des tuples numériques ou pour obtenir rapidement des valeurs clés.

# Compter les occurrences d’un élément avec count()
# La méthode count() permet de compter le nombre de fois qu’un élément spécifique apparaît dans un tuple. C’est pratique pour analyser les données contenues dans un tuple sans avoir à écrire de boucle.

tuple_compte = (1, 2, 3, 2, 4, 2)

# Compter le nombre de fois que 2 apparaît
print(tuple_compte.count(2))  # Output : 3

# Dans cet exemple, count() montre que l’élément 2 apparaît trois fois dans tuple_compte.

# Trouver l’index d’un élément avec index()
# La méthode index() permet de trouver la première occurrence d’un élément dans un tuple et retourne l’indice correspondant. Si l’élément n’est pas présent, elle déclenche une erreur ValueError.

tuple_index = (10, 20, 30, 40)

# Trouver l'index de l'élément 30
print(tuple_index.index(30))  # Output : 2

# Ici, index() renvoie 2 car l’élément 30 se trouve à cet emplacement dans tuple_index. Attention, si l’élément est absent, il est conseillé de vérifier son existence avec in avant d’utiliser index() pour éviter des erreurs.

# Comparaison de tuples
# Les tuples peuvent être comparés avec les opérateurs de comparaison standard (==, !=, <, >, <=, >=). Python compare les tuples en analysant chaque élément dans l’ordre et dès qu’il trouve une différence, il détermine le résultat de la comparaison.

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

# Comparer les tuples
print(tuple1 == tuple2)  # Output : False
print(tuple1 < tuple2)   # Output : True

# Dans cet exemple, tuple1 est considéré comme étant plus petit que tuple2 car l’élément 3 dans tuple1 est inférieur à 4 dans tuple2.

# Conversion d’un tuple en liste
# Bien que les tuples soient immuables, il est possible de les convertir en liste pour les manipuler plus librement. La conversion se fait en utilisant la fonction list() et permet de créer une liste avec les mêmes éléments.

mon_tuple = (1, 2, 3, 4)
liste = list(mon_tuple)
print(liste)  # Output : [1, 2, 3, 4]

# Cette méthode est utile si vous avez besoin de modifier les éléments d’un tuple temporairement, puis de les reconstituer dans un tuple si nécessaire.

# Les tuples nommés (namedtuples)
# Les tuples nommés (ou namedtuples) sont une extension des tuples standards en Python, permettant de donner un nom aux éléments d’un tuple pour améliorer la lisibilité et la maintenabilité du code. Ils sont particulièrement utiles lorsqu'on souhaite représenter des données structurées de manière immuable, tout en facilitant l’accès aux éléments par des noms explicites au lieu d’indices.

# Les namedtuples font partie du module collections de Python et sont souvent utilisés pour créer des structures de données légères et faciles à utiliser, idéales pour remplacer les objets simples ou les tuples classiques lorsque des noms d’attributs sont nécessaires.

# Créer un namedtuple
# Pour créer un namedtuple, on utilise la fonction namedtuple() du module collections. Il faut d'abord importer namedtuple, puis définir la structure en lui donnant un nom et une liste d'attributs. Voici comment créer un namedtuple de base :

from collections import namedtuple

# Création d'un namedtuple appelé Point avec deux attributs : x et y
Point = namedtuple("Point", ["x", "y"])

# Créer une instance de Point
p = Point(10, 20)
print(p)  # Output : Point(x=10, y=20)

# Dans cet exemple, Point est un namedtuple avec deux attributs, x et y. L'objet p est une instance de Point contenant les valeurs 10 pour x et 20 pour y.

# Accéder aux éléments d’un namedtuple
# Une fois le namedtuple créé, vous pouvez accéder à ses éléments de la même manière qu'avec un tuple standard, en utilisant des indices, mais aussi en utilisant des noms d'attributs pour plus de clarté.

# Accès aux éléments par nom
print(p.x)  # Output : 10
print(p.y)  # Output : 20

# Accès aux éléments par indice
print(p[0])  # Output : 10
print(p[1])  # Output : 20

# Accéder aux éléments par nom rend le code plus lisible, car p.x et p.y sont plus explicites que p[0] et p[1].

# Utilisation pratique des namedtuples
# Les namedtuples sont particulièrement utiles pour représenter des données structurées sans avoir à utiliser des classes complètes. Par exemple, ils peuvent être utilisés pour représenter des points géométriques, des dates, des coordonnées GPS, ou même des enregistrements de bases de données.

# Exemple : Représentation d’une personne

# Création d'un namedtuple pour représenter une personne
Personne = namedtuple("Personne", ["nom", "prenom", "age"])

# Créer une instance de Personne
personne = Personne("Dupont", "Alice", 30)
print(personne.nom)     # Output : Dupont
print(personne.prenom)  # Output : Alice
print(personne.age)     # Output : 30

# Dans cet exemple, le namedtuple Personne est utilisé pour stocker les informations d'une personne de manière structurée.

# Convertir un namedtuple en dictionnaire
# Il peut être utile de convertir un namedtuple en dictionnaire pour des traitements spécifiques. Les namedtuples disposent de la méthode _asdict() qui retourne un OrderedDict avec les noms d’attributs comme clés.

# Conversion d'un namedtuple en dictionnaire
personne_dict = personne._asdict()
print(personne_dict)  # Output : {'nom': 'Dupont', 'prenom': 'Alice', 'age': 30}

# Cette méthode est pratique pour manipuler les données du namedtuple comme un dictionnaire, par exemple pour des opérations de formatage ou pour l'exporter en JSON.

# Remplacer les valeurs dans un namedtuple avec _replace()
# Bien que les namedtuples soient immuables, la méthode _replace() permet de créer une nouvelle instance en modifiant un ou plusieurs attributs. Cette opération est utile lorsque vous avez besoin de créer une version modifiée sans altérer l’original.

# Remplacer l'âge dans le namedtuple
personne_modifiee = personne._replace(age=31)
print(personne_modifiee)  # Output : Personne(nom='Dupont', prenom='Alice', age=31)

# Dans cet exemple, personne_modifiee est une nouvelle instance de Personne avec l'âge mis à jour, sans modifier l'objet personne original.

# Utilisation des tuples pour le retour de multiples valeurs
# En Python, les fonctions peuvent retourner plusieurs valeurs en utilisant un tuple. Cela est particulièrement utile pour transmettre plusieurs résultats ou informations d'une fonction sans nécessiter de structures complexes. Lorsque vous retournez plusieurs valeurs dans une fonction, Python les regroupe automatiquement dans un tuple, simplifiant ainsi le code et améliorant sa lisibilité.

# Dans ce chapitre, nous allons voir comment retourner plusieurs valeurs avec un tuple, comment décomposer ces valeurs (ou les "déballer") lors de leur réception et examiner quelques exemples d’utilisation pratiques.

# Retourner plusieurs valeurs avec un tuple
# Pour retourner plusieurs valeurs d’une fonction, il suffit de les séparer par des virgules après l’instruction return. Python les encapsule automatiquement dans un tuple.

# Fonction qui retourne plusieurs valeurs
def calculs(a, b):
    somme = a + b
    produit = a * b
    return somme, produit  # Retourne un tuple (somme, produit)

resultat = calculs(5, 3)
print(resultat)  # Output : (8, 15)

# Dans cet exemple, calculs() retourne deux valeurs : la somme et le produit de a et b. La fonction renvoie un tuple (8, 15).

# Déballer les valeurs d’un tuple lors du retour
# Lorsque vous recevez un tuple contenant plusieurs valeurs, vous pouvez les déballer en affectant chaque valeur à une variable séparée. Cela rend le code plus clair et rend chaque valeur immédiatement accessible.

# Déballer les valeurs retournées
somme, produit = calculs(5, 3)
print(somme)    # Output : 8
print(produit)  # Output : 15

# Ici, somme et produit reçoivent respectivement les valeurs 8 et 15 du tuple retourné par la fonction, ce qui évite d’avoir à accéder aux valeurs en utilisant des indices.

# Cas d’usage des tuples pour le retour de valeurs multiples
# L’utilisation des tuples pour retourner plusieurs valeurs est particulièrement utile dans des situations où une fonction doit effectuer plusieurs calculs ou vérifier plusieurs conditions. Voici quelques cas pratiques :

# Exemple 1 : Retourner des statistiques

# Une fonction qui calcule les statistiques de base sur une liste de nombres peut retourner plusieurs valeurs utiles (moyenne, minimum et maximum) sous forme de tuple.

def statistiques(data):
    moyenne = sum(data) / len(data)
    minimum = min(data)
    maximum = max(data)
    return moyenne, minimum, maximum

# Utiliser la fonction et déballer les résultats
data = [10, 20, 30, 40, 50]
moyenne, minimum, maximum = statistiques(data)
print("Moyenne:", moyenne)    # Output : Moyenne : 30.0
print("Min:", minimum)        # Output : Min : 10
print("Max:", maximum)        # Output : Max : 50

# Dans cet exemple, la fonction statistiques() retourne trois valeurs sous forme de tuple, ce qui permet de capturer toutes les informations utiles sans nécessiter de structures de données supplémentaires.

# Exemple 2 : Validation de données

# Une fonction peut également retourner plusieurs informations après avoir validé des données, comme un booléen indiquant la validité et un message d’erreur si les données ne sont pas valides.

def valider_utilisateur(nom, age):
    if not nom:
        return False, "Nom requis"
    if age < 0:
        return False, "Âge invalide"
    return True, "Utilisateur valide"

# Déballer les valeurs pour récupérer le statut et le message
statut, message = valider_utilisateur("Alice", 25)
print(statut)   # Output : True
print(message)  # Output : Utilisateur valide

# Dans cet exemple, valider_utilisateur() retourne un tuple avec deux valeurs : un booléen indiquant si l'utilisateur est valide et un message descriptif. Ce modèle de retour est pratique pour des vérifications ou validations dans lesquelles plusieurs résultats doivent être retournés.