from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html', extra_context={'title':'歡迎光臨'}), name='home'),
    path('user/', include('django.contrib.auth.urls')),
    path('developer', TemplateView.as_view(template_name='developer.html')),
    path('teacher/', include('teacher.urls')),
    path('room/', include('room.urls')),
    path('log/', include('log.urls'))
]

# 加入靜態檔案的處理規則
urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)

# 加入使用者上傳檔案的處理規則
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)