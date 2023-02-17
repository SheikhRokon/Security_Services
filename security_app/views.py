from django.shortcuts import render
from .models import *
from django.db.models import Q
from .forms import *
# from django.contrib.auth.decorators import login_required  get_object_or_404,redirect
# from django.contrib import messages
# from django.utils import timezone

# Create your views here.
def base(request):
    return render(request,'security_app/base.html')



# Create your views here.
def index(request):
    banner = Banner.objects.all()
    about = About.objects.all().order_by("-id")[:1]
    service_section = Service_Section.objects.all()
    fact_counter = Fact_counter.objects.all().order_by("-id")[:4]
    security_information = Security_information.objects.last()
    team_section = Team_section.objects.all()
    testimonial_section = Testimonial_section.objects.all()
    brand_section_add = Brand_section_Add.objects.all()
    news_section = News_section.objects.all()
    footer_section = Footer_section.objects.all().order_by("-id")[:1]
    i_Gave_Protection_l = I_Gave_Protection_L.objects.all().order_by("-id")[:3]
    i_Gave_Protection_r = I_Gave_Protection_R.objects.all().order_by("-id")[:3]
    skill = Skill.objects.all().order_by("-id")[:3]



    if request.method == 'POST':
        forms = Contactfrom(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('index-page')
    else:
        forms = Contactfrom()

    context ={
        'banner':banner,
        'about':about,
        'forms':forms,
        'service_section':service_section,
        'fact_counter':fact_counter,
        'security_information':security_information,
        'team_section':team_section,
        'testimonial_section':testimonial_section,
        'brand_section_add':brand_section_add,
        'news_section':news_section,
        'footer_section':footer_section,
        'i_Gave_Protection_l':i_Gave_Protection_l,
        'i_Gave_Protection_r':i_Gave_Protection_r,
        'skill':skill,

    }
    
    return render(request,'security_app/index.html',context)    

def service(request):
    return render(request,'security_app/service.html')  

def contact(request):
    return render(request,'security_app/contact.html') 
          
def about_as(request):
    return render(request,'security_app/about_as.html')  

def blog_page(request):
    our_blog = Our_blog.objects.all()

    context={
        'our_blog':our_blog,

    }
    return render(request,'security_app/blog.html',context)       

def blog_details(request):
    return render(request,'security_app/blog_details.html') 

def board_of_directors(request):
    board_of_directors= Board_of_directors.objects.all()

    context={
        'board_of_directors':board_of_directors
    }
    return render(request,'security_app/board_of_directors.html',context) 

def management_term(request):
    return render(request,'security_app/management_term.html') 

def our_clicnts(request):
    return render(request,'security_app/our_clicnts.html') 

def clicnts_testimonials(request):
    return render(request,'security_app/clicnts_testimonials.html')   

def contract_signing(request):
    return render(request,'security_app/contract_signing.html')     


def history(request):
    return render(request,'security_app/history.html')  

def news(request):
    return render(request,'security_app/news.html')

def csr(request):
    return render(request,'security_app/csr.html')          

def career(request):
    return render(request,'security_app/career.html') 

def photo_gallery(request):
    return render(request,'security_app/photo_gallery.html')   

def video_gallery(request):
    return render(request,'security_app/video_gallery.html')




