from django.contrib import admin

# Register your models here.


from app.models import *

admin.site.register(user)
admin.site.register(friends)

admin.site.register(messages)
admin.site.register(ChatRoom)
admin.site.register(BlockUser)
