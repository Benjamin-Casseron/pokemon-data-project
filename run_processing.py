from utils.spinner import Spinner
from pathlib import Path
from processing.pokemon import build_pokemon_tables
from processing.species import build_species_table
from processing.types import build_types_table
from processing.evolution import build_evolution_table

RAW_POKEMON = Path("data_raw/pokemon")
RAW_SPECIES = Path("data_raw/species")
OUT = Path("data_clean")

build_pokemon_tables(RAW_POKEMON, OUT)
build_species_table(RAW_SPECIES, OUT)
build_types_table(OUT)
with Spinner("Building evolution table"):
    build_evolution_table(RAW_SPECIES, OUT)

print("Data processing complete.")