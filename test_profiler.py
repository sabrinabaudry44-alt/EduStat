# Challenge 5

"""
test_profiler.py

Teste le DataProfiler sur un DataFrame générique.
"""

import pandas as pd

from edustat import DataProfiler


# ==========================================================
# Création d'un DataFrame de test
# ==========================================================

df = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "Ville": ["Paris", "Lyon", "Marseille"],
})


# ==========================================================
# Création du profiler
# ==========================================================

profiler = DataProfiler(df, nom="Exemple")


# ==========================================================
# Tests
# ==========================================================

profiler.profiler().rapport()

print("\n" + "=" * 60)
print("TESTS")
print("=" * 60)

print(f"Nombre de lignes : {len(profiler)}")
print(f"Doublons : {profiler.doublons()}")

print("\nTypes des colonnes :")
print(profiler.types_colonnes())

print("\nStatistiques :")
print(profiler.stats_numeriques())