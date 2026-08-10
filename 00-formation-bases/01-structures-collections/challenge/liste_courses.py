courses = []

# Boucle principale du programme
while True:

    # Affichage du menu
    print("\n=== Liste de courses ===")
    print("1. Ajouter un article")
    print("2. Afficher la liste")
    print("3. Supprimer un article")
    print("4. Quitter")

    # Récupération du choix utilisateur
    choix = input("\nVotre choix : ")

    # Ajouter un article
    if choix == "1":
        article = input("Nom de l'article : ")

        # Vérifie que l'utilisateur a bien saisi quelque chose
        if article.strip() != "":
            courses.append(article)
            print("✅ Article ajouté !")
        else:
            print("❌ Le nom de l'article ne peut pas être vide.")

    # Afficher la liste
    elif choix == "2":
        print("\n=== Articles ===")

        # Vérifie si la liste est vide
        if len(courses) == 0:
            print("🛒 La liste de courses est vide.")
        else:
            # enumerate permet d'avoir un numéro pour chaque article
            for numero, article in enumerate(courses, start=1):
                print(f"{numero}. {article}")

    # Supprimer un article
    elif choix == "3":

        # Vérifie si la liste contient des articles
        if len(courses) == 0:
            print("🛒 La liste de courses est vide.")
        else:
            # Affiche d'abord les articles disponibles
            print("\n=== Articles ===")
            for numero, article in enumerate(courses, start=1):
                print(f"{numero}. {article}")

            numero = input("Numéro de l'article à supprimer : ")

            # Vérifie que l'utilisateur a entré un nombre
            if numero.isdigit():
                numero = int(numero)

                # Vérifie que le numéro existe dans la liste
                if 1 <= numero <= len(courses):
                    article_supprime = courses.pop(numero - 1)
                    print(f"✅ {article_supprime} supprimé !")
                else:
                    print("❌ Numéro invalide.")
            else:
                print("❌ Veuillez entrer un numéro.")

    # Quitter le programme
    elif choix == "4":
        print("👋 Au revoir !")
        break

    # Cas où l'utilisateur entre un choix inconnu
    else:
        print("❌ Choix invalide, veuillez choisir entre 1 et 4.")