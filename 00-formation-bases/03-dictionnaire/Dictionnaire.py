# Chaque dictionnaire se compose de trois éléments fondamentaux  que vous manipulerez constamment :

# Élément	Description	Exemple
# Clé	    Identifiant unique (immuable)	"nom", "age", 42
# Valeur	Donnée associée (tout type)	    "Alice", 30, [1, 2, 3]
# Paire	    Association clé → valeur	    "nom": "Alice"

# La clé joue le rôle d'étiquette : elle doit être unique dans le dictionnaire (impossible d'avoir deux clés identiques) et immuable (les chaînes, nombres et tuples fonctionnent, mais pas les listes).

# La valeur peut être de n'importe quel type Python : une chaîne, un nombre, une liste, un autre dictionnaire, ou même une fonction. Cette flexibilité fait des dictionnaires une structure de données extrêmement polyvalente.

# La paire clé-valeur est la brique de base : vous écrivez clé: valeur séparées par deux-points, et chaque paire est séparée des autres par une virgule.

# Pourquoi utiliser un dictionnaire ?
# Les listes et les dictionnaires sont les deux structures de données les plus utilisées en Python. Comprendre leurs différences vous permet de choisir la bonne structure selon votre besoin :


# Quand utiliser quoi ?

# Liste : collection ordonnée d'éléments similaires (liste de nombres, de noms...)
# Dictionnaire : objet avec des attributs nommés (utilisateur, configuration, réponse API...)
# Tuple : collection ordonnée immuable (coordonnées, valeurs de retour multiples...)
# Dictionnaire vide 

config = {}

#Dictionnaire avec des données

utilisateur = {
    "nom" : "Alice",
    "email" : "alice.durand@laposte.net",
    "age": 30,
    "actif" : True
    }


# SYNTAXE AVEC DICT()
# Le constructeur dict() crée un dictionnaire à 
# partir d'arguments nommés, d'une liste de tuples,
# ou de deux séquences combinées avec zip(). Pratique quand les données 
# viennent déjà sous forme de paires.

# À partir de mots-clés
utilisateur = dict(nom="Alice", email="alice.durand@laposte.net", age=30)

# À partir de tuples
utilisateur = dict([("nom", "Alice"), ("email", "alice.durand@laposte.net")])

# À partir de deux listes avec zip()
cles = ["nom", "email", "age"]
valeurs = ["Alice", "alice.durand@laposte.net", 30]
utilisateur = dict(zip(cles, valeurs))


# types de clés autorisés
# Les clés doivent être immuables (non modifiables). Pourquoi cette contrainte ? Python utilise un mécanisme appelé hachage pour retrouver instantanément une valeur à partir de sa clé. Si la clé pouvait changer après son insertion, Python ne saurait plus où retrouver la valeur associée.

# Types immuables utilisables comme clés :

# Clés valides
valide = {
    "texte": "valeur",      # str - le plus courant
    42: "valeur",           # int - utile pour les ID numériques
    3.14: "valeur",         # float - rare mais possible
    (1, 2): "valeur",       # tuple - utile pour les coordonnées
    True: "valeur"          # bool - peu recommandé (collision avec 1)
}

# Types mutables interdits :
# Clés invalides (TypeError: unhashable type)
# invalide = {
#     [1, 2]: "valeur",     # liste → utilisez un tuple (1, 2)
#     {"a": 1}: "valeur"    # dict → utilisez un tuple de tuples
# }

# Grille de jeu
plateau = {
    (0, 0): "X",
    (1, 1): "O",
    (2, 0): "X"
}
print(plateau[(1, 1)])  # "O"

# Accéder aux valeurs
# Accès direct avec []
# L'accès direct par crochets renvoie la valeur associée à une clé. C'est la syntaxe la plus rapide, mais elle lève une KeyError si la clé est absente.
utilisateur = {"nom": "Alice", "age": 30}

# Accès simple
nom = utilisateur["nom"]
print(nom)  # Alice

