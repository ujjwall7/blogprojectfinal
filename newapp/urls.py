from django.urls import path
from . import views

urlpatterns = [
    path('',views.front,name="front"),
    # path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('post',views.post,name="post"),
    # path('blog',views.blog,name="blog"),
    path('save_blog',views.save_blog,name="save_blog"),

    path('fdepth/<int:pk>/',views.fdepth,name="fdepth"),
    path('read/<int:pk>/',views.read,name="read"),


    path('signup',views.sign_up,name="sign_up"),
    path('login',views.login_form,name="login"),
    path('logoutt',views.userlogoutt,name="userlogout"),
    path('update/<int:id>',views.update,name="update"),
    # path('save/<int:id>',views.save,name="save"),
    path('destroy/<int:id>',views.destroy,name="destroy"),
    path('changedprofileshowdata/',views.profile,name="blogs"),
    path('editpage/',views.user_edit_profile,name="editprofile"),
    path('changepassword',views.user_change_pass,name="password"),

    

    
]