from django.shortcuts import render, redirect 

from django.http import HttpResponse
from app.models import State, StateCapital, City

from django.utils.html import escape

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import View 

from app.forms import CitySearchForm, CityCreate, EditCity, EditState


# Create your views here.

def edit_state(request, pk):

	context = {}

	stae = State.objects.get(pk=pk)

	context['state'] = state 

	form = EditState(request.POST or None, instance=state) 

	context['form'] = form 

	if form.is_valid():
		form.save()

		return redirect('/state_list/')

	return render(request, 'state_edit.html', context)



@login_required
def delete_city(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_list/')

@login_required
def edit_city(request, pk):

	context = {}

	city = City.objects.get(pk=pk) 

	context['city'] = city 


	form = EditCity(request.POST or None, instance=city)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/city_list/')

	return render(request, 'city_edit.html', context)

@login_required
def create_city(request):

	context = {}

	form = CityCreate(request.GET)

	context['form'] = form

	if form.is_valid():
		form.save()

	return render(request, 'create_city.html', context)


def city_search_post(request):

	context = {}

	form = CitySearchForm(request.POST)

	context['form'] = form

	print request.method
	print "it looks like the method was %s" % request.method


	if request.method == 'POST': 
		if form.is_valid():
			city = form.cleaned_data.get('city', 'Orem')
			state = form.cleaned_data.get('state', 'Utah')

	context['cities'] = city.objects.filter(name=city, state__name=state)

	return render(request, 'city_search_post.html', context)



def city_search(request):

	context = {}

	form = CitySearchForm(request.GET) 

	context['form'] = form

	if form.is_valid():

		city = form.cleaned_data.get("city", "Orem")
		state = form.cleaned_data.get("state", "Utah")

		cities = City.objects.filter(name=city, state__name=state)

		context['cities'] = cities

	return render(request, 'city_search.html', context)



# def city_search(request):

# 	context = {}

# 	form = CitySearchForm(request.GET)

# 	if form.is_valid():
# 		state = form.cleaned_data.get('state', 'Utah')
# 		city = form.cleaned_data.get('city', 'Orem')
# 		cities = City.objects.filter(name=city, state__name=state) 

# 		context['cities'] = cities

# 		context['form'] = form

# 	else: 
# 		context['form'] = form

# 	return render(request, 'city_search.html', context)


def city_search_old(request):

	context = {}

	form = CitySearchForm(request.GET)

	#print dir(form)

	#print form.data

	print form.is_valid()

	print form.cleaned_data

	#state = form.cleaned_data['state']
	#city = form.cleaned_data['city', 'Orem']


	state = form.cleaned_data.get('state', 'Utah')
	city = form.cleaned_data.get('city', 'Orem')

	print "%s is a state" % state
	print "%s is a city" % city 

	cities = City.objects.filter(name=city, state__name=state) 

	context['cities'] = cities

	context['form'] = form

	return render(request, 'city_search.html', context)

def city_list(request):

	context = {}

	context['cities'] = City.objects.all()

	# state.city_set.all()


	return render(request, 'city_list.html', context)



def state_detail(request, pk):
	context = {}

	state = State.objects.get(pk=pk)

	context['state'] = state 

	return render(request, 'state_detail.html', context)




def state_list(request):

	context = {}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'state_list.html', context)



def list(request):

	context = {}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'list.html', context)


def detail(request, pk):

	context = {}
	state = State.objects.get(pk=pk)

	context['state'] = state

	return render(request, 'state_detail.html', context)



def template_view2(request):

	context = {}
	state_city = {}

	states = State.objects.all()

	for state in states:
		cities = state.city_set.filter(name__startswith='A')

		state.name = { state.name : cities }

		state_city.update(state.name)

	context['states'] = state_city

	return render(request, 'base2.html', context)




def template_view(request):


	context = {}

	states = State.objects.all()

	context['states'] = states 

	return render(request, 'base.html', context)