# Erreur si la clé n'existe pas
# ville = utilisateur["ville"]  # KeyError: 'ville'

# Accès sécurisé avec get()
# La méthode get() évite les erreurs KeyError :


utilisateur = {"nom": "Alice", "age": 30}

# Retourne None si la clé n'existe pas
ville = utilisateur.get("ville")
print(ville)  # None

# Retourne une valeur par défaut
ville = utilisateur.get("ville", "Non renseignée")
print(ville)  # Non renseignée

# La clé existe : retourne sa valeur
nom = utilisateur.get("nom", "Inconnu")
print(nom)  # Alice 

# Règle d'or

# Utilisez get() quand la clé peut être absente, notamment avec des données externes (fichiers, API, saisie utilisateur). Utilisez [] quand l'absence de clé est une erreur de programmation que vous voulez détecter.

# Vérifier l'existence d'une clé
# L'opérateur in teste si une clé est présente avant d'y accéder ou d'en ajouter une, ce qui évite les erreurs et les écrasements involontaires.

utilisateur = {"nom": "Alice", "age": 30}

# Avec 'in'
if "email" in utilisateur:
    print(utilisateur["email"])
else:
    print("Email non renseigné")

# Avec 'not in'
if "ville" not in utilisateur:
    utilisateur["ville"] = "Paris"

# Modifier un dictionnaire
# Une fois le dictionnaire créé, vous ajoutez, modifiez ou supprimez des éléments à tout moment : un dictionnaire est mutable. Les opérations ci-dessous couvrent les cas les plus fréquents, de l'ajout d'une clé unique à la mise à jour groupée.

# Ajouter une clé à un dictionnaire
# Pour ajouter une clé, affectez-lui une valeur : si la clé n'existe pas, elle est créée ; si elle existe déjà, sa valeur est remplacée.

utilisateur = {"nom": "Alice"}

# Ajouter une nouvelle clé
utilisateur["email"] = "alice.durand@laposte.net"
print(utilisateur)  # {'nom': 'Alice', 'email': 'alice.durand@laposte.net'}

# Modifier une clé existante
utilisateur["email"] = "alice.durand.pro@laposte.net"
print(utilisateur)  # {'nom': 'Alice', 'email': 'alice.durand.pro@laposte.net'}

# Ajouter plusieurs éléments avec update()
# La méthode update() ajoute ou met à jour plusieurs clés en une seule opération, à partir d'un autre dictionnaire. Les clés déjà présentes sont écrasées.

utilisateur = {"nom": "Alice"}

# Ajouter plusieurs clés
utilisateur.update({
    "email": "alice.durand@laposte.net",
    "age": 30,
    "ville": "Paris"
})
print(utilisateur)
# {'nom': 'Alice', 'email': 'alice.durand@laposte.net', 'age': 30, 'ville': 'Paris'}

# update() écrase les valeurs existantes
utilisateur.update({"age": 31})
print(utilisateur["age"])  # 31

# Définir une valeur par défaut avec setdefault()
# setdefault() ajoute une clé seulement si elle n'existe pas :

utilisateur = {"nom": "Alice"}

# La clé n'existe pas → elle est ajoutée
utilisateur.setdefault("ville", "Paris")
print(utilisateur)  # {'nom': 'Alice', 'ville': 'Paris'}

# La clé existe déjà → rien ne change
utilisateur.setdefault("ville", "Lyon")
print(utilisateur)  # {'nom': 'Alice', 'ville': 'Paris'}

# Supprimer des éléments
# Supprimer et récupérer avec pop()
# La méthode pop() supprime une clé et retourne sa valeur, ce qui permet de la récupérer au passage. Un second argument sert de valeur de repli si la clé est absente, pour éviter la KeyError.

utilisateur = {"nom": "Alice", "email": "alice.durand@laposte.net", "age": 30}

# Supprimer et récupérer la valeur
email = utilisateur.pop("email")
print(email)       # alice.durand@laposte.net
print(utilisateur) # {'nom': 'Alice', 'age': 30}

