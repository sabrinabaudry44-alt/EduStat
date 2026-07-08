    # Challenge 3

from modeles import Promotion


class AnalyseurPromotion:
    SEUIL_ADMISSION = 10.0

    def __init__(self, promotion):
        self.promotion = promotion
        self._stats = {}

    def analyser(self):
        self._stats = {
            "nb_eleves": len(self.promotion),
            "moyenne": self.promotion.moyenne_generale(),
            "taux_admission": self.promotion.taux_admission(
                self.SEUIL_ADMISSION
            ),
        }
        return self

    def rapport(self):
        print("\n===== Rapport =====")
        print(f"Élèves           : {self._stats['nb_eleves']}")
        print(f"Moyenne          : {self._stats['moyenne']}/20")
        print(f"Taux admission   : {self._stats['taux_admission']} %")

    def top_n(self, n=3):
        return self.promotion.classement()[:n]


# ==========================================================
# Filière Générale
# ==========================================================

class AnalyseurGenerale(AnalyseurPromotion):

    SEUIL_ADMISSION = 10.0

    def analyser(self):
        super().analyser()

        maths = []
        sciences = []
        lettres = []

        for e in self.promotion:

            # Maths
            if e.maths is not None:
                maths.append(e.maths)

            # Sciences = moyenne(SVT, Physique)
            notes_sciences = []

            if e.svt is not None:
                notes_sciences.append(e.svt)

            if e.physique is not None:
                notes_sciences.append(e.physique)

            if notes_sciences:
                sciences.append(sum(notes_sciences) / len(notes_sciences))

            # Lettres = moyenne(Français, Histoire)
            notes_lettres = []

            if e.francais is not None:
                notes_lettres.append(e.francais)

            if e.histoire is not None:
                notes_lettres.append(e.histoire)

            if notes_lettres:
                lettres.append(sum(notes_lettres) / len(notes_lettres))

        self._stats["moy_maths"] = round(sum(maths) / len(maths), 2)

        self._stats["moy_sciences"] = round(
            sum(sciences) / len(sciences), 2
        )

        self._stats["moy_lettres"] = round(
            sum(lettres) / len(lettres), 2
        )

        return self

    def rapport(self):
        print("\n===== Filière Générale =====")
        super().rapport()
        print(f"Moyenne Maths      : {self._stats['moy_maths']}/20")
        print(f"Moyenne Sciences   : {self._stats['moy_sciences']}/20")
        print(f"Moyenne Lettres    : {self._stats['moy_lettres']}/20")


# ==========================================================
# Filière Technologique
# ==========================================================

class AnalyseurTechno(AnalyseurPromotion):

    SEUIL_ADMISSION = 10.0

    def __init__(self, promotion, matiere_dominante="maths"):
        super().__init__(promotion)
        self.matiere_dominante = matiere_dominante

    def analyser(self):
        super().analyser()

        notes = []

        for e in self.promotion:

            note = getattr(e, self.matiere_dominante)

            if note is not None:
                notes.append(note)

        self._stats["moy_matiere_dominante"] = (
            round(sum(notes) / len(notes), 2)
            if notes else None
        )

        return self

    def rapport(self):
        print(f"\n===== Filière Technologique =====")
        super().rapport()
        print(
            f"Moyenne {self.matiere_dominante} : "
            f"{self._stats['moy_matiere_dominante']}/20"
        )


# ==========================================================
# Filière Professionnelle
# ==========================================================

class AnalyseurPro(AnalyseurPromotion):

    SEUIL_ADMISSION = 8.0

    def analyser(self):
        super().analyser()

        # Recalcul avec le seuil de 8
        self._stats["taux_admission"] = (
            self.promotion.taux_admission(self.SEUIL_ADMISSION)
        )

        return self

    def rapport(self):
        print(
            f"\n===== Filière Professionnelle "
            f"(seuil = {self.SEUIL_ADMISSION}) ====="
        )
        super().rapport()