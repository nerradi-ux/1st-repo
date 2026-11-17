# Calculateur de moyennes

Petit projet Python utilisé comme support de cours pour découvrir
comment travailler avec Claude sur un dépôt GitHub.

Le programme lit un fichier CSV de notes et affiche, pour chaque
étudiant, sa moyenne pondérée et sa mention.

## Utilisation

    python notes.py data/notes.csv

## Tests

    pip install pytest
    pytest

## Structure

- `notes.py` : le programme
- `test_notes.py` : les tests (incomplets)
- `data/notes.csv` : données d'exemple
- `EXERCICES.md` : exercices à faire avec Claude
