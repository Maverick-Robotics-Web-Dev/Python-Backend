from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class LoginPermissionsMixin():

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print(self.request.user)
            return redirect(settings.LOGIN_URL)

    # def test_func(self):
    #     # obtenemos todos los grupos del usuario logueado
    #     grupos = self.request.user.groups.all()
    #     # comparamos que el usuario pertenezca al grupo GERENTE
    #     if 'GERENTE' in grupos:
    #         return True
    #     return False

    def dispatch(self, request, *args, **kwargs):
        if request.user:
            print(request.user)
            return self.get_login_url()
        return super().dispatch(request, *args, **kwargs)

# class LoginPermissionsMixin(LoginRequiredMixin, UserPassesTestMixin):

#     _PERMISSIONS = []

#     # def get_login_url(self):
#     #     if not self.request.user.is_authenticated:
#     #         # el usuario no está logueado, ir a la página de login
#     #         return super(LoginPermissionsMixin, self).get_login_url()
#     #     # El usuario está logueado pero no está autorizado
#     #     return '/no_autorizado/'

#     def test_func(self):
#         # obtenemos todos los grupos del usuario logueado
#         grupos = self.request.user.groups.all()
#         # comparamos los grupos del usuario con la lista de permisos
#         for grupo in self._PERMISSIONS:
#             print(grupo)
#             if grupo in ['VENDEDOR', 'SUPERVISOR']:
#                 return True
#         return False
