from django.contrib.auth import logout
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from order_module.models import Order
from .forms import *

from account_module.models import User
from .forms import EditProfileModelForm


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form,
            'current_user': current_user,
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')


class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        current_user: User = User.objects.filter(id=request.user.id).first()
        context = {
            'form': ChangePasswordForm(),
            'current_user': current_user

        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data['current_password']):
                current_user.set_password(form.cleaned_data['new_password'])
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('current_password', 'کلمه عبور فعلی وارد شده صحیح نمیباشد.')
        context = {
            'form': form,
            'current_user': current_user
        }
        return render(request, 'user_panel_module/change_password_page.html', context)


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket.html', context)


def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)

    detail = current_order.orderdetail_set.filter(id=detail_id).first()
    if detail is None:
        return JsonResponse({
            'status': 'detail_not_found',
        })
    detail.delete()
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)

    total_amount = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })
