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

