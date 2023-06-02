from django.shortcuts import render ,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
# Create your views here.

# html pages

def home(request):
    return render(request,"home/home.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request , 'Please Fill The Form Correctly')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request , 'Message ha been sent')

    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts=Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allpostsAuthor =Post.objects.filter(author__icontains=query)
        allposts = allpostsTitle.union(allpostsContent,allpostsAuthor)

    if allposts.count() == 0:
        messages.warning(request , 'No Search Result Found')
    params = {'allposts':allposts ,'query':query}
    return render(request ,"home/search.html",params)

# authenticate apis

def handleSignup(request):
    if request.method == 'POST': 
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # check for errorneous inputs

        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request , 'account has been created-')
        return redirect('home')

    else:
        return HttpResponse('wrong')
    
def handleLogin(request):
    if request.method == 'POST': 
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername,password = loginpass)

        if user is not None:
            login(request ,user)
            messages.success(request , 'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request , 'invalid credentials')
            return redirect ('home')

    return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request , 'Succesfully logged out')
    return redirect('home')
    # return HttpResponse('logout')



