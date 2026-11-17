"""Calcul des moyennes d'une classe à partir d'un fichier CSV."""
import csv
import sys
from collections import defaultdict


def lire_notes(chemin):
    """Retourne un dictionnaire {étudiant: [(note, coefficient), ...]}."""
    resultats = defaultdict(list)
    with open(chemin, newline="", encoding="utf-8") as f:
        for ligne in csv.DictReader(f):
            note = float(ligne["note"])
            coef = float(ligne["coefficient"])
            resultats[ligne["etudiant"]].append((note, coef))
    return resultats


def moyenne_ponderee(notes):
    """Moyenne pondérée d'une liste de (note, coefficient)."""
    total = sum(note * coef for note, coef in notes)
    return total / len(notes)


def mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    if moyenne >= 14:
        return "Bien"
    if moyenne >= 12:
        return "Assez bien"
    if moyenne > 10:
        return "Passable"
    return "Ajourné"


def main():
    chemin = sys.argv[1] if len(sys.argv) > 1 else "data/notes.csv"
    for etudiant, notes in lire_notes(chemin).items():
        m = moyenne_ponderee(notes)
        print(f"{etudiant:10s} {m:5.2f}  {mention(m)}")


if __name__ == "__main__":
    main()
