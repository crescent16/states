from django.contrib import admin

# Register your models here.

from app.models import State, StateCapital, City


class StateAdmin(admin.ModelAdmin):
	list_display = ("name", "abbreviation",)
	search_fields = ['name']

admin.site.register(State, StateAdmin)


admin.site.register(StateCapital)
admin.site.register(City)
