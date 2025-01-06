from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ledger/', include('ledger.urls')),  # Include URLs from the ledger app
]
