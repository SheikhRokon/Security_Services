from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index-page' ),
    path('service-us/',service,name='service-page' ),
    path('contact-us/',contact,name='contact-page' ),
    path('blog-us/',blog_page,name='blog-page' ),
    path('about_as-us/',about_as,name='about-page' ),
    path('blog_details-us/',blog_details,name='blog_details-page' ),
    path('board_of_directors-us/',board_of_directors,name='board_of_directors-page' ),
    path('management_term-us/',management_term,name='management_term-page' ),
    path('our_clicnts-us/',our_clicnts,name='our_clicnts-page' ),
    path('clicnts_testimonials-us/',clicnts_testimonials,name='clicnts_testimonials-page' ),
    path('contract_signing-us/',contract_signing,name='contract_signing-page' ),
    path('history-us/',history,name='history-page' ),
    path('news-us/',news,name='news-page' ),
    path('csr-us/',csr,name='csr-page' ),
    path('career-us/',career,name='career-page' ),
    path('photo_gallery-us/',photo_gallery,name='photo_gallery-page' ),
    path('video_gallery-us/',video_gallery,name='video_gallery-page' ),














]
