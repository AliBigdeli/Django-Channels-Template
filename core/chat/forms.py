from django import forms

class ChatCreateForm(forms.Form):
    chat_room_name = forms.CharField(required=True)
    display_name = forms.CharField(required=True)