# Valeur par défaut si la clé n'existe pas
ville = utilisateur.pop("ville", "Aucune")
print(ville)  # Aucune (pas d'erreur)

# Supprimer avec del
# L'instruction del supprime une clé sans renvoyer sa valeur. Elle lève une KeyError si la clé n'existe pas : utilisez-la quand vous êtes sûr de sa présence.

utilisateur = {"nom": "Alice", "email": "alice.durand@laposte.net"}

# Supprimer une clé
del utilisateur["email"]
print(utilisateur)  # {'nom': 'Alice'}

# Erreur si la clé n'existe pas
# del utilisateur["ville"]  # KeyError

# Supprimer le dernier élément avec popitem()
# La méthode popitem() retire et retourne la dernière paire insérée, sous forme de tuple (clé, valeur). Utile pour vider un dictionnaire comme une pile (dernier entré, premier sorti).

utilisateur = {"nom": "Alice", "email": "alice.durand@laposte.net", "age": 30}

# Supprime et retourne la dernière paire ajoutée
derniere = utilisateur.popitem()
print(derniere)     # ('age', 30)
print(utilisateur)  # {'nom': 'Alice', 'email': 'alice.durand@laposte.net'}

# Vider le dictionnaire avec clear()
# La méthode clear() retire toutes les clés d'un coup tout en conservant le même objet en mémoire. Les autres variables qui référencent ce dictionnaire voient donc aussi le vidage.

utilisateur = {"nom": "Alice", "age": 30}

utilisateur.clear()
print(utilisateur)  # {}

# Parcourir un dictionnaire
# Contrairement aux listes où vous parcourez simplement les éléments dans l'ordre, un dictionnaire offre trois façons de le parcourir selon ce dont vous avez besoin : les clés seules, les valeurs seules, ou les deux ensemble. Choisir la bonne méthode rend votre code plus clair et plus efficace.

# Parcourir les clés
# Quand vous avez besoin uniquement des identifiants (par exemple, pour vérifier quelles clés existent ou pour construire une liste de noms de champs) :

utilisateur = {"nom": "Alice", "age": 30, "ville": "Paris"}

# Par défaut, itérer sur un dict parcourt ses clés
for cle in utilisateur:
    print(cle)
# nom
# age
# ville

# Explicitement avec keys() - même résultat, intention plus claire
for cle in utilisateur.keys():
    print(cle)
    
    # Cas d'usage : lister les champs d'une configuration, vérifier la présence de certaines clés, générer des rapports sur la structure des données.
    
# Parcourir les valeurs
# Quand vous n'avez pas besoin de savoir d'où vient chaque valeur (par exemple, pour calculer une somme ou trouver un maximum) :

utilisateur = {"nom": "Alice", "age": 30, "ville": "Paris"}

for valeur in utilisateur.values():
    print(valeur)
# Alice
# 30
# Paris

# Cas d'usage : calculer la somme des valeurs numériques, compter les occurrences, vérifier si une valeur particulière existe.

# Exemple pratique : calculer le total des scores
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
total = sum(scores.values())
print(f"Total: {total}")  # Total: 255

# Parcourir les paires clé-valeur (recommandé)
# C'est la méthode la plus courante car vous avez généralement besoin de contexte (la clé) pour traiter chaque valeur :

utilisateur = {"nom": "Alice", "age": 30, "ville": "Paris"}

for cle, valeur in utilisateur.items():
    print(f"{cle}: {valeur}")
# nom: Alice
# age: 30
# ville: Paris

# Cas d'usage : afficher un rapport formaté, transformer les données, filtrer selon des critères, exporter vers un autre format.

# Exemple pratique : formater pour l'affichage
config = {"host": "localhost", "port": 5432, "debug": True}
print("Configuration:")
for param, valeur in config.items():
    print(f"  • {param} = {valeur}")
    
#     Meilleure pratique

# Utilisez items() quand vous avez besoin à la fois de la clé et de la valeur. C'est plus lisible que d'accéder à la valeur via dict[cle] dans la boucle.

