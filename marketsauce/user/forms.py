from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Profile


class SignupForm(forms.Form):
    nickname = forms.CharField(label=_('nickname'),
                                 max_length=30,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('nickname'), }))
    phone = forms.CharField(label=_('Phone number'),
                            max_length=30,
                            widget=forms.TextInput(
                                attrs={'placeholder':
                                           _('Phone number'), }))                   

    def signup(self, request, user):
        user.save()
        profile = Profile()
        profile.user = user
        profile.phone = self.cleaned_data['phone']
        profile.nickname = self.cleaned_data['nickname']
        profile.save() 