import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograma(
    data, column, figsize=(6, 3), bins=15, kde=True, mvd=True, shade=True, snk=False
):
    skewness = (data[column]).skew()
    kurtosis = (data[column]).kurt()
    media = (data[column]).mean()
    var = (data[column]).var()
    std = (data[column]).std()
    plt.figure(figsize=figsize)
    plt.grid(axis="y")
    sns.histplot(data[column], bins=bins, kde=kde)
    if snk:
        plt.figtext(0.7, 0.8, f"Asimetría: {skewness:.2f}", fontsize=10, color="blue")
        plt.figtext(0.715, 0.73, f"Curtosis: {kurtosis:.2f}", fontsize=10, color="blue")
        plt.axvline(media, color="red", linestyle="--", label="Media")

    # Sombreado
    if mvd and shade:
        plt.axvspan(media - std, media + std, alpha=0.1, color="orange", label="±1 Std")
        plt.axvline(media + std, color="orange", linestyle=":", label="+1 Std")
        plt.axvline(media - std, color="orange", linestyle=":", label="-1 Std")
        plt.figtext(0.15, 0.80, f"Media: {media:.2f}", fontsize=10, color="red")
        plt.figtext(0.15, 0.73, f"Var:   {var:.2f}", fontsize=10, color="red")
        plt.figtext(0.15, 0.66, f"Std:   {std:.2f}", fontsize=10, color="orange")

    plt.title(f"Variable: {column}")
    plt.xlabel(f"{column}")
    plt.ylabel("Frecuencia")
    plt.show()

    return

def cuartiles(variable):
    Q1 = variable.quantile(0.25)
    Q2 = variable.quantile(0.50)  # Percentile 50 - Equivalente a la mediana
    Q3 = variable.quantile(0.75)
    return Q1, Q2, Q3

def plot_pie(data, column, ax=None, startangle=90, palette='pastel', title=None):
    counts = data[column].value_counts()
    total = counts.sum()
    
    # Identificar categorías menores al 10%
    threshold = 0.1 * total
    mask = counts < threshold
    
    if mask.any():
        others_count = counts[mask].sum()
        counts = counts[~mask].copy()
        # Sumar a 'Other' si ya existe, o crearla
        if 'Other' in counts:
            counts['Other'] += others_count
        else:
            counts['Other'] = others_count
        # Re-ordenar para que el gráfico sea estético
        counts = counts.sort_values(ascending=False)

    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 3))
    
    ax.pie(
        counts,
        labels=counts.index,
        autopct='%1.1f%%',
        startangle=startangle,
        colors=sns.color_palette(palette, n_colors=len(counts))
    )
    ax.set_title(title if title else f'Distribución de "{column}"')
    ax.axis('equal')
