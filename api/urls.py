from django.urls import path, include


from api.ger_therapists.urls import urlpatterns as therapists_urls
from api.ger_patients.urls import urlpatterns as patients_urls
from api.users.urls import urlpatterns as users_urls

api_urlpatterns = []

api_urlpatterns += therapists_urls
api_urlpatterns += patients_urls
api_urlpatterns += users_urls

urlpatterns = [path("api/", include(api_urlpatterns))]