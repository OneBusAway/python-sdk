from typing import Any, Dict, Optional
from pathlib import Path


def load_settings(default_settings: Dict[str, Any]) -> Dict[str, Any]:
    """
    Load settings by merging default settings with environment variables.

    Args:
        default_settings (Dict[str, Any]): The default settings to use.

    Returns:
        Dict[str, Any]: The merged settings.
    """
    env_variables = load_env()
    if env_variables:
        return {**default_settings, **env_variables}
    else:
        return default_settings


def load_env() -> Optional[Dict[str, Any]]:
    """
    Loads environment variables from a .env file located in the parent directory of the current file.

    Returns:
        A dictionary containing the loaded environment variables, or None if the .env file does not exist.
    """
    dirname = Path(__file__).resolve().parent
    env_path = dirname.parent / ".env"

    if env_path.exists():
        return load_env_from_path(str(env_path))
    else:
        return None


def load_env_from_path(file_path: str) -> Dict[str, str]:
    """
    Load environment variables from a file.

    Args:
        file_path (str): The path to the file containing environment variables.

    Returns:
        dict: A dictionary containing the loaded environment variables, where the keys are the variable names
        and the values are the variable values.

    """
    env = {}
    with open(file_path, "r", encoding="utf8") as file:
        lines = file.readlines()

    for line in lines:
        # Remove comments and trim whitespace
        trimmed_line = line.split("#")[0].strip()

        if not trimmed_line:
            continue

        key_value = trimmed_line.split("=", 1)
        if len(key_value) != 2:
            continue

        key, value = key_value
        value = value.strip()

        # Remove surrounding quotes if they exist
        if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]

        env[key.strip()] = value

    return env  # type: ignore
