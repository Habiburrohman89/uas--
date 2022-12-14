from django.contrib import admin
from django.urls import include, path

from. import views
from blog import views as blogviews
from about import views as aboutviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rohman/',include('rohman.urls')),
    path('tahu/', blogviews.tahu),
    path('skripsi/', aboutviews.bh),
    path('matakuliah/', aboutviews.hp),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('',views.habib),
]