# Compréhensions de dictionnaire
# Les compréhensions permettent de créer des dictionnaires de manière concise et expressive. C'est l'une des fonctionnalités les plus élégantes de Python : une seule ligne remplace souvent 4-5 lignes de boucle.

# Syntaxe de base
# La syntaxe suit le pattern {clé: valeur for élément in iterable}. Lisez-la de droite à gauche : "pour chaque élément dans l'iterable, crée une paire clé-valeur".

# Version longue avec boucle
carres = {}
for x in range(1, 6):
    carres[x] = x**2

# Version compréhension (équivalente)
carres = {x: x**2 for x in range(1, 6)}
print(carres)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Décomposition : {x: x**2 for x in range(1, 6)}

# for x in range(1, 6) → parcourt les nombres 1, 2, 3, 4, 5
# x: x**2 → pour chaque x, crée la paire (x, x²)
# {} → le tout dans un dictionnaire

# Avec condition
# Une condition if placée en fin de compréhension agit comme un filtre : seuls les éléments qui la satisfont produisent une paire dans le dictionnaire final.

# Garder seulement les nombres pairs
carres_pairs = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(carres_pairs)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transformer un dictionnaire existant
# Une compréhension qui itère sur items() applique un calcul à chaque valeur (ou clé) pour produire un nouveau dictionnaire, sans modifier l'original.

prix_euros = {"pomme": 1.5, "banane": 0.8, "orange": 2.0}

# Convertir en dollars (taux 1.1)
prix_dollars = {fruit: prix * 1.1 for fruit, prix in prix_euros.items()}
print(prix_dollars)  # {'pomme': 1.65, 'banane': 0.88, 'orange': 2.2}

# Filtrer les produits chers
produits_chers = {f: p for f, p in prix_euros.items() if p >= 1.5}
print(produits_chers)  # {'pomme': 1.5, 'orange': 2.0}

# Inverser clés et valeurs
# En échangeant k et v dans la compréhension, vous inversez le dictionnaire (les valeurs deviennent des clés). Attention : des valeurs en double provoqueraient des collisions de clés.

original = {"a": 1, "b": 2, "c": 3}
inverse = {v: k for k, v in original.items()}
print(inverse)  # {1: 'a', 2: 'b', 3: 'c'}

# Créer à partir de deux listes
# La fonction zip() associe deux listes position par position ; la compréhension transforme ensuite ces couples en paires clé-valeur.

noms = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

# Avec zip() et compréhension
personnes = {nom: age for nom, age in zip(noms, ages)}
print(personnes)  # {'Alice': 30, 'Bob': 25, 'Charlie': 35}

# Dictionnaires imbriqués
# Les dictionnaires peuvent contenir d'autres dictionnaires, ce qui permet de représenter des structures de données complexes. C'est exactement ce que vous recevez quand vous interrogez une API REST ou lisez un fichier JSON.

# Cas d'usage typiques
# Réponses d'API : {"status": "ok", "data": {"user": {...}, "permissions": [...]}}
# Configuration : {"database": {"host": "...", "port": 5432}, "cache": {...}}
# Données relationnelles : employés par département, produits par catégorie

# Création et accès
# Voici un exemple concret : une base de données d'employés où chaque ID pointe vers les informations de l'employé.

employes = {
    "E001": {
        "nom": "Alice",
        "poste": "Développeuse",
        "salaire": 45000
    },
    "E002": {
        "nom": "Bob",
        "poste": "Designer",
        "salaire": 40000
    }
}

# Accéder à une valeur imbriquée
print(employes["E001"]["nom"])     # Alice
print(employes["E002"]["salaire"]) # 40000

# Modifier un élément imbriqué
# Pour modifier une valeur profonde, chaînez les crochets jusqu'au niveau voulu. Une affectation sur une clé absente à ce niveau la crée au passage.

# Augmenter le salaire d'Alice
employes["E001"]["salaire"] = 48000

