from django.contrib import admin

from .models import Game, Highlight, UpcomingSchedule, RecentGame

admin.site.register(Game)
admin.site.register(Highlight)
admin.site.register(UpcomingSchedule)
admin.site.register(RecentGame)
