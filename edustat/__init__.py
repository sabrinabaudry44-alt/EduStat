# Challenge 4

"""
Package EduStat

Réexporte les principales classes du projet.
"""

# ==========================
# MODÈLES
# ==========================

from .modeles import Eleve, Promotion

# ==========================
# ANALYSEURS
# ==========================

from .analyseurs import (
    AnalyseurPromotion,
    AnalyseurGenerale,
    AnalyseurTechno,
    AnalyseurPro,
)

# ==========================
# UTILITAIRES
# ==========================

from .utils import charger_notes