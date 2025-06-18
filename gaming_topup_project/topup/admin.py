from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Game, TopUpProduct

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'game_id', 'is_active']
    search_fields = ['name', 'game_id']

@admin.register(TopUpProduct)
class TopUpProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'game', 'price', 'in_game_currency']
    search_fields = ['name', 'game__name']
