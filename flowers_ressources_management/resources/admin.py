from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Reference)
admin.site.register(Category)
admin.site.register(Loan)
admin.site.register(State)