from django.contrib import admin
from travel.models import Tuser, Treview, Travel

# Register your models here.
class TuserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_pwd')
    # 아이디 : admin 비밀번호 : 123

admin.site.register(Tuser, TuserAdmin)
admin.site.register(Treview)
admin.site.register(Travel)