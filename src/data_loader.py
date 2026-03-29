"""
data_loader.py
--------------
Fonctions pour générer et charger les données du projet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generer_dataset_emploi(n=2000, seed=42):
    """
    Génère un dataset simulé d'offres d'emploi tech en France.
    
    Paramètres
    ----------
    n : int
        Nombre d'offres à générer
    seed : int
        Graine aléatoire pour la reproductibilité

    Retourne
    --------
    pd.DataFrame
        Dataset complet des offres d'emploi
    """
    np.random.seed(seed)
    random.seed(seed)

    # --- Définition des variables ---
    titres = [
        "Data Scientist", "Data Analyst", "ML Engineer",
        "Data Engineer", "AI Researcher", "Business Intelligence Analyst",
        "NLP Engineer", "Computer Vision Engineer", "MLOps Engineer",
        "Stagiaire Data Science", "Stagiaire Data Analyst", "Stagiaire ML"
    ]

    entreprises = [
        "Mistral AI", "Dataiku", "Owkin", "Hugging Face", "Shift Technology",
        "PhotoRoom", "Ekimetrics", "Younited", "Kayrros", "Withings",
        "BlaBlaCar", "Doctolib", "Alan", "Contentsquare", "Swile",
        "Qonto", "Payfit", "Back Market", "ManoMano", "Mirakl"
    ]

    villes = ["Paris", "Lyon", "Bordeaux", "Toulouse", "Nantes",
              "Grenoble", "Lille", "Marseille", "Rennes", "Strasbourg"]
    poids_villes = [0.62, 0.10, 0.06, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.01]

    contrats = ["CDI", "Stage", "CDD", "Freelance", "Alternance"]
    poids_contrats = [0.54, 0.28, 0.08, 0.06, 0.04]

    niveaux = ["Bac+3", "Bac+4", "Bac+5", "Bac+8 (PhD)"]
    poids_niveaux = [0.10, 0.23, 0.57, 0.10]

    competences_pool = [
        "Python", "SQL", "Machine Learning", "Deep Learning", "TensorFlow",
        "PyTorch", "Pandas", "Spark", "Airflow", "Docker",
        "Kubernetes", "dbt", "Tableau", "Power BI", "Scikit-learn",
        "NLP", "Computer Vision", "LLM", "RAG", "Hugging Face",
        "Azure", "AWS", "GCP", "Git", "API REST"
    ]

    secteurs = [
        "FinTech", "HealthTech", "RetailTech", "LegalTech",
        "EdTech", "MarTech", "DeepTech", "SaaS", "E-commerce"
    ]

    # --- Génération des dates sur 12 mois ---
    date_fin = datetime(2024, 6, 30)
    date_debut = datetime(2023, 7, 1)
    delta = (date_fin - date_debut).days

    dates = [date_debut + timedelta(days=random.randint(0, delta)) for _ in range(n)]

    # --- Salaires simulés ---
    def generer_salaire(contrat, titre):
        if contrat == "Stage":
            return round(np.random.uniform(600, 1200), 0)
        elif contrat == "Alternance":
            return round(np.random.uniform(1000, 1800), 0)
        elif "Researcher" in titre or "PhD" in titre:
            return round(np.random.uniform(55000, 90000), 0)
        elif contrat == "Freelance":
            return round(np.random.uniform(400, 800), 0)  # TJM
        else:
            return round(np.random.uniform(35000, 75000), 0)

    # --- Construction du DataFrame ---
    rows = []
    for i in range(n):
        titre = random.choice(titres)
        contrat = np.random.choice(contrats, p=poids_contrats)
        ville = np.random.choice(villes, p=poids_villes)
        nb_comp = random.randint(3, 7)
        comps = random.sample(competences_pool, nb_comp)
        salaire = generer_salaire(contrat, titre)

        rows.append({
            "id": i + 1,
            "date_publication": dates[i].strftime("%Y-%m-%d"),
            "titre": titre,
            "entreprise": random.choice(entreprises),
            "ville": ville,
            "type_contrat": contrat,
            "secteur": random.choice(secteurs),
            "niveau_requis": np.random.choice(niveaux, p=poids_niveaux),
            "competences": ", ".join(comps),
            "salaire": salaire,
            "teletravail": random.choice(["Oui", "Non", "Hybride"]),
            "experience_requise_ans": random.choice([0, 0, 1, 2, 3, 5])
        })

    df = pd.DataFrame(rows)
    df["date_publication"] = pd.to_datetime(df["date_publication"])
    return df


def charger_donnees(chemin=None):
    """
    Charge les données depuis un fichier CSV ou génère un dataset.

    Paramètres
    ----------
    chemin : str ou None
        Chemin vers un fichier CSV. Si None, génère les données.

    Retourne
    --------
    pd.DataFrame
    """
    if chemin:
        return pd.read_csv(chemin, parse_dates=["date_publication"])
    else:
        print("ℹ️  Aucun fichier fourni — génération du dataset simulé...")
        return generer_dataset_emploi()
