# Créez un programme de gestion de contacts avec les fonctionnalités suivantes :

# Créer un dictionnaire de contacts (nom → infos)
# Ajouter un nouveau contact avec email et téléphone
# Rechercher un contact par nom
# Modifier le téléphone d'un contact
# Supprimer un contact
# Lister tous les contacts
# Structure attendue :

# dictionnaire de base
contacts = {
    "Alice": {"email": "alice.durand@laposte.net", "tel": "0612345678"},
    "Bob": {"email": "bob.lemaire@orange.fr", "tel": "0698765432"}
}


# 2. Fonction pour ajouter un contact
def ajouter_contact(nom, email, tel):
    if nom in contacts:
        print(f"Le contact {nom} existe déjà.")
        return False
    contacts[nom] = {"email": email, "tel": tel}
    print(f"Contact {nom} ajouté.")
    return True