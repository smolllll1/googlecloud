from django.shortcuts import render, redirect
from .models import DishCategory, Dish, About, Service, Galerys, Events
from .forms import ReservationForm
# Create your views here.
def main_view(request):

	if request.method == 'POST':
		form_reserve = ReservationForm(request.POST)
		if form_reserve.is_valid():
			form_reserve.save()
			return redirect('/#')

	categories = DishCategory.objects.filter(is_visible=True)
	dishes = Dish.objects.filter(is_visible=True, is_special=False, is_signature=False)
	is_signature = Dish.objects.filter(is_visible=True, is_signature=True)
	special = Dish.objects.filter(is_visible=True, is_special=True)
	ubout = About.objects.filter(is_visible=True)
	servis = Service.objects.filter(is_visible=True)
	galerys = Galerys.objects.filter(is_visible=True)
	form_reserve = ReservationForm()
	events = Events.objects.filter(is_visible=True)

	return render(request, 'main_page.html', context={
		'categories': categories,
		'dishers': dishes,
		'signature': is_signature,
		'offers': special,
		'ubout': ubout,
		'servis': servis,
		'galerys': galerys,
		'form_reserve': form_reserve,
		'events': events,
	})

