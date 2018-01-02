from django.contrib import admin
from .models import UserProfile


# admin.site.register(UserProfile)
admin.site.site_header = 'Social Network Administration Panel'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'description', 'city', 'website', 'phone', 'user_info')

    def user_info(self, obj):
        return obj.id,  obj.user, obj.phone

    user_info.short_description = 'info'

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(self)
        queryset = queryset.order_by('-id')  # from big to small
        # queryset = queryset.order_by('id')  # from small to big
        # queryset = queryset.order_by('-phone', 'user')  # from big to small based on phone first
        #  then username based on alphabetic
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)


