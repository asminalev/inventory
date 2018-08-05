from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from inventory import views

urlpatterns = [
    url(r'', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^inventory/', include('inventory.urls')),

]
