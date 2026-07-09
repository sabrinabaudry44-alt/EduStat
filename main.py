"""
main.py
Point d'entrée du projet EduStat

Charge les données depuis le fichier CSV,
construit les promotions,
lance les analyses
et affiche les rapports.
"""

# ======================================================
# IMPORTS
# ======================================================

from edustat import (
    Promotion,
    AnalyseurGenerale,
    AnalyseurTechno,
    AnalyseurPro,
)

from edustat.utils import charger_notes


# ======================================================
# FONCTION PRINCIPALE
# ======================================================

def main():
    print("=" * 70)
    print("                     PROJET EDUSTAT")
    print("=" * 70)

    # Chargement des données
    promotions = charger_notes("notes_brutes.csv")

    print(f"\n{len(promotions)} établissement(s) chargé(s)\n")

    # Affichage des établissements chargés
    for nom, promo in sorted(promotions.items()):
        print(f"{nom:<35} : {len(promo)} élève(s)")

    # ==================================================
    # Création d'une promotion par filière
    # ==================================================

    pool = {
        "Générale": Promotion(
            "Générale - Réseau",
            "Réseau EduStat",
            "Générale"
        ),

        "Technologique": Promotion(
            "Technologique - Réseau",
            "Réseau EduStat",
            "Technologique"
        ),

        "Professionnelle": Promotion(
            "Professionnelle - Réseau",
            "Réseau EduStat",
            "Professionnelle"
        )
    }

    # ==================================================
    # Regroupement des élèves par filière
    # ==================================================

    for promo in promotions.values():
        for eleve in promo:
            if eleve.filiere in pool:
                pool[eleve.filiere].ajouter(eleve)

    # ==================================================
    # Création des analyseurs
    # ==================================================

    analyseurs = [
        AnalyseurGenerale(pool["Générale"]),

        AnalyseurTechno(
            pool["Technologique"],
            matiere_dominante="physique"
        ),

        AnalyseurPro(pool["Professionnelle"])
    ]

    # ==================================================
    # RAPPORTS
    # ==================================================

    print("\n")
    print("=" * 70)
    print("               RAPPORTS DES FILIÈRES")
    print("=" * 70)

    for analyseur in analyseurs:
        analyseur.analyser().rapport()
        print("-" * 70)


# ======================================================
# LANCEMENT DU PROGRAMME
# ======================================================

if __name__ == "__main__":
    main()