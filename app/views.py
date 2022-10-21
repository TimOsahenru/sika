from django.shortcuts import render, redirect
from .models import House, Agent
from .forms import HouseForm, HouseCreate, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import HouseFilter
from django.db.models import Q
from django.core.paginator import Paginator


# ..................... All Houses .......................
def index(request):

    if 'q' in request.GET:
        q = request.GET['q']
        house_query = Q(Q(location__name__icontains=q) | Q(type_of_house__name__icontains=q))
        houses = House.objects.filter(house_query)
    else:
        houses = House.objects.all()
        page = Paginator(houses, 3)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)

    my_filter = HouseFilter(request.GET, queryset=houses)
    houses = my_filter.qs

    # .... temporary solutions to filters-pagination error
    page = Paginator(houses, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {'houses': houses,
               'my_filter': my_filter,
               'page': page}
    return render(request, 'index.html', context)


# ..................... Detail House .......................
def house_detail(request, pk):
    house = House.objects.get(id=pk)

    context = {'house': house}
    return render(request, 'detail.html', context)


# ..................... Agent profile .......................
def agent_profile(request, pk):
    agent = Agent.objects.get(username=pk)
    houses = agent.house_set.all()
    count = houses.count()

    context = {'agent': agent, 'houses': houses, 'count': count}
    return render(request, 'agent-profile.html', context)


# ..................... Update House .......................
@login_required(login_url='login')
def house_update(request, pk):
    house = House.objects.get(id=pk)
    form = HouseForm(instance=house)
    agent = request.user

    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=house)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=agent.username)

    context = {'house': house, 'form': form}
    return render(request, 'edit.html', context)


# ..................... Delete House .......................
@login_required(login_url='login')
def house_delete(request, pk):
    house = House.objects.get(id=pk)
    agent = request.user

    if request.method == 'POST':
        house.delete()
        return redirect('profile', pk=agent.username)

    context = {'house': house}
    return render(request, 'delete.html', context)


# ..................... Create House .......................
@login_required(login_url='login')
def house_create(request):
    form = HouseCreate()
    agent = request.user

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.agent = agent
            house.save()
            return redirect('profile', pk=agent.username)

    context = {'form': form}
    return render(request, 'create.html', context)


# ..................... Login User .......................
def login_user(request):

    if request.user.is_authenticated:
        return redirect('houses')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        agent = authenticate(email=email, password=password)
        if agent is not None:
            login(request, agent)
            return redirect('profile', pk=request.user.username)
        else:
            messages.error(request, 'Email or Password is incorrect')
            return redirect('login')
    context = {}
    return render(request, 'login.html', context)


# ..................... Logout User .......................
def logout_user(request):
    logout(request)
    return redirect('houses')


# ..................... Agent profile update .......................
@login_required(login_url='login')
def profile_update(request):
    agent = request.user
    form = ProfileForm(instance=agent)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=agent.username)
    context = {'form': form}
    return render(request, 'profile-update.html', context)


# ..................... Agent signup .......................
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('houses')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if Agent.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            if Agent.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            else:
                agent = Agent.objects.create_user(username=username, email=email, password=password)
                agent.save()
                return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('signup')
    context = {}
    return render(request, 'signup.html', context)
