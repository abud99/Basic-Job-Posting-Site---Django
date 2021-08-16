from django.contrib import admin

from .models import reviews
from .models import job
from .models import transactions

# Register your models here.

admin.site.register(reviews)
admin.site.register(job)
admin.site.register(transactions)
