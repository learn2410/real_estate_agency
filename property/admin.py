from django.contrib import admin

from .models import Flat, Conplaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ('owner',)
    verbose_name = "Собственник"
    verbose_name_plural = "Собственники"

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


class ConplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('problem_flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Conplaint, ConplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
