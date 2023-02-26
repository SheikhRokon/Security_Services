from .models import *
from django import forms

subjects = (
        
        ('django Web Application', 'Service-1'),    
        ('django Web Application', 'Service-2'),
    
    )
class Contactfrom (forms.ModelForm):
    
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
        fields = '__all__'

class Contactfrom (forms.ModelForm):
    
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
        fields = '__all__'        

    