# Ajouter un nouvel attribut
employes["E001"]["departement"] = "IT"

# Parcourir un dictionnaire imbriqué
# Deux boucles imbriquées suffisent : la première parcourt chaque enregistrement, la seconde ses attributs internes.

for id_employe, infos in employes.items():
    print(f"\n{id_employe}:")
    for attribut, valeur in infos.items():
        print(f"  {attribut}: {valeur}")

# E001:
#   nom: Alice
#   poste: Développeuse
#   salaire: 48000
#   departement: IT
# E002:
#   nom: Bob
#   poste: Designer
#   salaire: 40000

# Accès sécurisé aux structures imbriquées
# Enchaîner des get() avec un dictionnaire vide {} comme valeur par défaut évite la KeyError lorsqu'un niveau intermédiaire est absent.

# Risqué si une clé intermédiaire n'existe pas
# ville = employes["E003"]["adresse"]["ville"]  # KeyError

# Accès sécurisé chaîné
employe = employes.get("E003", {})
adresse = employe.get("adresse", {})
ville = adresse.get("ville", "Non renseignée")
print(ville)  # Non renseignée


# Fusionner des dictionnaires
# Fusionner des dictionnaires est une opération courante : combiner des configurations par défaut avec des options utilisateur, enrichir des données avec des informations complémentaires, ou consolider des résultats partiels.

# Python propose trois syntaxes selon vos besoins.

# Avec update() (modifie en place)
# Utilisez update() quand vous voulez modifier le dictionnaire original. C'est efficace en mémoire pour les gros dictionnaires.

base = {"nom": "Alice", "age": 30}
extra = {"ville": "Paris", "age": 31}

base.update(extra)
print(base)  # {'nom': 'Alice', 'age': 31, 'ville': 'Paris'}
# Attention : 'age' est écrasé par la valeur de 'extra'

# Cas d'usage : appliquer des options utilisateur sur une configuration par défaut.

# Avec l'opérateur ** (crée un nouveau dict)
# Le dépaquetage ** rassemble plusieurs dictionnaires dans un nouveau dictionnaire, sans modifier les originaux. Compatible avec toutes les versions de Python 3.

base = {"nom": "Alice", "age": 30}
extra = {"ville": "Paris", "email": "alice.durand@laposte.net"}

fusionne = {**base, **extra}
print(fusionne)
# {'nom': 'Alice', 'age': 30, 'ville': 'Paris', 'email': 'alice.durand@laposte.net'}

# Les dicts originaux ne sont pas modifiés
print(base)  # {'nom': 'Alice', 'age': 30}

# Avec l'opérateur | (Python 3.9+)
# Depuis Python 3.9, l'opérateur | fusionne deux dictionnaires en un nouveau, et |= réalise la fusion en place. C'est la syntaxe la plus lisible quand elle est disponible.

base = {"nom": "Alice", "age": 30}
extra = {"ville": "Paris"}

# Union (nouveau dictionnaire)
fusionne = base | extra
print(fusionne)  # {'nom': 'Alice', 'age': 30, 'ville': 'Paris'}

# Union en place
base |= extra
print(base)  # {'nom': 'Alice', 'age': 30, 'ville': 'Paris'}


# Méthodes essentielles : récapitulatif
# Voici les 10 méthodes que vous utiliserez le plus souvent. Gardez ce tableau sous le coude comme référence rapide :

# Méthode	        Description	            Exemple
# get(clé, défaut)	Accès sécurisé	        d.get("x", 0)
# keys()	        Vue des clés	        for k in d.keys()
# values()	        Vue des valeurs	        for v in d.values()
# items()	        Vue des paires	        for k, v in d.items()
# pop(clé, défaut)	Supprime et retourne	d.pop("x", None)
# popitem()	        Supprime la dernière paire	d.popitem()
# update(autre)	    Fusionne	            d.update({"a": 1})
# setdefault(clé,val)Ajoute si absent	    d.setdefault("x", 0)
# clear()	        Vide le dict	        d.clear()
# copy()	        Copie superficielle	    d2 = d.copy()

