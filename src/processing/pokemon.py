from pathlib import Path
import pandas as pd
from utils.io import read_json, write_csv, list_json_files


def build_pokemon_tables(raw_folder: Path, output_folder: Path):
    """
    Read all raw /pokemon/ JSON files and build:
    - pokemon.csv
    - pokemon_stats.csv
    - pokemon_types.csv
    - pokemon_abilities.csv
    """

    pokemon_rows = []
    stats_rows = []
    types_rows = []
    abilities_rows = []

    for file in list_json_files(raw_folder):
        data = read_json(file)

        poke_id = data["id"]
        name = data["name"]
        species_id = data["species"]["url"].split("/")[-2]
        height = data["height"]
        weight = data["weight"]
        base_exp = data["base_experience"]
        order = data["order"]
        sprite = data["sprites"]["front_default"]

        # ---- Main Pokémon table row ----
        pokemon_rows.append({
            "pokemon_id": poke_id,
            "name": name,
            "species_id": int(species_id),
            "height": height,
            "weight": weight,
            "base_experience": base_exp,
            "order": order,
            "sprite": sprite
        })

        # ---- Stats ----
        for s in data["stats"]:
            stats_rows.append({
                "pokemon_id": poke_id,
                "stat_name": s["stat"]["name"],
                "base_stat": s["base_stat"],
                "effort": s["effort"]
            })

        # ---- Types ----
        for t in data["types"]:
            types_rows.append({
                "pokemon_id": poke_id,
                "slot": t["slot"],
                "type_name": t["type"]["name"]
            })

        # ---- Abilities ----
        for a in data["abilities"]:
            abilities_rows.append({
                "pokemon_id": poke_id,
                "ability_name": a["ability"]["name"],
                "is_hidden": a["is_hidden"],
                "slot": a["slot"]
            })

    # Convert to DataFrames
    df_pokemon = pd.DataFrame(pokemon_rows)
    df_stats = pd.DataFrame(stats_rows)
    df_types = pd.DataFrame(types_rows)
    df_abilities = pd.DataFrame(abilities_rows)

    # Save as CSV
    write_csv(df_pokemon, output_folder / "pokemon.csv")
    write_csv(df_stats, output_folder / "pokemon_stats.csv")
    write_csv(df_types, output_folder / "pokemon_types.csv")
    write_csv(df_abilities, output_folder / "pokemon_abilities.csv")

    print("Pokémon tables created successfully.")
