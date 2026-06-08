import json
import os
from collections import defaultdict, Counter
from typing import Dict, List, Any, Set
import hashlib

def get_file_hash(filepath: str) -> str:
    """Calculate SHA256 hash of file content"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def infer_schema(obj: Any, path: str = "") -> Dict[str, Any]:
    """Recursively infer schema from JSON object"""
    if isinstance(obj, dict):
        schema = {"type": "object", "properties": {}}
        for key, value in obj.items():
            nested_path = f"{path}.{key}" if path else key
            schema["properties"][key] = infer_schema(value, nested_path)
        return schema
    elif isinstance(obj, list):
        if not obj:
            return {"type": "array", "items": {"type": "unknown"}}
        # Check if all items are the same type
        item_types = set()
        for item in obj:
            item_types.add(type(item).__name__)
        if len(item_types) == 1:
            item_type = list(item_types)[0]
            if item_type == "dict":
                # For arrays of objects, infer schema of first item
                if len(obj) > 0:
                    schema = {"type": "array", "items": infer_schema(obj[0])}
                else:
                    schema = {"type": "array", "items": {"type": "unknown"}}
            else:
                schema = {"type": "array", "items": {"type": item_type}}
        else:
            schema = {"type": "array", "items": {"type": "mixed"}}
        return schema
    else:
        return {"type": type(obj).__name__}

def normalize_schema(schema: Dict[str, Any]) -> str:
    """Convert schema to normalized string representation for comparison"""
    def _normalize(obj: Any) -> str:
        if isinstance(obj, dict):
            if "type" in obj:
                if obj["type"] == "object":
                    props = sorted(obj.get("properties", {}).items())
                    return f"object({','.join(f'{k}:{_normalize(v)}' for k, v in props)})"
                elif obj["type"] == "array":
                    items = _normalize(obj.get("items", {}))
                    return f"array({items})"
                else:
                    return obj["type"]
            else:
                return str(sorted(obj.items()))
        else:
            return str(obj)
    
    return _normalize(schema)

def load_json_files(filepaths: List[str]) -> List[tuple]:
    """Load JSON files and return (filepath, data, schema) tuples"""
    loaded_files = []
    for filepath in filepaths:
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                schema = infer_schema(data)
                loaded_files.append((filepath, data, schema))
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
    return loaded_files

# Get all JSON files
json_files = [
    "p_1_log.json",
    "./tasks/task_276/step_3_log.json",
    "./tasks/task_276/step_2_log.json",
    "./tasks/task_276/step_4_log.json",
    "./tasks/task_234/step_1_log.json",
    "./tasks/task_234/step_3_log.json",
    "./tasks/task_234/step_2_log.json",
    "./tasks/task_234/step_4_log.json",
    "./tasks/task_012/step_1_log.json",
    "./tasks/task_012/step_3_log.json",
    "./tasks/task_012/step_2_log.json",
    "./tasks/task_012/step_4_log.json",
    "./tasks/task_012/step_5_log.json",
    "./tasks/task_018/step_1_log.json",
    "./tasks/task_018/step_3_log.json",
    "./tasks/task_018/step_2_log.json",
    "./tasks/task_137/step_1_log.json",
    "./tasks/task_137/step_3_log.json",
    "./tasks/task_137/step_2_log.json",
    "./tasks/task_055/step_1_log.json",
    "./tasks/task_055/step_3_log.json",
    "./tasks/task_055/step_2_log.json",
    "./tasks/task_158/step_