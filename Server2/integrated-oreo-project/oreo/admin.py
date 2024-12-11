from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    # list_display에서 사용하려는 필드를 실제 모델 필드명으로 수정
    list_display = ( 'email', 'real_name', 'nickname')  # 이메일을 email로 수정
    search_fields = ('email', 'user_id', 'real_name')  # 검색 필드에 'email' 포함

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
