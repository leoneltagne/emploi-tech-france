"""
cleaning.py
-----------
Fonctions de nettoyage et preprocessing des données.
"""

import pandas as pd
import numpy as np


def afficher_resume(df):
    """Affiche un résumé rapide du DataFrame."""
    print("=" * 50)
    print(f"📋 Dimensions : {df.shape[0]} lignes × {df.shape[1]} colonnes")
    print(f"📅 Période    : {df['date_publication'].min().date()} → {df['date_publication'].max().date()}")
    print(f"🔍 Valeurs manquantes :\n{df.isnull().sum()[df.isnull().sum() > 0]}")
    print("=" * 50)


def nettoyer_donnees(df):
    """
    Pipeline complet de nettoyage des données.

    Paramètres
    ----------
    df : pd.DataFrame
        Données brutes

    Retourne
    --------
    pd.DataFrame
        Données nettoyées
    """
    df = df.copy()

    # Supprimer les doublons
    nb_avant = len(df)
    df = df.drop_duplicates(subset=["titre", "entreprise", "date_publication"])
    nb_apres = len(df)
    print(f"✅ Doublons supprimés : {nb_avant - nb_apres}")

    # Nettoyer les espaces dans les colonnes texte
    for col in ["titre", "entreprise", "ville", "type_contrat"]:
        df[col] = df[col].str.strip()

    # Ajouter colonne mois et trimestre
    df["mois"] = df["date_publication"].dt.to_period("M").astype(str)
    df["trimestre"] = df["date_publication"].dt.to_period("Q").astype(str)

    # Catégoriser les titres
    df["categorie"] = df["titre"].apply(categoriser_titre)

    # Flag stage
    df["est_stage"] = df["type_contrat"] == "Stage"

    print(f"✅ Nettoyage terminé — {len(df)} offres valides")
    return df


def categoriser_titre(titre):
    """Catégorise un titre de poste en grande famille."""
    titre_lower = titre.lower()
    if "scientist" in titre_lower:
        return "Data Science"
    elif "analyst" in titre_lower or "bi" in titre_lower:
        return "Data Analysis"
    elif "engineer" in titre_lower and "ml" in titre_lower:
        return "ML Engineering"
    elif "engineer" in titre_lower:
        return "Data Engineering"
    elif "research" in titre_lower:
        return "Recherche IA"
    elif "stagiaire" in titre_lower or "stage" in titre_lower:
        return "Stage"
    else:
        return "Autre"


def extraire_competences(df):
    """
    Transforme la colonne 'competences' en DataFrame long (une ligne par compétence).

    Retourne
    --------
    pd.DataFrame
        Colonne 'competence' avec une ligne par compétence par offre
    """
    df_comp = df[["id", "competences", "type_contrat", "ville"]].copy()
    df_comp["competence"] = df_comp["competences"].str.split(", ")
    df_comp = df_comp.explode("competence")
    df_comp["competence"] = df_comp["competence"].str.strip()
    return df_comp
