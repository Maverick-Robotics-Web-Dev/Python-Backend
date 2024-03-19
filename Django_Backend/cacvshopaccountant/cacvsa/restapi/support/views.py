from typing import Any
from rest_framework.viewsets import ViewSet, GenericViewSet


class MultiSerializerViewSet(GenericViewSet):

    action: str | Any = None
    serializers_classes: dict[str, None] = None

    serializers_classes = {"default": None}

    def get_serializer_class(self) -> None:
        """
        Devuelve un serializador en función del verbo HTTP
        (o acción). Si no está definido, devuelve el serializador
        por defecto.
        """

        return self.serializers_classes.get(
            self.action, self.serializers_classes["default"])
