from django.urls import re_path, path
from rest_framework.documentation import include_docs_urls

from .swaggerview import *

urlpatterns = [
    path('', schema_view.with_ui('redoc',
                                 cache_timeout=0), name='schema-redoc'),
    path('coreapi/', include_docs_urls(title='CACVSA API'), name='home'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]
