from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Banner(models.Model):

    titel = models.CharField(max_length = 150)
    descriptions=models.CharField(max_length = 150)
    image = models.ImageField(upload_to='BannerImage',)
    url_http_link = models.CharField(max_length = 150,blank=True,null=True)
   
    class Meta:

        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        """Unicode representation of Banner."""
        return self.titel

class About(models.Model):
    title = models.CharField( max_length=150)
    descriptions = models.CharField( max_length=150)
    Video_link=models.URLField(max_length=200,blank=True,null=True)


   
    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """Unicode representation of About."""
        return self.title

class Service_Section(models.Model):
    image = models.ImageField(upload_to='ServiceImage',)
    title = models.CharField(max_length=100)
    detalis = models.CharField(max_length=150)
    
        
    def __str__(self):
        return self.title
        
class Contat(models.Model):

    full_name = models.CharField( max_length=150)
    email = models.EmailField( max_length=150)
    phone = models.CharField( max_length=150)
    company = models.CharField( max_length=150)
    satet = models.CharField( max_length=150)
    topics = models.ForeignKey(Service_Section,on_delete=models.CASCADE)
    massege = models.CharField( max_length=500)

    class Meta:
      

        verbose_name = 'contat'
        verbose_name_plural = 'contats'

    def __str__(self):
       
        return self.full_name
class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class Fact_counter(models.Model):

    titel=models.CharField(max_length=150)
    number=models.CharField(max_length=150)

   

    class Meta:
        """Meta definition for Fact_counter."""

        verbose_name = 'Fact_counter'
        verbose_name_plural = 'Fact_counters'

    def __str__(self):
        """Unicode representation of Fact_counter."""
        return self.titel

class Security_information(models.Model):
    image= models.ImageField(upload_to='SecurityInformationImage',null=True)
    top_text= models.CharField(max_length=100,null=True)
    information_title= models.CharField( max_length=500,null=True)
    detalis = models.CharField(max_length=550,null=True)

    class Meta:
        """Meta definition for Security_information."""

        verbose_name = 'Security_information'
        verbose_name_plural = 'Security_informations'

    def __str__(self):
        """Unicode representation of Security_information."""
        return self.top_text

class I_Gave_Protection_L(models.Model):
    title = models.CharField(max_length=200)
    

    class Meta:
        """Meta definition for I_Gave_Protection."""

        verbose_name = 'I_Gave_Protection_L'
        verbose_name_plural = 'I_Gave_Protections_L'

    def __str__(self):
        """Unicode representation of I_Gave_Protection_L."""
        return self.title

class I_Gave_Protection_R(models.Model):
    title = models.CharField(max_length=200)
    

    class Meta:
        """Meta definition for I_Gave_Protection."""

        verbose_name = 'I_Gave_Protection_R'
        verbose_name_plural = 'I_Gave_Protections_R'

    def __str__(self):
        """Unicode representation of I_Gave_Protection_R."""
        return self.title         

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=50)


    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return self.skill_name
        

       


class Team_section(models.Model):
    image= models.ImageField(upload_to='SecurityInformationImage')
    name= models.CharField(max_length=100)
    titel= models.CharField( max_length=100)
    detalis = models.CharField(max_length=250)
    facebook_link = models.CharField(max_length = 150,blank=True,null=True)
    twitter_link = models.CharField(max_length = 150,blank=True,null=True)
    google_plus_link = models.CharField(max_length = 150,blank=True,null=True)


    class Meta:
        """Meta definition for Team_section."""

        verbose_name = 'Team_section'
        verbose_name_plural = 'Team_sections'

    def __str__(self):
        """Unicode representation of Team_section."""
        return self.name

class Testimonial_section(models.Model):
    image= models.ImageField(upload_to='TestimonialSectionImage')
    name= models.CharField(max_length=100)
    titel= models.CharField( max_length=100)
    detalis = models.CharField(max_length=250)

    class Meta:
        """Meta definition for Testimonial_section."""

        verbose_name = 'Testimonial_section'
        verbose_name_plural = 'Testimonial_sections'

    def __str__(self):
        """Unicode representation of Testimonial_section."""
        return self.name

class  Brand_section_Add(models.Model):
    c_name = models.CharField(max_length=100,null=True)
    logo = models.ImageField(upload_to='BrandSectionIogo')
    company_link = models.CharField(max_length = 150,blank=True,null=True)

    class Meta:
        """Meta definition for  Brand_section."""

        verbose_name = ' Brand_section'
        verbose_name_plural = ' Brand_sections'

    def __str__(self):
        """Unicode representation of  Brand_section."""
        return self.c_name

class News_section(models.Model):
    image = models.ImageField(upload_to='News_sectionImage')
    title = models.CharField(max_length=100)
    detalis = models.CharField(max_length=150)
    date = models.CharField(max_length=100,null=True)
    
    class Meta:
        """Meta definition for News_section."""

        verbose_name = 'News_section'
        verbose_name_plural = 'News_sections'

    def __str__(self):
        """Unicode representation of News_section."""
        return self.title

class Our_blog(models.Model):
    image = models.ImageField(upload_to='Our_blogImage')
    title = models.CharField(max_length=100)
    detalis = models.CharField(max_length=150)
    date = models.CharField(max_length=100,null=True)    
    class Meta:
     

        verbose_name = 'Our_blog'
        verbose_name_plural = 'Our_blogs'

    def __str__(self):
     
        return self.title        

class Footer_section(models.Model):
    image = models.ImageField(upload_to='Our_blog')
    detalis = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    email =models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length = 150,blank=True,null=True)
    instagram_link = models.CharField(max_length = 150,blank=True,null=True)
    twitter_link = models.CharField(max_length = 150,blank=True,null=True)
    google_plus_link = models.CharField(max_length = 150,blank=True,null=True)


   

    class Meta:
        """Meta definition for Footer_section."""

        verbose_name = 'Footer_section'
        verbose_name_plural = 'Footer_sections'

    def __str__(self):
        """Unicode representation of Footer_section."""
        return self.phone



class Other_Page_Image(models.Model):
    image = models.ImageField(upload_to='Other_Image',blank=True)
    Image_Name = models.CharField(max_length=50,blank=True)

    class Meta:
        verbose_name_plural = 'Other_Page_Images'

    def __str__(self):
        """Unicode representation of Other_Page_Image."""
        return self.Image_Name

class Board_of_directors(models.Model):

    name = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='BoardOfDirectors',)
    first_part = models.TextField(blank = True)
    secend_part = models.TextField(blank = True)
    
    class Meta:
       

        verbose_name = 'Board_of_directors'
        verbose_name_plural = 'Board_of_directorss'

    def __str__(self):
       
        return self.name
        