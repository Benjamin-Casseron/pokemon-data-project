from pathlib import Path
import pandas as pd
from utils.io import read_json, write_csv, list_json_files


def build_species_table(raw_folder: Path, output_folder: Path):
    """
    Build pokemon_species.csv from raw species JSON files.
    """

    species_rows = []

    for file in list_json_files(raw_folder):
        data = read_json(file)

        species_id = data["id"]
        capture_rate = data.get("capture_rate")
        base_happiness = data.get("base_happiness")

        generation = (data.get("generation") or {}).get("name")
        growth_rate = (data.get("growth_rate") or {}).get("name")
        habitat = (data.get("habitat") or {}).get("name")
        color = (data.get("color") or {}).get("name")
        shape = (data.get("shape") or {}).get("name")

        species_rows.append({
            "species_id": species_id,
            "generation": generation,
            "growth_rate": growth_rate,
            "habitat": habitat,
            "capture_rate": capture_rate,
            "base_happiness": base_happiness,
            "color": color,
            "shape": shape
        })

    df_species = pd.DataFrame(species_rows)

    write_csv(df_species, output_folder / "pokemon_species.csv")

    print("Species table created successfully.")
