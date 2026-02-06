import yaml
import os

# Configuration manager for specified environments
class ConfigManager:
    def __init__(self, config_dir='configs'):
        self.config_dir = config_dir
        self.config = {}
    
    def load_config(self, environment='development'):
        """Load configuration for a specific environment"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        try:
            with open(config_file, 'r') as file:
                self.config = yaml.safe_load(file)
            print(f"✓ Loaded configuration for {environment}")
            return self.config
        except FileNotFoundError:
            print(f"✗ Configuration file not found: {config_file}")
            return None
        except yaml.YAMLError as e:
            print(f"✗ Error parsing YAML: {e}")
            return None
        
    def get(self, key_path, default=None):
        """Get a configuration value using dot annotation"""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            # Check if the value is a dictionary and key is present in it
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
            
        return value
    
    def save_config(self, environment, config_data):
        """Save configuration to a file"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        os.makedirs(self.config_dir, exist_ok=True)
        
        with open(config_file, 'w') as file:
            yaml.dump(config_data, file, default_flow_style=False)
            
        print(f"✓ Saved configuration for {environment}")