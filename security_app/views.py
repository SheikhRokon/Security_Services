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
    news_section = News_section.objects.all()
    footer_section = Header_and_Footer.objects.all().order_by("-id")[:1]
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

def news_details(request,pk):
    news_details=News_section.objects.get(pk=pk)

    context={
        'news_details':news_details,
    }

    return render(request,'security_app/news_details.html',context) 

def board_of_directors(request):
    board_of_directors= Board_of_directors.objects.all().order_by("-id")[:1]

    context={
        'board_of_directors':board_of_directors
    }
    return render(request,'security_app/board_of_directors.html',context) 

def management_term(request):
    management_term= Management_term.objects.all()

    context={
        'management_term':management_term
    }
    return render(request,'security_app/management_term.html',context) 

def our_clicnts(request):
    brand_section_add = Brand_section_Add.objects.all()

    context={
        'brand_section_add':brand_section_add
    }
    return render(request,'security_app/our_clicnts.html',context) 

def clicnts_testimonials(request):
    clicnts_testimonials = Clicnts_testimonials.objects.all()

    context={
        'clicnts_testimonials':clicnts_testimonials
    }
    return render(request,'security_app/clicnts_testimonials.html',context)   

def contract_signing(request):
    contract_signing = Contract_signing.objects.all()

    context={
        'contract_signing':contract_signing
    }

    return render(request,'security_app/contract_signing.html',context)     


def history(request):
    history = History.objects.all().order_by('-id')[:1]

    context={
        'history':history
    }

    return render(request,'security_app/history.html',context)  

def services_details(request,pk):
    services_details = Service_Section.objects.get(pk=pk)

    context={
        'services_details':services_details
    }

    return render(request,'security_app/services_details.html',context)

def news(request):
    
    return render(request,'security_app/news.html')

def csr(request):
    csr_add_page= CSR_add_page.objects.all()

    context={
        'csr_add_page':csr_add_page
    }
    return render(request,'security_app/csr.html',context)

def csr_details(request, pk ):
    csr_details= CSR_add_page.objects.get(pk=pk)

    context={
        'csr_details':csr_details
    }
    return render(request,'security_app/csr_details.html',context)

def career(request):
    job_post=Job_Post.objects.all()

    context={
        'job_post':job_post
    }
    return render(request,'security_app/career.html',context) 

def photo_gallery(request):
    photo_gallery=Photo_gallery.objects.all()

    context={
        'photo_gallery':photo_gallery
    }
    return render(request,'security_app/photo_gallery.html',context)   

def video_gallery(request):

    video_gallery=Video_gallery.objects.all()

    context={
        'video_gallery':video_gallery
    }
    return render(request,'security_app/video_gallery.html',context)


def notice(request):
    return render(request, 'security_app/notice.html')    

def certifieateverification(request):
    return render(request, 'security_app/certifieateverification.html')
