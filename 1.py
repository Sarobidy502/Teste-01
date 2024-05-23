
def menu_principal():
    print("1. Se connecter à un compte existant")
    print("2. Créer un nouveau compte")
    choix = input("Choisissez une option : ")

    if choix == "1":
        verifier_identite()
    elif choix == "2":
        nouveau_compte = creer_compte()
        print("Bienvenue", nouveau_compte, "votre compte a été créé avec succès")
    else:
        print("Choix invalide. Veuillez sélectionner 1 ou 2.")
        menu_principal()

def creer_compte():
    nom = input("Entrez votre nom : ")
    email = input("Entrez votre adresse email : ")
    
    while '@' not in email:
        print("L'adresse email doit contenir le caractère '@'. Veuillez réessayer.")
        email = input("Entrez votre adresse email : ")

    mot_de_passe = input("Entrez votre mot de passe : ")

    compte_info = f"Nom : {nom}\nEmail : {email}\nMot de passe : {mot_de_passe}\n"

    with open('comptes.txt', 'a') as f:
        f.write(compte_info)
        f.write('\n')  
    return nom  

def verifier_identite():
    email_entre = input("Entrez votre adresse email : ")
    mot_de_passe_entre = input("Entrez votre mot de passe : ")

    with open('comptes.txt', 'r') as f:
        lignes = f.readlines()
        comptes = [lignes[i:i+4] for i in range(0, len(lignes), 4)]  

    compte_existe = False
    # fomba entina milaza fa ato miss no miss le compte jeren
    for compte in comptes:
        if email_entre in compte[1] and mot_de_passe_entre in compte[2]:
            print("Identité vérifiée. Vous êtes connecté.")
            compte_existe = True
            break

    if not compte_existe:
        print("Le compte n'existe pas. Voulez-vous créer un nouveau compte ? (Oui/Non)")
        reponse = input().lower()
        if reponse == "oui":
            nouveau_compte = creer_compte()
            print("Bienvenue", nouveau_compte, "votre compte a été créé avec succès")
        else:
            print("OK, retour au menu principal.")
            menu_principal()

menu_principal()


