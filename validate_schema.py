import json

import jsonschema
from jsonschema import validate

print("Validating schema...")

# Load schema
with open("schemas/event.schema.json", "r", encoding="utf-8") as schema_file:
    schema = json.load(schema_file)

# Load data
with open("data/events.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)

# Validate each event
for idx, event in enumerate(data, start=1):
    try:
        validate(instance=event, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(f"Error in event {idx}: {err.message}")

print("Done!")
