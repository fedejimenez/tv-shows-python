from django import forms
from django.conf import settings
import requests

class DictionaryForm(forms.Form):
    name = forms.CharField(max_length=100)

    def search(self):
        result = {}
        name = self.cleaned_data['name']
        endpoint = 'http://api.tvmaze.com/singlesearch/shows?q={name_id}'
        url = endpoint.format(source_lang='en', name_id=name)
        response = requests.get(url)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % name
            else:
                result['message'] = 'The API is not available at the moment. Please try again later.'
        return result 

