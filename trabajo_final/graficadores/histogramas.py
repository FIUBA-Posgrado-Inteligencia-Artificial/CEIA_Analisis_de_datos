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
