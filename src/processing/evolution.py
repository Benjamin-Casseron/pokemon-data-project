from pathlib import Path
import pandas as pd
from utils.io import read_json, write_csv, list_json_files
from api.pokeapi import fetch_endpoint


def extract_species_id_from_url(url: str) -> int:
    return int(url.rstrip("/").split("/")[-1])


def flatten_chain(chain: dict, parent_species_id=None, trigger=None, min_level=None, item=None, rows=None):
    if rows is None:
        rows = []

    species_id = extract_species_id_from_url(chain["species"]["url"])

    # Add a row if this species evolves from another
    if parent_species_id is not None:
        rows.append({
            "species_id": species_id,
            "evolves_from_species_id": parent_species_id,
            "trigger": trigger,
            "min_level": min_level,
            "item": item
        })

    # Process further evolutions
    for evo in chain.get("evolves_to", []):
        evo_details = evo["evolution_details"][0] if evo["evolution_details"] else {}

        # Safely extract item (can be None)
        raw_item = evo_details.get("item")
        item_name = raw_item["name"] if isinstance(raw_item, dict) else None

        flatten_chain(
            evo,
            parent_species_id=species_id,
            trigger=evo_details.get("trigger", {}).get("name"),
            min_level=evo_details.get("min_level"),
            item=item_name,
            rows=rows
        )

    return rows


def build_evolution_table(species_raw_folder: Path, output_folder: Path):
    """
    Build pokemon_evolution.csv by fetching and flattening evolution chains.
    """

    # Step 1: Collect unique evolution chain URLs
    chain_urls = set()

    for file in list_json_files(species_raw_folder):
        data = read_json(file)
        url = data["evolution_chain"]["url"]
        chain_urls.add(url)

    rows = []

    # Step 2: Fetch and flatten each evolution chain
    for url in chain_urls:
        chain_id = extract_species_id_from_url(url)
        chain_json = fetch_endpoint(f"evolution-chain/{chain_id}")

        flat_rows = flatten_chain(chain_json["chain"])
        rows.extend(flat_rows)

    # Build DataFrame
    df_evo = pd.DataFrame(rows)

    # Save to CSV
    write_csv(df_evo, output_folder / "pokemon_evolution.csv")

    print("Evolution table created successfully.")
