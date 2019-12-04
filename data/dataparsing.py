import utils


def transform_data(j_file):
    activities = _get_unique_activities(j_file)
    _get_places_by_activites(j_file, activities)
    activity_set = activities.keys()
    transformed_data = dict()
    transformed_data["activity_list"] = list(activity_set)
    transformed_data['places'] = activities
    return transformed_data


def _get_unique_activities(j_file):
    activities = dict()
    for place in j_file['places']:
        for activity in place['activities']:
            print(activity)
            activities[activity] = list()
    return activities


def _get_places_by_activites(j_file, activities):
    for id, place in enumerate(j_file['places']):
        p = dict()
        p['name'] = place['name']
        p['url'] = place['url']
        p['address'] = place['address']
        p['activities'] = place['activities']
        for activity in place['activities']:
            activities[activity].append(id)


if __name__ == '__main__':
    data = utils.read_json('data/places.json')
    t_data = transform_data(data)
    utils.save_json(t_data, 'data/places_transformed.json')
