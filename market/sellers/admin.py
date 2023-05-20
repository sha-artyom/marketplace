from django.contrib import admin, messages
from django.utils.translation import ngettext
from market.sellers.models import Factory, PrivateBusinessman, RetailNetwork, Product
from django.urls import reverse
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_filter = ("title",)


@admin.action
def clean_debt(modeladmin, request, queryset):
    updated = queryset.update(debt=0)
    modeladmin.message_user(
        request,
        ngettext(
            "%d задолженность была обнулена.",
            "%d задолженности были обнулены.",
            updated,
        )
        % updated,
        messages.SUCCESS,
    )


@admin.register(PrivateBusinessman)
class PrivateBusinessmanAdmin(admin.ModelAdmin):
    list_display = ("title", "provider_link",)
    readonly_fields = ("provider_link",)
    ordering = ("title",)
    actions = (clean_debt,)
    list_filter = ("city",)

    def provider_link(self, businessman):
        if businessman.provider in Factory.objects.all():
            url = reverse("admin:sellers_factory_change", args=[businessman.provider.id])
        else:
            url = reverse("admin:sellers_retailnetwork_change", args=[businessman.provider.id])
        link = '<a href="%s">%s</a>' % (url, businessman.provider.title)
        return mark_safe(link)

    provider_link.short_description = 'Поставщик'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ("title", "provider_link",)
    readonly_fields = ("provider_link",)
    ordering = ("title",)
    actions = (clean_debt,)
    list_filter = ("city",)

    def provider_link(self, retailer):
        url = reverse("admin:sellers_factory_change", args=[retailer.provider.id])
        link = '<a href="%s">%s</a>' % (url, retailer.provider.title)
        return mark_safe(link)

    provider_link.short_description = 'Поставщик'


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    ordering = ("title",)
    list_filter = ("city",)
