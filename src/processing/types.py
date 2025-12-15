from pathlib import Path
import pandas as pd
from utils.io import write_csv
from api.pokeapi import fetch_endpoint

def build_types_table(output_folder: Path):
    """
    Fetch /type endpoint and build types.csv
    """

    data = fetch_endpoint("type")

    rows = []
    for t in data["results"]:
        # Extract ID from URL
        type_id = int(t["url"].rstrip("/").split("/")[-1])
        type_name = t["name"]

        rows.append({
            "type_id": type_id,
            "type_name": type_name
        })

    df_types = pd.DataFrame(rows)
    write_csv(df_types, output_folder / "types.csv")

    print("Types table created successfully.")
