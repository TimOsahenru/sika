from django.shortcuts import render, redirect
from .models import User
from .models import House, Area, HouseType
from .forms import HouseForm, MyCreationForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import HouseFilter
# Create your views here.


@login_required(login_url='login')
def user_profile(request, pk):

    user = User.objects.get(id=pk)
    my_houses = user.house_set.all()

    context = {'user': user, 'my_houses': my_houses}
    return render(request, 'profile.html', context)

# ----------------End of user_profile---------------------


@login_required(login_url='login')
def user_profile_update(request):
    form = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('useraccount', pk=request.user.id)

    context = {'form': form}
    return render(request, 'profile-update.html', context)

# ----------------End of user_profile---------------------


def register_user(request):
    form = MyCreationForm()

    if request.method == 'POST':
        form = MyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Incorrect credentials')
            return redirect('register')

    context = {'form': form}
    return render(request, 'login_register.html', context)

# ----------------End of register_user---------------------


def login_user(request):
    page = 'login'

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Later redirect them to their profile page
            return redirect('houses')
        else:
            messages.error(request, 'Email or Password incorrect')

    context = {'page': page}
    return render(request, 'login_register.html', context)

# ----------------End of login_user---------------------


def logout_user(request):

    logout(request)
    return redirect('login')

# ----------------End of logout_user---------------------


def house_list(request):
    # keyword_search = request.GET.get('keyword_search') if request.GET.get('keyword_search') != None else ''
    # houses = House.objects.filter(Q(area__name__icontains=keyword_search) | Q(house_type__name__icontains=keyword_search) | Q(price__icontains=keyword_search))

    houses = House.objects.all()

    my_filter = HouseFilter(request.GET, queryset=houses)
    houses = my_filter.qs

    page = Paginator(houses, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {'houses': houses,
               'page': page,
               'my_filter': my_filter}
    return render(request, 'index.html', context)

# ----------------End of house_list---------------------


def house_detail(request, pk):

    house = House.objects.get(id=pk)

    context = {'house': house}
    return render(request, 'detail.html', context)

# ----------------End of house_detail---------------------


@login_required(login_url='login')
def house_create(request):

    areas = Area.objects.all()
    house_types = HouseType.objects.all()

    form = HouseForm()

    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.agent = request.user
            house.save()
            return redirect('houses')

    context = {'form': form,
               'areas': areas,
               'house_types': house_types}
    return render(request, 'create.html', context)

# ----------------End of house_create---------------------


@login_required(login_url='login')
def house_edit(request, pk):

    house = House.objects.get(id=pk)
    form = HouseForm(instance=house)

    if request.method == 'POST':
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('house', pk=house.id)

    context = {'form': form}
    return render(request, 'edit.html', context)

# ----------------End of house_create---------------------


@login_required(login_url='login')
def house_delete(request, pk):
    house = House.objects.get(id=pk)

    if request.method == 'POST':
        house.delete()
        return redirect('houses')

    context = {'house': house}
    return render(request, 'delete.html', context)

# ----------------End of house_delete---------------------
