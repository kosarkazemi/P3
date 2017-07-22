from django.conf.urls import url
from django.contrib import admin
from author.views import *
from blog.views import *



urlpatterns = (
    #author
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^register/', register_page , name='register'),
    url(r'^logout/$', logout_page , name='logout'),
    url(r'^auth/login/$', login_page),
    url(r'^auth/blog_id/$', blog_id_get),

    #blog
    url(r'^blog/(\d)/posts/$', get_posts),
    url(r'^blog/(\d)/post/$', post),
    url(r'^blog/(\d)/comments/$', get_comments),
    url(r'^blog/(\d)/comment/$', comment),

    #search
    url(r'^search/blog/$',search),

    #static files
    # url(r'^blog/(\d)$',None ) ### TODO
    url(r'^login/$', login_page_static , name='login')

)