class GetPost(View):
	def get(self, request, *args, **kwargs): 
		city_state_string = """

		<form action="/form_view/" method="GET">

		State: <input type="text" name="state" >

		<br>

		City: <input type="text" name="city" >

		<br>

		<input type="submit" value="Search" >

		</form>

		<br>
		<br>
		""" 

		states = State.objects.filter(name__startswith=get_state)

		for state in states:
			cities = state.city_set.filter(name__startswith=get_city)

			for city in cities:
				city_state_string += "<b>%s</b> %s -- %s<br>" % (state, city.name, city.zipcode)


		return HttpResponse(city_state_string)


# def post


def form_view(request):

	state = request.GET.get('state', 'C') #fails gracefully 
	#state = request.GET('state') #fails hard
	city = request.GET.get('city', 'C')


	city_state_string= """
	<from action="/from_view/" method="GET" >

		State: <input type="text" name="state" > <br>

		City: <input type="text" name="city" > <br>

		<input type="submit" value="submit">

	</form>

	"""

	states = State.objects.filter(name__startswith=state)

	for state in states:
				# parent.child_set
		cities = state.city_set.filter(name__startswith=city)
		for city in cities:
			city_state_string += ",b>%s</b> %s | %s" % (state.name, city.name, city.zipcode)
	return HttpResponse(city_state_string)


# @csrf_exempt

#def form_view(request):

#	get_state = request.GET.get('state', 'C')
#	get_city = request.GET.get('city', 'C')

#	city_state_string = """
#	POST: %s <br>
#	GET: %s <br>

#	<form action="/form_view/" method="GET">

#	State: <input type="text" name="state" >

#	<br>

#	City: <input type="text" name="city" >

#	<br>

	# <input type="submit" value="Search" >

	# </form>

	# <br>
	# <br>
	# """ % (escape(request.POST), escape(request.GET))

	# states = State.objects.filter(name__startswith=get_state)

	# for state in states:
	# 	cities = state.city_set.filter(name__startswith=get_city)

	# 	for city in cities:
	# 		city_state_string += "<b>%s</b> %s -- %s<br>" % (state, city.name, city.zipcode)


	# city_state_string += """
	# <from action="/form_view/" method="POST">

	# State: <input type="text" name="state" >

	# <br>

	# City: <input type="text" name="city" >

	# <br>

	# <input type="submit" value="Search" >

	# </from>

	# <br>
	# <br>

	# """


	# return HttpResponse(city_state_string) 


def get_post(request):

	text_string = ''

	starts_with = request.Get['state_name']

	states = State.objects.filter(name__startwith=starts_with)

	state_string = ''

	for stae in states:
		state_string += '%s <br>' % state.name 


	return HttpResponse(state_string) 


def first_view(request):

	states = State.objects.all()
	# state_list = []
	text_string = ''

	for state in states:

		cities = state.city_set.filter(name__startwith="A")

		for city in cities:

			text_string += 'state:%s --city:%s <br>' % (state.name, city.name)

	return HttpResponse(text_string) 

def second_view(request):

	states = State.objects.all()
	# state_list = []
	text_string = ''

	for state in states:

		cities = state.city_set.filter(name__startwith='B')

		for city in cities:

			text_string += 'state:%s -- city:%s <br>' % (state.name, city.name)

	return HttpResponse(text_string)

def third_view(request):

	states = State.objects.all()
	# state_list = []
	text_string = ''

	for state in states:

		cities = state.city_set.filter(name__startwith='C')

		for city in cities:

			text_string += 'state:%s -- city:%s <br>' % (state.name, city.name)

		return HttpResponse(text_string)




	# text_string = "This is a string of text."

	

# def state_list(request, letter, sort):
#	states = State.objects.filter(name__startwith=letter).order_by('sort')

#	state_list = []

#	for state in states:
#		states_list.append('%s ,br>' % state.name)



#	return HttpResponse(states_list) 