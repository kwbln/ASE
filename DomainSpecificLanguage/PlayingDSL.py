import json

import jsl


class GeoData(jsl.Document):
    lat = jsl.NumberField(required=True)
    lng = jsl.NumberField(required=True)


class Activity(jsl.Document):
    id = jsl.StringField(required=True)
    name = jsl.StringField(required=True)
    dist = jsl.NumberField(required=True)
    start_time = jsl.DateTimeField(required=True)
    end_time = jsl.DateTimeField(required=True)
    start_gps = jsl.ArrayField(
        jsl.DocumentField(GeoData, as_ref=True)
    )
    end_gps = jsl.ArrayField(
        jsl.DocumentField(GeoData, as_ref=True)
    )


with open('my_json.json', 'w') as f:
    f.write(json.dumps(Activity.get_schema(ordered=True)))
