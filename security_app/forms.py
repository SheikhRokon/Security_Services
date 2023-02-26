from .models import *
from django import forms

subjects = (
    
    )
class Contactfrom (forms.ModelForm):
    field1 = forms.ModelChoiceField(queryset=Service_Section.objects.all(),empty_label="Choose any Service")

    full_name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Full Name" }))

    email = forms.EmailField(widget= forms.EmailInput(attrs ={
        'class': 'form-control', 'placeholder':"Your Email" }))

    phone = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Phone Number"}))

    company = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Company" }))
    
    satet = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Satet" }))

    topics = forms.ChoiceField(choices=subjects,widget=forms.Select(attrs={
        'class': 'form-select' }))

    massege = forms.CharField(widget= forms.Textarea(attrs={
        'class': 'form-control','placeholder' :"Your Comment" , 'row': 3 }))
    


    class Meta:
        model = Contat
        fields = ['field1','full_name']
       
    






