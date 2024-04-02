# from cacvsa.settings.base import *
from typing import Any, Self

from django.conf import settings
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

from rest_framework.request import Request


class LoginPermissionsMixin():

    def get_login_url(self: Self, request: Request) -> (HttpResponseRedirect | HttpResponsePermanentRedirect):

        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return redirect(settings.HOME_URL)

    # def test_func(self):
    #     # obtenemos todos los grupos del usuario logueado
    #     grupos = self.request.user.groups.all()
    #     # comparamos que el usuario pertenezca al grupo GERENTE
    #     if 'GERENTE' in grupos:
    #         return True
    #     return False

    def dispatch(self: Self, request: Request, *args: tuple, **kwargs: dict) -> (HttpResponseRedirect | HttpResponsePermanentRedirect | Any):

        if request.user:
            return self.get_login_url(request)

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
