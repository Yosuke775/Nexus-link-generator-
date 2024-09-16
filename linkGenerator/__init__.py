import yaml
from pathlib import Path
import logging
from rich.logging import RichHandler

logging.basicConfig(
	format="[%(asctime)s] In thread %(threadName)s, module %(module)s at %(funcName)s line %(lineno)s -> %(message)s",
	level=logging.INFO,
	handlers=[RichHandler()],
)

logging.getLogger("httpx").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


def config(key):
    yaml_file_path = Path("config.yaml")
    
    try:
        with open(yaml_file_path, 'r') as file:
            config = yaml.safe_load(file)
        
        return config.get(key) if config else None
    except FileNotFoundError:
        LOGGER.error(f"Config file not found at {yaml_file_path}")
        return None
    except yaml.YAMLError as e:
        LOGGER.error(f"Error parsing YAML file: {e}")
        return None
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
        return None


class StringsManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = self.load_yaml()
    
    def load_yaml(self):
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            LOGGER.error(f"Config file not found at {self.file_path}")
            return None
        except yaml.YAMLError as e:
            LOGGER.error(f"Error parsing YAML file: {e}")
            return None
    
    def get_string(self, dot_notation, *args):
        if not self.config:
            return None
        
        try:
            category, key = dot_notation.split('.', 1)
        except ValueError:
            LOGGER.error(f"Invalid dot notation: '{dot_notation}'")
            return None

        category_data = self.config.get(category)
        if not category_data:
            LOGGER.error(f"Category '{category}' not found in config.")
            return None
        
        template = category_data.get(key)
        if not template:
            LOGGER.error(f"Key '{key}' not found in category '{category}'.")
            return None
        
        try:
            return template.format(*args)
        except (IndexError, KeyError, ValueError) as e:
            LOGGER.error(f"Error formatting string: {e}")
            return None

sm = StringsManager(Path("linkGenerator/strings/strings.yaml"))
PendingUpdatesStatus = config("drop_pending_updates")

