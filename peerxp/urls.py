from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from Acme_Support.models import Ticket, Category
from rest_framework import routers

from Acme_Support.views import UserViewSet, TicketViewSet, CategoryViewSet,dashboard,register,edit

from django.contrib.auth import views as auth

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

router.register(r'api/tickets', TicketViewSet)

router.register(r'api/category', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),


    path('', include('Acme_Support.urls')),
    path('admin/', admin.site.urls),
]
