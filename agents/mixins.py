from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect



class OrganisorAndLoginRequiredMixin(AccessMixin):
    """Joriy foydalanuvchi autentifikatsiya qilinganligini tekshiring. va tashkilot ekanligini ham"""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not  request.user.is_organisor:
            return redirect('user:login')
        return super().dispatch(request, *args, **kwargs)



