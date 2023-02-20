from .models import *

def G_services(requrest):
    g_service_s = Service_Section.objects.all()

    context={

        'g_service_s':g_service_s
    }
    return context

def G_security_information(requrest):
    g_service_info = Security_information.objects.all().order_by("-id")[:1]

    context={

        'g_service_info':g_service_info
    }
    return context   

def G_Gave_Protection_R(requrest):
    g_Gave_Protection_R = I_Gave_Protection_R.objects.all().order_by("-id")[:3]

    context={

        'g_Gave_Protection_R':g_Gave_Protection_R
    }
    return context    

def G_Gave_Protection_L(requrest):
    g_Gave_Protection_L = I_Gave_Protection_L.objects.all().order_by("-id")[:3]

    context={

        'g_Gave_Protection_L':g_Gave_Protection_L
    }
    return context    

def G_Skill(requrest):
    g_Skill = Skill.objects.all().order_by("-id")[:3]

    context={

        'g_Skill':g_Skill
    }
    return context    



def G_contact(requrest):
    g_contact = Header_and_Footer.objects.all()
    print(g_contact)

    context={

        'g_contact':g_contact
    }
    return context    

def G_Team_section(requrest):
    g_Team_section = Team_section.objects.all().order_by("-id")[:4]

    context={

        'g_Team_section':g_Team_section
    }
    return context        

def G_Brand_section_Add(requrest):
    g_Brand_section_Add = Brand_section_Add.objects.all().order_by("-id")[:5]

    context={

        'g_Brand_section_Add':g_Brand_section_Add
    }
    return context     

def G_news(requrest):
    g_news = News_section.objects.all()

    context={

        'g_news':g_news
    }
    return context      

def G_Other_Page_Image(requrest):
    g_Other_Page_Image = Other_Page_Image.objects.all().order_by("-id")[:1]

    context={

        'g_Other_Page_Image':g_Other_Page_Image
    }
    return context    

