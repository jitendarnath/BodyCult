
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from body.views import home,signup,signin,signout,contact,memberDashboard,membership,mclass,mtrainer,details,trainerDashboard,tclass,ttrainee,allclass,subscribe,edit,delete,tprofile,mprofile,msession

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('signup/', signup),
    path('signin/', signin),    
    path('signout/', signout),  
    path('trainerDashboard/', trainerDashboard),
    path('tclass/', tclass), 
    path('ttrainee/',ttrainee),
    path('memberDashboard/', memberDashboard),
    path('membership/', membership),
    path('mclass/',mclass),
    path('mtrainer/',mtrainer),
    path('contact/', contact),
    path('details/<int:pk>/', details),
    path('allclass/', allclass),
    path('subscribe/<int:pk>/', subscribe),
    path('edit/<int:pk>/', edit),
    path('delete/<int:pk>/', delete),
    path('tprofile/',tprofile),
    path('mprofile/',mprofile),
    path('msession/',msession)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



