fruits = {"pomme", "banane", "cerise"}   # set littéral
vide = set()                             # ensemble vide

faux_set = {}                            # ATTENTION : c'est un dict vide !
print(type(faux_set))                    # <class 'dict'>


# Le set vide s'écrit set(), jamais {}

# {} est réservé au dictionnaire vide. Pour un ensemble vide,
# il faut obligatoirement écrire set(). 
# C'est l'erreur la plus fréquente des débutants avec les sets.


# On crée souvent un set à partir d'une liste,
# ce qui la dédoublonne au passage :

notes = [12, 15, 12, 18, 15]
uniques = set(notes)
print(uniques)          # {18, 12, 15}

#Ajouter et supprimer des éléments
# Un set est modifiable. On ajoute avec add() 
# et on retire avec discard() ou remove().
# La différence entre les deux compte :

couleurs = {"rouge", "vert"}

couleurs.add("bleu")        # {'rouge', 'vert', 'bleu'}
couleurs.discard("jaune")   # absent : ne fait rien, aucune erreur
couleurs.remove("vert")     # présent : retiré
# couleurs.remove("jaune")  # absent : lève KeyError

# discard() ne lève jamais d'erreur si l'élément est absent :
# c'est le choix sûr.
# remove() lève KeyError si l'élément n'existe pas.
# pop() retire un élément arbitraire (l'ordre n'étant pas défini)
# , et clear() vide le set.


# les opérations d'ensemble
# C'est la vraie force des sets :
# combiner deux collections avec les opérateurs mathématiques.
# Chaque opérateur a une méthode équivalente, plus lisible 
# pour les débutants.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union : {1, 2, 3, 4, 5, 6}          (a.union(b))
print(a & b)   # intersection : {3, 4}               (a.intersection(b))
print(a - b)   # différence : {1, 2}                 (a.difference(b))
print(a ^ b)   # différence symétrique : {1, 2, 5, 6}

# Opérateur	 Méthode	          Résultat	        Signification
# a | b	     union	              tous les éléments	dans a ou b
# a & b	     intersection	      éléments communs	dans a et b
# a - b	     difference	          propres à a	    dans a mais pas b
# a ^ b	     symmetric_difference non partagés	    dans l'un ou l'autre, pas les deux

# On compare aussi deux ensembles avec <= (sous-ensemble) et >= (surensemble) :
print({1, 2} <= a)         # True : {1, 2} est inclus dans a
print(a.isdisjoint({9}))   # True : aucun élément commun

# Cas concret : comparer deux listes

serveurs_avant = {"web-1", "web-2", "db-1"}
serveurs_apres = {"web-1", "web-3", "db-1", "db-2"}

# ajoutes   = serveurs_apres - serveurs_avant   # {'web-3', 'db-2'}
# supprimes = serveurs_avant - serveurs_apres   # {'web-2'}
# communs   = serveurs_avant & serveurs_apres   # {'web-1', 'db-1'}

# Appartenance : le vrai atout des sets
# Tester si une valeur est présente avec in 
# est extrêmement rapide sur un set : 
# le temps est en moyenne constant (noté O(1)),
# quel que soit le nombre d'éléments.
# Sur une liste, la même opération parcourt
# les éléments un par un (O(n)).
import timeit

gros_set   = set(range(100_000))
grosse_liste = list(range(100_000))

t_set  = timeit.timeit(lambda: 99_999 in gros_set, number=1000)
t_list = timeit.timeit(lambda: 99_999 in grosse_liste, number=1000)

print(f"in set   : {t_set:.5f}s")    # ~0.00003 s
print(f"in liste : {t_list:.5f}s")   # ~0.43 s

# Les set comprehensions
# Comme les listes et les dictionnaires,
# les ensembles ont leur comprehension :
# la même syntaxe, mais entre accolades,
# avec dédoublonnage automatique.

mots = ["chat", "chien", "chat", "oiseau"]
initiales = {mot[0] for mot in mots}
print(initiales)      # {'c', 'o'}  → une seule fois chaque initiale

# frozenset : l'ensemble immuable
# Le frozenset est la version immuable du set :
# une fois créé, on ne peut plus le modifier.
# En échange, il devient hashable,
# ce qui permet de l'utiliser comme clé 
# de dictionnaire ou comme élément d'un autre set,
# chose impossible avec un set normal.

fs = frozenset([1, 2, 3])
# fs.add(4)   -> AttributeError : frozenset est figé

# utilisable comme clé de dictionnaire
resultats = {frozenset(["a", "b"]): "paire AB"}
print(resultats[frozenset(["b", "a"])])   # 'paire AB'

# À retenir
# Un set est une collection non ordonnée d'éléments uniques : il supprime les doublons.
# Le set vide s'écrit set(), jamais {} (qui crée un dictionnaire).
# On ajoute avec add, on retire avec discard (sûr) ou remove (lève KeyError si absent).
# Les opérations d'ensemble (|, &, -, ^) comparent deux collections sans boucle.
# Le test in est en temps constant sur un set, des milliers de fois plus rapide que sur une liste.
# La set comprehension {x for x in ...} construit un set en dédoublonnant.
# Le frozenset est immuable et hashable : utilisable comme clé de dict ou élément de set.
# Les éléments d'un set doivent être hashables : ni liste, ni dict à l'intérieur.



