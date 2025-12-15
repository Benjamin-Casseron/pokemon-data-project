import json
from pathlib import Path
import pandas as pd

def read_json(path: Path) -> dict:
    """Read a JSON file and return it as a Python dict."""
    with path.open(encoding="utf-8") as f:
        return json.load(f)

def write_csv(df: pd.DataFrame, path: Path):
    """Write a DataFrame to CSV with UTF-8 encoding."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")

def list_json_files(folder: Path) -> list[Path]:
    """Return a list of all JSON files in a folder."""
    return sorted(folder.glob("*.json"))
