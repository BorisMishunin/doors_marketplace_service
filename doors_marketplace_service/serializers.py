# -*- coding: utf-8 -*-

from rest_framework import serializers

import json

class WritableJSONField(serializers.Field):
    def to_representation(self, obj):
        return json.loads(obj)

    def to_internal_value(self, data):
        return json.dumps(data)





