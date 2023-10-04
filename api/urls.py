from django.urls import path, include
from api.ger_therapists.urls import urlpatterns as therapists_url 

api_urlpatterns = []

api_urlpatterns += therapists_url

urlpatterns = [path("api/", include(api_urlpatterns))]