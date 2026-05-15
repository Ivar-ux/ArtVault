from django.contrib import admin
from .models import Profile, Seller, Artwork, Bid, Finalization

admin.site.register(Profile)
admin.site.register(Seller)
admin.site.register(Artwork)
admin.site.register(Bid)
admin.site.register(Finalization)