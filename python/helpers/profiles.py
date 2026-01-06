
import os
import json
from python.helpers import files, settings

DEFAULT_AGENTS_DIR = "agents/default"
CUSTOM_AGENTS_DIR = "agents/custom"

def list_profiles():
    profiles = []
    # List default profiles
    if os.path.exists(DEFAULT_AGENTS_DIR):
        for d in os.listdir(DEFAULT_AGENTS_DIR):
            if os.path.isdir(os.path.join(DEFAULT_AGENTS_DIR, d)):
                profiles.append({"id": d, "name": d, "type": "default"})

    # List custom profiles
    if os.path.exists(CUSTOM_AGENTS_DIR):
        for d in os.listdir(CUSTOM_AGENTS_DIR):
            if os.path.isdir(os.path.join(CUSTOM_AGENTS_DIR, d)):
                # Avoid duplicates if custom overrides default
                if not any(p['id'] == d for p in profiles):
                    profiles.append({"id": d, "name": d, "type": "custom"})
                else:
                    for p in profiles:
                        if p['id'] == d: p['type'] = 'custom' # Mark as overridden
    return profiles

def create_profile(name: str):
    path = os.path.join(CUSTOM_AGENTS_DIR, name)
    os.makedirs(path, exist_ok=True)
    config_path = os.path.join(path, "config.json")
    if not os.path.exists(config_path):
        with open(config_path, 'w') as f:
            json.dump({}, f)
    return {"id": name, "name": name, "type": "custom"}

def set_profile(profile_name: str):
    from python.helpers import settings, dotenv
    dotenv.save_dotenv_value("A0_SET_AGENT_PROFILE", profile_name)
    settings.reload_settings()
    return {"status": "success", "profile": profile_name}
