# -*- coding: utf-8 -*-

from rest_framework import serializers
from doors_marketplace_service.models import Actions

import json

class WritableJSONField(serializers.Field):
    def to_representation(self, obj):
        return json.loads(obj)

    def to_internal_value(self, data):
        return json.dumps(data)

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        partial=True
        fields = "__all__"



