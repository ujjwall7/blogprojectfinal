from dataclasses import dataclass
from email.mime import image
from multiprocessing import context
import os
from urllib import request
from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import *
from .forms import SignupForm,BlogForms,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
 


#signup_form
def sign_up(request):
    if request.method=="POST":
         fm=SignupForm(request.POST)
         if fm.is_valid():

            fm.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
            
    else:
        fm = SignupForm()          
    
    return render(request,"signup.html",{'form':fm})







def login_form(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'login successfully')
                    return redirect('about')
                    
        else:
            fm=AuthenticationForm()
        return render(request,"login.html",{'form':fm})

    else:
        return redirect('about')



def userlogoutt(request):
    logout(request)
    return HttpResponseRedirect('/')



def about(request):
    user=request.user
    # post=Blog.objects.filter(user=user).order_by('-id')
    # return render(request,"myblogs.html",{'post':post})
    blog= None
    categories = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        post = Blog.get_all_Blog_by_id(categoryID) 
    else:
        # blog = Blog.get_all_Blog();
        post=Blog.objects.filter(user=user).order_by('-id')


    data = {} 
    data['post'] = post 
    data['categories'] = categories

    return render(request,'myblogs.html',data)


def fdepth(request,pk):
        post=Blog.objects.get(id=pk)
        return render(request,"dpost.html",{'post':post})


def read(request,pk):
    post=Blog.objects.get(id=pk)
    return render(request,"blogread.html",{'post':post})


def contact(request):
    if request.user.is_authenticated:
        return render(request,"contact.html")
    else:
        return redirect('login')

def front(request):
    blog= None
    blogfinalpage=None
    totalpage=None
    total=None

    categories = Category.get_all_categories()

    categoryID = request.GET.get('category')
    if categoryID:
        blog = Blog.get_all_Blog_by_id(categoryID) 
        paginator = Paginator(blog, 5)
        page_number = request.GET.get('page')
        blogfinalpage = paginator.get_page(page_number)
        totalpage=blogfinalpage.paginator.num_pages
        total=[n+1 for n in range(totalpage)]
    else:
        blog = Blog.objects.all()
        blog = Blog.objects.all()
        paginator = Paginator(blog, 5)
        page_number = request.GET.get('page')
        blogfinalpage = paginator.get_page(page_number)
        totalpage=blogfinalpage.paginator.num_pages
        total=[n+1 for n in range(totalpage)]
        
    data = {} 
    data['blog'] = blog 
    data['categories'] = categories
    data['blog'] = blogfinalpage
    data['lastpage'] = totalpage
    data['totalpagelist'] = total

    return render(request,'front.html',data)

#original
# def front(request):
#     blog= None

#     blog = Blog.objects.all()

#     categories = Category.get_all_categories()

#     categoryID = request.GET.get('category')
#     if categoryID:
#         blog = Blog.get_all_Blog_by_id(categoryID) 
#     else:
#         blog = Blog.objects.all()
        
#     data = {} 
#     data['blog'] = blog 
#     data['categories'] = categories


#     return render(request,'front.html',data)







def post(request):
    return render(request,"post.html")
    

# def blog(request):
    
#     return render(request,'contact.html',{'fm':fm})

def save_blog(request):
    if request.method=="POST":
        newblog=BlogForms(request.POST,request.FILES)
        if newblog.is_valid():
            nblog=newblog.save(commit=False)
            nblog.user = request.user
            nblog.save()
            return redirect('about')
    else:
        fm=BlogForms()
        return render(request,'contact.html',{'fm':fm})


@login_required
# update view for details
def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Blog    , id = id)
        
    # pass the object as instance in form
    form = BlogForms(data=(request.POST or None),
    files=(request.FILES or None),
    instance=obj,)


    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("front")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update.html", context)

@login_required
def destroy(request,id):
    blogdata=Blog.objects.get(id=id)
    blogdata.delete()


def profile(request):
    context = {
        'user' : request.user
    }
    return render(request,'newprofile.html',context)


def user_edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                # messages.success(request, 'Profile Updated !!!')
                fm.save() 
                return redirect('blogs')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render (request, 'editprofile.html', {'name' : request.user, 'form' : fm}) 
    else:
        return HttpResponseRedirect('login')

    

# Change Password with old Password 
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Updated !!!')

                return HttpResponseRedirect('changedprofileshowdata')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('login')

