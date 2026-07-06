from modeles import Eleve

e1 = Eleve("E001","Lucas","Martin","Lycée Victor Hugo","Générale",
 maths=14.5, francais=13.0, anglais=16.0,
 histoire=12.5, svt=15.0, physique=14.0)
e2 = Eleve("E003","Nathan","Leroy","Lycée Victor Hugo","Générale",
 maths=9.0, francais=11.0, anglais=10.5,
 histoire=8.0, svt=9.5, physique=8.5)
e3 = Eleve("E007","Axel","Robert","Lycée Victor Hugo","Technologique",
 maths=11.0, francais=10.0, anglais=12.0,
 histoire=9.5, svt=11.5, physique=12.5)
e4 = Eleve("E013","Théo","Dupont","Lycée Victor Hugo","Professionnelle",
 maths=10.0, francais=11.5, anglais=9.0,
 histoire=10.5, svt=None, physique=10.0)

for e in [e1, e2, e3, e4]:
    e.bulletin()
    print(f" Mention (seuil 12) : {e.est_admis(seuil=12.0)}\n")

# Élèves dont la note de maths dépasse la moyenne générale
print("Maths > moyenne générale :")
for e in [e1, e2, e3, e4]:
    if e.maths is not None and e.moyenne() is not None and e.maths > e.moyenne():
        print(f" {e.prenom} {e.nom} — maths={e.maths}, moy={e.moyenne()}")
