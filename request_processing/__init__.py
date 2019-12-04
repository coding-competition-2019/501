import yaml
import googlemaps

GOOGLE_KEY_NAME = 'google-api-key'


def load_key(key_name):
    with open('data/config.yml', mode='r') as f:
        cfg = yaml.load(f, Loader=yaml.BaseLoader)

    return cfg[key_name][0]


def get_service():
    return googlemaps.Client(key=load_key(GOOGLE_KEY_NAME))


if __name__ == '__main__':
    import os

    os.chdir('..')
    print(load_key(GOOGLE_KEY_NAME))
    service = get_service()
