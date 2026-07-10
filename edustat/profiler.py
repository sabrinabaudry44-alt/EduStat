# Challenge 5 - EduStat

"""
profiler.py

Contient :
- DataProfiler (générique)
- ProfileurNotes (spécialisé)
"""

import pandas as pd


# ==========================================================
# CLASSE GÉNÉRIQUE
# ==========================================================

class DataProfiler:

    def __init__(self, df, nom="DataFrame"):

        if not isinstance(df, pd.DataFrame):
            raise TypeError("df doit être un pandas.DataFrame")

        self._df = df.copy()
        self.nom = nom
        self._profil = {}

    def __len__(self):
        return len(self._df)

    def __repr__(self):

        return (
            f"DataProfiler("
            f"nom={self.nom!r}, "
            f"lignes={len(self)}, "
            f"colonnes={len(self._df.columns)})"
        )

    @classmethod
    def depuis_csv(cls, chemin, separateur=";", nom="CSV"):

        df = pd.read_csv(
            chemin,
            sep=separateur,
            dtype=str
        )

        return cls(df, nom)

    def types_colonnes(self):

        return self._df.dtypes

    def valeurs_manquantes(self):

        return self._df.isna().sum()

    def doublons(self):

        return self._df.duplicated().sum()

    def stats_numeriques(self):

        return self._df.describe(include="all")

    def profiler(self):

        self._profil = {

            "lignes": len(self._df),

            "colonnes": len(self._df.columns),

            "doublons": self.doublons(),

            "manquantes": self.valeurs_manquantes()

        }

        return self

    def rapport(self):

        print("\n" + "=" * 60)
        print(f"PROFIL : {self.nom}")
        print("=" * 60)

        print(f"Nombre de lignes : {self._profil['lignes']}")
        print(f"Nombre de colonnes : {self._profil['colonnes']}")
        print(f"Nombre de doublons : {self._profil['doublons']}")

        print("\nValeurs manquantes :")
        print(self._profil["manquantes"])

    def exporter(self, chemin):

        resume = pd.DataFrame({

            "Indicateur": [

                "Lignes",

                "Colonnes",

                "Doublons"

            ],

            "Valeur": [

                self._profil["lignes"],

                self._profil["colonnes"],

                self._profil["doublons"]

            ]

        })

        resume.to_csv(
            chemin,
            sep=";",
            index=False
        )

        print(f"\nProfil exporté dans : {chemin}")


# ==========================================================
# CLASSE SPÉCIALISÉE
# ==========================================================

class ProfileurNotes(DataProfiler):

    def profiler(self):

        super().profiler()

        notes = [
            "maths",
            "francais",
            "anglais",
            "histoire",
            "svt",
            "physique"
        ]

        moyennes = {}

        for matiere in notes:

            valeurs = pd.to_numeric(
                self._df[matiere],
                errors="coerce"
            )

            moyennes[matiere] = round(
                valeurs.mean(),
                2
            )

        self._profil["moyennes"] = moyennes

        # moyenne par filière

        df = self._df.copy()
        
        from .modeles import Eleve

        df["filiere"] = df["filiere"].apply(Eleve.normaliser_filiere)

        for col in notes:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

        df["moyenne"] = df[notes].mean(axis=1)

        self._profil["filiere"] = (
            df.groupby("filiere")["moyenne"]
              .mean()
              .round(2)
        )

        self._profil["etablissement"] = (
            df.groupby("etablissement")["moyenne"]
              .mean()
              .round(2)
        )

        return self

    def rapport(self):

        super().rapport()

        print("\n" + "=" * 60)
        print("MOYENNES PAR MATIÈRE")
        print("=" * 60)

        for matiere, moyenne in self._profil["moyennes"].items():

            print(f"{matiere:<12} : {moyenne}")

        print("\n" + "=" * 60)
        print("MOYENNES PAR FILIÈRE")
        print("=" * 60)

        print(self._profil["filiere"])

        print("\n" + "=" * 60)
        print("MOYENNES PAR ÉTABLISSEMENT")
        print("=" * 60)

        print(self._profil["etablissement"])