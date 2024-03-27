from typing import Self

from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet


class MultiSerializerViewSet(GenericViewSet):

    action: str = None
    serializers: dict = None

    serializers = {"default": None}

    def get_serializer_class(self: Self) -> Serializer:
        """
        Devuelve un serializador en función del verbo HTTP
        (o acción). Si no está definido, devuelve el serializador
        por defecto.
        """

        return self.serializers.get(
            self.action, self.serializers["default"])

    def get_serializer(self, *args, **kwargs) -> Serializer:
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)
