from datetime import datetime
from rest_framework import exceptions

fk_user_employee = models.ForeignKey(
        'users.UserEmployeeModel', on_delete=models.CASCADE, verbose_name='Usuario')

fk_user_employee = StringRelatedField()
default='No existe descripción'
credit_note_create_at = models.DateTimeField('Fecha de Creación')
credit_note_update_at = models.DateTimeField(
        'Fecha de Actualización', blank=True, null=True)
credit_note_status = models.BooleanField('Estado', default=False)

c
models.BooleanField('Estado', default=False)

        try:

            obj = self.model.objects.get(pk=pk, way_to_pay_status=True)
            return obj

        except self.model.DoesNotExist:

            response = {'error': 'ERROR', 'msg': 'No existe'}
            raise exceptions.ValidationError(response)

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