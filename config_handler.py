import json

def load_cfg():
  # check if settings file exists
  try:
    cfg_file = open("settings.json", "r")
    
  except OSError: # generate default settings if file does not exist
    print("generating new settings file")
    cfg_file = open("settings.json", "w")
    default_settings = {"discord_token": "", "prefix": "#"}
    json.dump(default_settings, cfg_file)
  
  cfg_file = open("settings.json", "r")
  retval = json.load(cfg_file)
  cfg_file.close()
  return retval

def update_cfg_file(config):
  cfg_file = open("settings.json", "w")
  json.dump(config, cfg_file)
  cfg_file.close()