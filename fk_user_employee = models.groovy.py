from datetime import datetime
from rest_framework import exceptions

fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')

fk_user_employee = StringRelatedField()
default='No existe descripción'

->
Related
models.BooleanField('Estado', default=False)

def get_object(self: Self, pk: str):

        try:

            obj: WayToPayModel = None

            obj = self.model.objects.get(pk=pk, status=True)
            return obj

        except self.model.DoesNotExist:

            data: dict = None
            response: ValidationError = None

            data = {
                'error': 'ERROR',
                'msg': 'No existe'
            }

            response = ValidationError(data, HTTP_204_NO_CONTENT)

            raise response

response = {
            'ok': 'OK',
            'data': serializer.data
        }

response = {
            'ok': 'OK',
            'msg': 'Creado Exitosamente',
            'data': serializer.data
        }

response = {
                'ok': 'OK',
                'msg': 'Actualizado Exitosamente',
                'data': serializer.data
            }
            return Response(response, HTTP_200_OK)

response = {
                'ok': 'OK',
                'msg': 'Eliminado Exitosamente',
            }
            return Response(response, HTTP_200_OK)

response = {
            'error': 'ERROR',
            'msg': serializer.errors
        }