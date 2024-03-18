from typing import Any
from rest_framework.viewsets import ViewSet, GenericViewSet


class MultiSerializerViewSet(ViewSet):

    action: str | Any = None
    serializers: dict[str, None] = None

    serializers = {"default": None}

    def get_serializer_class(self):
        """
        Devuelve un serializador en función del verbo HTTP
        (o acción). Si no está definido, devuelve el serializador
        por defecto.
        """

        return self.serializers.get(
            self.action, self.serializers["default"])
