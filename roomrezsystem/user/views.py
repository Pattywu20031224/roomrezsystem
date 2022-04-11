from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import *
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Subquery
from django import forms
from .models import *


# 限定管理員才允許操作的混成類別
class SuperuserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
# 使用者註冊
class UserRegister(CreateView):
    extra_context = {'title': '使用者註冊'}
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'form.html'
    success_url = reverse_lazy('home')  # 註冊完成返回首頁

    # 取得要顯示的表單內容
    def get_form(self):
        form = super().get_form()
        form.fields['first_name'].label = '真實姓名'
        form.fields['first_name'].required = True
        form.fields['last_name'].label = '學校名稱'
        form.fields['last_name'].required = True
        form.fields['password2'] = forms.CharField(label='密碼驗證', max_length=255)
        return form

    # 表單驗證
    def form_valid(self, form):
        user = form.save(commit=False)
        pw1 = form.cleaned_data['password']
        pw2 = form.cleaned_data['password2']
        if pw1 != pw2:
            form.add_error('password2', '密碼與驗證密碼不相符')
            return super().form_invalid(form)
        user.set_password(pw1)
        return super().form_valid(form)
# 使用者列表
class UserList(SuperuserRequiredMixin, ListView):
    extra_context = {'title': '使用者列表'}
    model = User
    ordering = ['username']
    paginate_by = 20
    template_name = 'user/user_list.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('groups')
class UserView(SuperuserRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'tuser'
class UserEdit(SuperuserRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'

    def get_form(self):
        form = super().get_form()
        form.fields['first_name'].label = '真實姓名'
        form.fields['first_name'].required = True
        form.fields['last_name'].label = '班級座號'
        form.fields['last_name'].required = True
        return form
class UserPasswordUpdate(SuperuserRequiredMixin, UpdateView):
    model = User
    fields = ['password']
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'

    def get_form(self):
        form = super().get_form()
        form.fields['password2'] = forms.CharField(label='密碼驗證', max_length=255)
        return form
    
    def get_initial(self):  # 指定初始值來清掉密碼輸入欄位的原始值
        return {'password': ''}
    
    def form_valid(self, form):
        user = form.save(commit=False)
        pw1 = form.cleaned_data['password']
        pw2 = form.cleaned_data['password2']
        if pw1 != pw2:
            form.add_error('password2', '密碼與驗證密碼不相符')
            return super().form_invalid(form)
        user.set_password(pw1)
        return super().form_valid(form)
class UserTeacherToggle(SuperuserRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['uid'])
        try :
            group = Group.objects.get(name="teacher")	
        except ObjectDoesNotExist :
            group = Group(name="teacher")
            group.save()

        if user.groups.filter(name='teacher').exists():
            group.user_set.remove(user)
        else: 
            group.user_set.add(user)
        return self.request.META.get('HTTP_REFERER', '/')
class UserDashboard(LoginRequiredMixin, TemplateView):
    extra_context = {'title': '我的儀表板'}
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tuser'] = self.request.user
        return ctx
