from django.contrib import admin

from sample.models import Company, BalancingGroup, PowerPlant, Generator

admin.site.register(Company)
admin.site.register(BalancingGroup)
admin.site.register(PowerPlant)
admin.site.register(Generator)
