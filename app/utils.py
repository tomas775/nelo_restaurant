# utils.py (helper module)

def serialize_list(items: list) -> str:
    """Convert a list to a comma-separated string for database storage."""
    if not items:
        return ""
    return ", ".join(items)

def deserialize_list(serialized: str) -> list:
    """Convert a comma-separated string back to a list."""
    if not serialized:
        return []
    return serialized.split(", ")