# Les plus utilisées au quotidien :

# get() : indispensable pour éviter les crashs quand vous traitez des données externes (API, fichiers JSON, formulaires). Toujours préférer d.get("clé", valeur_defaut) à d["clé"] quand la clé peut être absente.

# items() : la méthode de parcours standard. Dans 90% des cas où vous parcourez un dictionnaire, vous avez besoin à la fois de la clé et de la valeur.

# update() : parfait pour fusionner des configurations ou enrichir des données. Attention : les clés existantes sont écrasées par les nouvelles valeurs.

# pop() : utile pour extraire une valeur tout en la supprimant du dictionnaire (pattern courant dans les files de traitement).

# Différence entre keys(), values() et items()

# Ces trois méthodes retournent des vues (dict_keys, dict_values, dict_items), pas des listes. Ces vues sont dynamiques : si le dictionnaire change, la vue reflète les modifications. Pour obtenir une vraie liste, utilisez list(d.keys()).

d = {"a": 1, "b": 2}
cles = d.keys()
print(list(cles))  # ['a', 'b']

d["c"] = 3
print(list(cles))  # ['a', 'b', 'c'] - la vue est mise à jour !

# Bonnes pratiques
# Ces recommandations viennent de l'expérience collective de la communauté Python. Elles vous éviteront des bugs subtils et rendront votre code plus facile à maintenir.

# 1. Utilisez des clés descriptives
# Les abréviations font gagner quelques caractères mais rendent le code obscur. Dans 6 mois, vous ne vous souviendrez plus ce que signifie "n" ou "a".

# Peu lisible - économie de caractères mal placée
u = {"n": "Alice", "a": 30, "e": "alice.durand@laposte.net"}

# Clair et maintenable - le code se lit comme de la prose
utilisateur = {"nom": "Alice", "age": 30, "email": "alice.durand@laposte.net"}

# Astuce : utilisez des noms qui répondent à la question "qu'est-ce que cette valeur représente ?" plutôt que des raccourcis cryptiques.

# 2. Préférez get() pour les données externes
# Avec des données venues d'une API, d'un fichier ou d'un formulaire, une clé peut manquer sans que ce soit un bug. get() renvoie alors une valeur de repli plutôt que de faire planter le programme.

# Données venant d'une API ou d'un fichier
reponse = {"status": "ok", "data": {"user": "Alice"}}

# Robuste face aux champs manquants
user = reponse.get("data", {}).get("user", "Inconnu")

# 3. Ne modifiez pas un dict pendant son parcours
# Supprimer ou ajouter des clés pendant l'itération change la taille du dictionnaire en cours de route et déclenche une RuntimeError. Itérez plutôt sur une copie des clés.

scores = {"Alice": 10, "Bob": 5, "Charlie": 15}

# Dangereux : RuntimeError possible
# for nom in scores:
#     if scores[nom] < 10:
#         del scores[nom]

# Créez une copie ou une liste des clés
for nom in list(scores.keys()):
    if scores[nom] < 10:
        del scores[nom]
        
        
# 4. Utilisez les compréhensions pour les transformations simples
# Pour une transformation directe, une compréhension remplace une boucle de plusieurs lignes par une seule expression lisible. Réservez la boucle classique aux logiques complexes.

# Verbeux
resultat = {}
for x in range(5):
    resultat[x] = x ** 2

# Concis et expressif
resultat = {x: x**2 for x in range(5)}

# 5. Évitez l'imbrication excessive
# Au-delà de deux ou trois niveaux, un dictionnaire imbriqué devient difficile à lire et à maintenir. Une dataclass ou une structure aplatie exprime souvent mieux l'intention.

# Difficile à maintenir
data = {
    "niveau1": {
        "niveau2": {
            "niveau3": {
                "valeur": 42
            }
        }
    }
}

# Envisagez des classes ou aplatissez la structure
from dataclasses import dataclass

@dataclass
class Config:
    valeur: int = 42