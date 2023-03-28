from django.shortcuts import render, redirect
from main_app.models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
	return user.groups.filter(name='manadger').exists()


# Create your views here.
@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
	massages = Reservation.objects.filter(is_processed=False)
	return render(request, 'reservation_list.html', context={'reservation': massages})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
	Reservation.objects.filter(pk=pk).update(is_processed=True)
	return redirect('manager:reservation')

