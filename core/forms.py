from django import forms
from .models import Bid

from .models import Finalization


class FinalizationForm(forms.ModelForm):
    class Meta:
        model = Finalization
        fields = ['street_address', 'city', 'postal_code', 'country', 'national_id']
class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }