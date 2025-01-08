# Saisie donnée
def saisir_etudiants():

    noms = []
    notes = []

    n = int(input("Combien d'étudiants souhaitez-vous saisir ? "))
    for i in range(n):
        nom = input(f"Nom de l'étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} (sur 20) : "))
        noms.append(nom)
        notes.append(note)

    return noms, notes


# Calcul de la moyenne
def calculer_moyenne(notes):

    return sum(notes) / len(notes)


# Echec/ reussi (note au dessus de 10)
def afficher_repartition(noms, notes):

    reussite = []
    echec = []

    for i in range(len(notes)):
        if notes[i] >= 10:
            reussite.append(noms[i])
        else:
            echec.append(noms[i])

    print("\nÉtudiants ayant réussi :", ", ".join(reussite))
    print("Étudiants en échec :", ", ".join(echec))


# Check meilleur note
def meilleure_note(noms, notes):

    meilleure_note = max(notes)
    indice = notes.index(meilleure_note)
    print(f"L’étudiant ayant la meilleure note est {noms[indice]} avec {meilleure_note}.")


# Le programme principal avec l'appel des différent fonctions
def main():

    noms, notes = saisir_etudiants()

    moyenne = calculer_moyenne(notes)
    print(f"\nLa moyenne de la classe est de {moyenne:.2f}.")

    afficher_repartition(noms, notes)

    meilleure_note(noms, notes)


# Exécution du programme principal
if __name__ == "__main__":
    main()
