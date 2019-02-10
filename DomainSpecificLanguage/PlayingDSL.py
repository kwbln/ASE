import json

import jsl


class User(jsl.Document):
    id = jsl.StringField(required=True)
    login = jsl.StringField(required=True, min_length=3, max_length=20)


class Activity(jsl.Document):
    id = jsl.StringField(required=True)
    name = jsl.StringField(required=True)
    dist = jsl.NumberField(required=True)
    start_time = jsl.DateTimeField(required=True)
    end_time = jsl.DateTimeField(required=True)
    start_gps = jsl.ArrayField(
        lat=jsl.NumberField,
        lng=jsl.NumberField
    ),
    end_gps = jsl.ArrayField(
        lat=jsl.NumberField,
        lng=jsl.NumberField
    )


with open('my_json.json', 'w') as f:
    f.write(json.dumps(Activity.get_schema(ordered=True)))
