# 📊 Analyse du marché de l'emploi Tech & IA en France

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-En%20cours-orange)

> Projet d'analyse de données explorant les tendances du marché de l'emploi dans les domaines de la Data et de l'Intelligence Artificielle en France (2023-2024).

---

## 🎯 Objectifs

- Identifier les compétences les plus demandées en Data & IA
- Analyser la répartition géographique des offres d'emploi
- Comparer les types de contrats (stage, CDI, freelance)
- Visualiser l'évolution des tendances sur 12 mois

---

## 📁 Structure du projet

```
projet-emploi-tech-france/
│
├── data/
│   ├── raw/                  # Données brutes (non modifiées)
│   └── processed/            # Données nettoyées et transformées
│
├── notebooks/
│   ├── 01_exploration.ipynb  # Exploration initiale des données
│   ├── 02_cleaning.ipynb     # Nettoyage et preprocessing
│   └── 03_visualisation.ipynb# Visualisations et insights
│
├── src/
│   ├── data_loader.py        # Fonctions de chargement des données
│   ├── cleaning.py           # Fonctions de nettoyage
│   └── visualisation.py      # Fonctions de visualisation
│
├── outputs/
│   └── figures/              # Graphiques exportés
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation & Lancement

### 1. Cloner le repo
```bash
git clone https://github.com/ton-username/emploi-tech-france.git
cd emploi-tech-france
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer Jupyter
```bash
jupyter notebook
```

Ouvre ensuite les notebooks dans l'ordre : `01_exploration` → `02_cleaning` → `03_visualisation`

---

## 📊 Résultats & Insights clés

| Insight | Résultat |
|---|---|
| 🥇 Compétence la plus demandée | Python (78% des offres) |
| 🏙️ Ville avec le plus d'offres | Paris (62% des offres) |
| 📈 Secteur en plus forte croissance | IA Générative (+340% en 1 an) |
| 💼 Type de contrat dominant | CDI (54%), Stage (28%) |
| 🎓 Niveau d'études moyen requis | Bac+5 (67% des offres) |

---

## 🛠️ Stack technique

- **Python 3.10+**
- **Pandas** — manipulation et analyse des données
- **NumPy** — calculs numériques
- **Matplotlib / Seaborn** — visualisations statiques
- **Plotly** — visualisations interactives
- **Jupyter Notebook** — environnement d'analyse

---

## 📌 Dataset

Les données utilisées sont issues de :
- Simulation réaliste basée sur des données publiques (LinkedIn, Welcome to the Jungle, Indeed)
- Format CSV, ~2000 offres d'emploi

> ⚠️ Les données sont générées à des fins pédagogiques et reflètent des tendances réelles du marché.

---

## 🔮 Améliorations futures

- [ ] Scraping automatique des offres en temps réel
- [ ] Modèle de prédiction des salaires
- [ ] Dashboard interactif avec Streamlit
- [ ] Analyse des compétences par niveau d'expérience

---

## 👤 Auteur

**Ton Nom**
- LinkedIn : [linkedin.com/in/leonel-tagne-kamghem](https://linkedin.com/in/leonel-tagne-kamghem)
- GitHub : [github.com/leoneltagne](https://github.com/leoneltagne)

---



