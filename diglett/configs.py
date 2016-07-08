import json
import os

HOME_DIR = os.path.expanduser("~")
CONFIG_PATH = os.path.join(HOME_DIR, ".dig.cfg")


def load_or_get_empty_config(config_path=CONFIG_PATH):
    try:
        config = load_config(config_path)
    except IOError:
        config = {}
    return config


def load_config(config_path):
    with open(config_path) as cfg_fd:
        config = json.load(cfg_fd)
    return config


def write_config(config, config_path=CONFIG_PATH):
    with open(config_path, 'w') as cfg_fd:
        json.dump(config, cfg_fd, sort_keys=True, indent=4)


def add_to_config(new_tunnel_conf, tunnel_configs):
    new_conf_name = new_tunnel_conf.keys()[0]
    if new_conf_name not in tunnel_configs:
        tunnel_configs.update(new_tunnel_conf)
        write_config(tunnel_configs)
        print ("Config for {0} added.\n"
               "Use diglett tunnel {0} to connect".format(new_conf_name))
    else:
        print ("Config for name {} already exists. "
               "Please use another name".format(new_conf_name))
        # TODO: Pretty print config with that name
