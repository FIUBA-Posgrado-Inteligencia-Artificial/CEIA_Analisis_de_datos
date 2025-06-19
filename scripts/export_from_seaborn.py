import seaborn as sns
import pandas as pd
import argparse

def export_from_seaborn(dataset_name: str, destination_path: str = "../datasets/") -> None:
    """
    Exporta un dataset desde seaborn a un archivo CSV.
    """
    # Cargar el dataset de Titanic
    df = sns.load_dataset(dataset_name)

    try:
        df = sns.load_dataset(dataset_name)
    except Exception as e:
        print(f"Error al cargar el dataset '{dataset_name}': {e}")
    
    # Exportar CSV
    df.to_csv(f"{destination_path}{dataset_name}.csv", index=False)
    print(f"Dataset '{dataset_name}' exportado a {destination_path}{dataset_name}.csv")
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exporta un dataset de Seaborn a CSV.")
    parser.add_argument("dataset_name", help="Nombre del dataset en seaborn (por ejemplo: titanic, iris, penguins)")
    parser.add_argument("--destination_path", default="../datasets/", help="Ruta destino (por defecto: ../datasets/)")
    
    args = parser.parse_args()
    export_from_seaborn(args.dataset_name, args.destination_path)