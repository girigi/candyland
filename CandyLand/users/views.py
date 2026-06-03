from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm, UserUpdateForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# def profile_page(request, pk):
#     template = 'registration/login.html'
#     page_user = get_object_or_404(Profile, user__id=pk)
#     context = {'page_user': page_user}
#     return render(request, template, context)


@login_required
def profile_view(request, username=None):
    """Просмотр профиля пользователя"""
    template = 'profile/user_profile.html'
    if username:
        profile_user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=profile_user)
        is_owner = request.user == profile_user
    else:
        profile = get_object_or_404(Profile, user=request.user)
        profile_user = request.user
        is_owner = True

    context = {
        'profile': profile,
        'profile_user': profile_user,
        'is_owner': is_owner
    }
    return render(request, template, context)

@login_required
def edit_profile(request):
    """Редактирование профиля"""
    template = 'profile/user_profile.html'
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлён!')
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, template, context)


@login_required
def delete_avatar(request):
    """Удаление аватара"""
    if request.method == 'POST':
        profile = request.user.profile
        if profile.avatar:
            profile.avatar.delete()
            profile.avatar = None
            profile.save()
            messages.success(request, 'Аватар успешно удалён')
    return redirect('edit_profile')


@login_required
def update_field(request):
    """Динамическое обновление полей профиля через AJAX"""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Недопустимый метод запроса.'}, status=400)

    field = request.POST.get('field')
    value = request.POST.get('value', '').strip()

    if field == 'username':
        if not value:
            return JsonResponse({'status': 'error', 'message': 'Имя пользователя не может быть пустым.'}, status=400)

        # Проверяем, не занят ли username другим пользователем
        if User.objects.filter(username=value).exclude(id=request.user.id).exists():
            return JsonResponse({'status': 'error', 'message': 'Этот никнейм уже занят.'}, status=400)

        # Сохраняем новое имя в модель User
        request.user.username = value
        request.user.save()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Неизвестное поле.'}, status=400)


@login_required
def exit_profile(request):
    """Выход из профиля"""
    template = 'registration/login.html'
    return render(request, template)


def register(request):
    template = 'registration/register.html'
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        avatar = request.FILES.get('avatar')

        if form.is_valid():
            user = form.save()

            # Создаем профиль
            profile, created = Profile.objects.get_or_create(user=user)
            profile.name_user = form.cleaned_data['username']
            profile.email_user = form.cleaned_data['email']

            if avatar:
                profile.avatar = avatar

            profile.save()

            # Автоматически входим после регистрации
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно! Добро пожаловать!')
            return redirect('profile:profile_view')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}

    return render(request, template, context)
