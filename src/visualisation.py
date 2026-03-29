"""
visualisation.py
----------------
Fonctions de visualisation pour l'analyse du marché de l'emploi.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

# Style global
plt.rcParams.update({
    "font.family": "sans-serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

PALETTE = ["#1565C0", "#42A5F5", "#0D47A1", "#90CAF9", "#1E88E5", "#64B5F6"]


def plot_top_competences(df_comp, top_n=15, save_path=None):
    """
    Barplot horizontal des compétences les plus demandées.
    """
    top = (
        df_comp["competence"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )
    top.columns = ["competence", "count"]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(top["competence"][::-1], top["count"][::-1], color=PALETTE[0], alpha=0.85)

    # Valeurs sur les barres
    for bar, val in zip(bars, top["count"][::-1]):
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=9, color="#333")

    ax.set_xlabel("Nombre d'offres", fontsize=11)
    ax.set_title(f"🔑 Top {top_n} compétences les plus demandées", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlim(0, top["count"].max() * 1.15)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
        print(f"💾 Graphique sauvegardé : {save_path}")
    plt.show()


def plot_repartition_villes(df, save_path=None):
    """
    Camembert + barplot de la répartition des offres par ville.
    """
    villes = df["ville"].value_counts().head(8)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Pie chart
    wedges, texts, autotexts = ax1.pie(
        villes.values,
        labels=villes.index,
        autopct="%1.1f%%",
        colors=PALETTE * 2,
        startangle=140,
        pctdistance=0.82
    )
    for at in autotexts:
        at.set_fontsize(9)
    ax1.set_title("Répartition géographique", fontsize=12, fontweight="bold")

    # Barplot
    ax2.bar(villes.index, villes.values, color=PALETTE[0], alpha=0.8)
    ax2.set_xlabel("Ville", fontsize=11)
    ax2.set_ylabel("Nombre d'offres", fontsize=11)
    ax2.set_title("Offres par ville", fontsize=12, fontweight="bold")
    ax2.tick_params(axis="x", rotation=30)

    fig.suptitle("🗺️ Marché de l'emploi tech par ville", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    plt.show()


def plot_evolution_mensuelle(df, save_path=None):
    """
    Courbe d'évolution du nombre d'offres publiées par mois.
    """
    evol = df.groupby("mois").size().reset_index(name="nb_offres")

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(evol["mois"], evol["nb_offres"], marker="o", color=PALETTE[0],
            linewidth=2.5, markersize=6, markerfacecolor="white", markeredgewidth=2)
    ax.fill_between(evol["mois"], evol["nb_offres"], alpha=0.12, color=PALETTE[0])

    ax.set_xlabel("Mois", fontsize=11)
    ax.set_ylabel("Nombre d'offres", fontsize=11)
    ax.set_title("📈 Évolution mensuelle des offres d'emploi tech & IA", fontsize=13, fontweight="bold", pad=15)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    plt.show()


def plot_contrats(df, save_path=None):
    """
    Visualisation de la répartition par type de contrat.
    """
    contrats = df["type_contrat"].value_counts()
    colors = [PALETTE[0] if c == "Stage" else PALETTE[1] if c == "CDI" else "#B0BEC5" for c in contrats.index]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(contrats.index, contrats.values, color=colors, alpha=0.85, edgecolor="white", linewidth=1.5)

    for bar, val in zip(bars, contrats.values):
        pct = val / contrats.sum() * 100
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 8,
                f"{pct:.1f}%", ha="center", fontsize=10, fontweight="bold", color="#333")

    ax.set_ylabel("Nombre d'offres", fontsize=11)
    ax.set_title("💼 Répartition par type de contrat", fontsize=13, fontweight="bold", pad=15)

    # Légende personnalisée
    patch_stage = mpatches.Patch(color=PALETTE[0], label="Stage (priorité pour toi 🎯)")
    ax.legend(handles=[patch_stage], fontsize=10)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    plt.show()


def plot_heatmap_competences_villes(df_comp, save_path=None):
    """
    Heatmap : compétences vs villes principales.
    """
    top_comp = df_comp["competence"].value_counts().head(10).index
    top_villes = df_comp["ville"].value_counts().head(6).index

    pivot = (
        df_comp[df_comp["competence"].isin(top_comp) & df_comp["ville"].isin(top_villes)]
        .groupby(["ville", "competence"])
        .size()
        .unstack(fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="Blues", linewidths=0.5,
                linecolor="#E0E0E0", ax=ax, cbar_kws={"shrink": 0.8})

    ax.set_title("🗺️ Heatmap : Compétences demandées par ville", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Compétence", fontsize=11)
    ax.set_ylabel("Ville", fontsize=11)
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, bbox_inches="tight")
    plt.show()
