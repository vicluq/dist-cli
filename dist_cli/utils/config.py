import os
import json

def create_if_not_exists(config_file: str):
      if not os.path.isfile(f'.dist/{config_file}'):
            with open(os.path.join(f'.dist/{config_file}'), 'w') as f:
                  f.close()

def add_config(config_file: str, elem_name: str, config_data: dict):
      data = {}

      create_if_not_exists(config_file)

      with open(os.path.join(f'.dist/{config_file}'), 'r') as f:
            f_data = f.read()
            if f_data:
                  data = json.loads(f_data)
            f.close()

      with open(os.path.join(f'.dist/{config_file}'), 'w') as f:
            data[elem_name] = config_data
            f.write(json.dumps(data))
            f.close()


def get_config(config_file: str, key: str):
      create_if_not_exists(config_file)
      data = {}
      
      with open(os.path.join(f'.dist/{config_file}'), 'r') as f:
            f_data = f.read()
            if f_data:
                  data = json.loads(f_data)
            f.close()

      return data[key] if data.get(key) else None


def get_all_config(config_file: str):
      create_if_not_exists(config_file)
      data = {}
      
      with open(os.path.join(f'.dist/{config_file}'), 'r') as f:
            f_data = f.read()
            if f_data:
                  data = json.loads(f_data)
            f.close()

      return data


def update_config(config_file: str, key: str, new_data: dict, new_key: str = None):
      create_if_not_exists(config_file)
      data = {}
      
      with open(os.path.join(f'.dist/{config_file}'), 'r') as f:
            f_data = f.read()
            if f_data:
                  data = json.loads(f_data)
            f.close()

      if not data.get(key):
            return False
      
      if new_key:
            data.pop(key)
            data[new_key] = new_data
      else:
           data[key] = new_data

      with open(os.path.join(f'.dist/{config_file}'), 'w') as f:
            f.write(json.dumps(data))
            f.close()

      return True


def delete_config(config_file: str, key: str):
      create_if_not_exists(config_file)
      data: dict = {}
      conf = {}

      with open(os.path.join(f'.dist/{config_file}'), 'r') as f:
            f_data = f.read()
            if f_data:
                  data = json.loads(f_data)
                  conf = data.pop(key)
            f.close()

      with open(os.path.join(f'.dist/{config_file}'), 'w') as f:
            f.write(json.dumps(data))
            f.close()

      return conf