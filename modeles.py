    # Challenge 1
class Eleve:
    def __init__(self, identifiant, prenom, nom, etablissement, filiere,
    maths=None, francais=None, anglais=None,
    histoire=None, svt=None, physique=None):
        self.identifiant = identifiant
        self.prenom = prenom
        self.nom = nom # type: ignore
        self.etablissement = etablissement
        self.filiere = filiere
        self.maths = maths
        self.francais = francais
        self.anglais = anglais # type: ignore
        self.histoire = histoire
        self.svt = svt
        self.physique = physique

    def notes(self):
        toutes = [self.maths, self.francais, self.anglais,
        self.histoire, self.svt, self.physique]
        return [n for n in toutes if n is not None]

    def moyenne(self):
        n = self.notes()
        if not n:
            return None
        return round(sum(n) / len(n), 2)
    
    def est_admis(self, seuil=10.0):
        moy = self.moyenne()
        return moy is not None and moy >= seuil
    
    def bulletin(self):
        moy = self.moyenne()
        statut = "Admis" if self.est_admis() else "Non admis"
        print(f"-- {self.prenom} {self.nom} ({self.filiere}) --")
        print(f" Moyenne : {moy if moy is not None else 'N/A'}/20 | {statut}")

    def __repr__(self):
        return (f"Eleve(id={self.identifiant!r}, "
        f"nom={self.nom!r}, "
        f"filiere={self.filiere!r})")
    
    def __str__(self):
        moy = self.moyenne()
        moy_str = f"{moy}/20" if moy is not None else "N/A"
        return f"{self.prenom} {self.nom} | {self.filiere} | moy. {moy_str}"
    
    def __eq__(self, other):
        if not isinstance(other, Eleve):
            return NotImplemented
        return self.identifiant == other.identifiant
    
    def __lt__(self, other):
        moy_self = self.moyenne() or 0
        moy_other = other.moyenne() or 0
        return moy_self < moy_other

class Promotion:
    def __init__(self, nom, etablissement, filiere):
        self.nom = nom
        self.etablissement = etablissement
        self.filiere = filiere
        self._eleves = []

    def __repr__(self):
        return (f"Promotion({self.nom}, "
        f"filiere={self.filiere!r}, "
        f"{len(self)} élève(s))")
    
    def __str__(self):
        return f"[{self.etablissement}] {self.nom} — {len(self)} élève(s)"
    
    def __len__(self):
        return len(self._eleves)
    
    def __iter__(self):
        return iter(self._eleves)
    
    def __contains__(self, eleve):
        return eleve in self._eleves
    
    def ajouter(self, eleve):
        self._eleves.append(eleve)

    def moyenne_generale(self):
        moyennes = [e.moyenne() for e in self if e.moyenne() is not None]
        if not moyennes:
            return None
        return round(sum(moyennes) / len(moyennes), 2)
    
    def taux_admission(self, seuil=10.0):
        avec_notes = [e for e in self if e.moyenne() is not None]
        if not avec_notes:
            return None
        admis = sum(1 for e in avec_notes if e.est_admis(seuil))
        return round(admis / len(avec_notes) * 100, 1)
    
    def classement(self):
        return sorted(
    [e for e in self if e.moyenne() is not None],
    reverse=True
    )

    def rapport(self):
        print(f"\n{'='*52}")
        print(f" {self}")
        print(f"{'='*52}")
        print(f" Moyenne générale : {self.moyenne_generale()}/20")
        print(f" Taux d'admission : {self.taux_admission()}%")
        print(f"\n Top 3 :")
        for rang, eleve in enumerate(self.classement()[:3], 1):
           print(f" {rang}. {eleve}")