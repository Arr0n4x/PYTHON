# Scénario
# Vous êtes responsable de la gestion des informations des étudiants d'une classe. Chaque étudiant possède des informations immuables telles que son nom, son prénom, son âge et sa note finale. Vous allez suivre chaque étape pour construire votre programme en utilisant des tuples pour chaque étudiant et un dictionnaire pour stocker tous les étudiants.

# Étapes de l'exercice
# Traitez les huit étapes dans l'ordre : chacune réutilise la structure construite par la précédente. L'étape 6 est la plus instructive, car elle vous confronte à l'immuabilité : modifier une note impose de reconstruire le tuple entier.

# Créer un tuple pour un étudiant






# Rechercher un étudiant par nom

# Demandez à l'utilisateur de saisir le nom d'un étudiant.
# Parcourez classe pour vérifier si un étudiant avec ce nom existe.
# Si l'étudiant est trouvé, affichez toutes ses informations. Sinon, affichez un message indiquant que l'étudiant n'a pas été trouvé.
# Mettre à jour la note d'un étudiant

# Demandez à l'utilisateur de saisir l'identifiant d'un étudiant (par exemple, "Etudiant1").
# Puis demandez-lui de saisir une nouvelle note.
# Mettez à jour la note finale en recréant le tuple correspondant pour l'étudiant dans le dictionnaire classe.
# Supprimer un étudiant de la classe

# Demandez à l'utilisateur de saisir l'identifiant d'un étudiant à supprimer (par exemple, "Etudiant2").
# Supprimez l'étudiant correspondant du dictionnaire classe.
# Afficher les étudiants ayant une note supérieure à une valeur donnée

# Demandez à l'utilisateur de saisir une note minimale.
# Parcourez classe et affichez les informations de tous les étudiants ayant une note finale supérieure ou égale à cette valeur.


# Créez un tuple pour un étudiant contenant les informations suivantes : nom, prénom, âge et note finale. Remplissez-le avec un exemple de votre choix.
# Créer une liste d'étudiants sous forme de dictionnaire
from collections import namedtuple

Etudiant = namedtuple("Etudiant", ["nom", "prenom", "age","Note_final"])

# Créez un dictionnaire vide appelé classe pour stocker les informations de plusieurs étudiants.
# Ajoutez le tuple de l’étudiant que vous avez créé dans la première étape en lui assignant un identifiant unique (comme "Etudiant1").
# Ajouter plusieurs étudiants à la classe

Etudiant1 = Etudiant("MARTIN","Luc",20,15.5)

classe = {}
classe ["Etudiant1"] = Etudiant1

etudiant2 = Etudiant("Martin", "Bob", 22, 18)
etudiant3 = Etudiant("Leclerc", "Claire", 19, 13)

classe["Etudiant2"] = etudiant2
classe["Etudiant3"] = etudiant3

for identifiant, etudiant in classe.items():
    print(f"{identifiant}:")
    print(f"  Nom : {etudiant[0]}")
    print(f"  Prénom : {etudiant[1]}")
    print(f"  Âge : {etudiant[2]}")
    print(f"  Note finale : {etudiant[3]}")
    
