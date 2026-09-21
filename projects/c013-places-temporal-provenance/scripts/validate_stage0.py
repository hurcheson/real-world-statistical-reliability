from pathlib import Path
from c013_places.pipeline import validate_project
print(validate_project(Path(__file__).resolve().parents[1]))
