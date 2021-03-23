from django import forms
CHART_CHOICES =(
    ('Bar Chart', 'Bar Chart'),
    ('Pie Chart', 'Pie Chart'),
    ('Line Chart', 'Line Chart'),
)
class SalesSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_to= forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)