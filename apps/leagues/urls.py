from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^make_data$", views.make_data, name="make_data"),
	url(r"^get-results/$", views.get_results, name="get-results"),
]