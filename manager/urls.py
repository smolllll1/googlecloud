from django.urls import path
from .views import reservation_list, update_reservation

app_name = 'manager'

urlpatterns = [
	path('reservation/', reservation_list, name='reservation'),
	path('reservation/update/<int:pk>', update_reservation, name='update_reservation'),
]