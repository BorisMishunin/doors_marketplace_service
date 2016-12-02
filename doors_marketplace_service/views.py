# -*- coding: utf-8 -*-

from rest_framework import generics, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from doors_marketplace_service.models import Actions
from doors_marketplace_service.serializers import ActionsSerializer


class ActionsList(viewsets.ModelViewSet):
    queryset = Actions.objects.filter(actual=True)
    serializer_class = ActionsSerializer

