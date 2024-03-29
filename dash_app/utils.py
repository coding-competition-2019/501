import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        j_file = json.load(f)
    return j_file


def save_json(d_file, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d_file, f, ensure_ascii=False)


def check_activity_matches_existing(activity_list, in_activity):
    if in_activity in activity_list:
        return True
    else:
        return False
