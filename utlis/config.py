import yaml
from pathlib import Path

CONFIG_PATH = Path.home() / ".taskmanager" / "config.yaml"

DEFAULT_CONFIG = {
    "settings": {
        "task_file": Path.home() / ".taskmanager" / "tasks.yaml",
        "editor": "vim",
        "date_format": "%Y-%m-%d",
        "time_format": "%H:%M",
    }
}

def initialize_config_file():
    try:
        if not CONFIG_PATH.parent.exists():
            CONFIG_PATH.parent.mkdir(parents=True)
        
        if not CONFIG_PATH.exists():
            with CONFIG_PATH.open("w", encoding="utf-8") as file:
                yaml.dump(DEFAULT_CONFIG, file, default_flow_style=False)
            print(f"Created config file at: {CONFIG_PATH} with default settings.")
    except Exception as e:
        print(f"An error occurred while initializing the config file: {e}")
        
def update_config(section, key, value):
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        
        if section not in config:
            config[section] = {}
        
        config[section][key] = value
        
        with CONFIG_PATH.open("w", encoding="utf-8") as file:
            yaml.dump(config, file, default_flow_style=False)
        
        print(f"Updated config setting: {section}.{key} = {value}")
    except Exception as e:
        print(f"An error occurred while updating the config file: {e}")
        
def get_task_file_path():
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        
        return Path(config["settings"]["task_file"])
    except Exception as e:
        print(f"An error occurred while reading the config file: {e}")
        return None