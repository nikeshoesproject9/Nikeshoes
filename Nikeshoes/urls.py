from django.contrib import admin
from django.urls import path, include
from shoes import views as shoes_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shoes_views.home, name='home'),
    path('item_details/<shoe_id>', shoes_views.item_details, name='item_details'),
    path('myCart', shoes_views.myCart, name='myCart'),
    

    path('accounts/', include('accounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)