import yaml
import googlemaps


def load_key():

    with open("data/config.yml", mode="r") as f:
        cfg = yaml.load(f, Loader=yaml.BaseLoader)

    return cfg["api-key"][0]


def get_service():
    return googlemaps.Client(key=load_key())


if __name__ == "__main__":
    import os

    os.chdir("..")
    print(load_key())
    service = get_service()
