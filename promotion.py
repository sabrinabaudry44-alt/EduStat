from modeles import Promotion, Eleve

promo = Promotion(
    nom="Promotion Data IA 2026",
    etablissement="Wild Code School",
    filiere="Data"
)

promo.ajouter(Eleve(
    "E001", "Lucas", "Martin", "Data",
    maths=18, francais=15, anglais=16,
    histoire=14, svt=17, physique=18
))

promo.ajouter(Eleve(
    "E002", "Emma", "Durand", "Data",
    maths=14, francais=13, anglais=15,
    histoire=12, svt=14, physique=13
))

promo.ajouter(Eleve(
    "E003", "Nathan", "Bernard", "Data",
    maths=9, francais=11, anglais=10,
    histoire=8, svt=9, physique=10
))

promo.ajouter(Eleve(
    "E004", "Chloé", "Petit", "Data",
    maths=19, francais=18, anglais=17,
    histoire=16, svt=19, physique=20
))

promo.ajouter(Eleve(
    "E005", "Lina", "Robert", "Data",
    maths=11, francais=12, anglais=13,
    histoire=11, svt=10, physique=12
))

promo.ajouter(Eleve(
    "E006", "Hugo", "Moreau", "Data",
    maths=6, francais=8, anglais=9,
    histoire=7, svt=8, physique=6
))