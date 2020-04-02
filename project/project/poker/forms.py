from django import forms

class KakikomiForm(forms.Form):
    action_name = forms.CharField()

    def send_text(self):
        pass

