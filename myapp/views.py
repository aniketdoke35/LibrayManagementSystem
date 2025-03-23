from django.shortcuts import redirect, render
from datetime import datetime 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import Books


def index(request):
   return render(request,'myapp/index.html')


def login_view(request): 
     if (request.method == "POST"):
          email=request.POST.get('email')
          pwd = request.POST.get('password')

          user = User.objects.get(email=email)
          user = authenticate(request, username=user.username, password=pwd)

          if user is  None:
               return render(request,"myapp/login.html",{'err':'invalid credentials'})
          else:
               login(request,user)
               return redirect("main") 
               
     return render(request,'myapp/login.html')

def logout_view(request):
     logout(request)
     return render(request,'myapp/admin.html')





def signup_view(request):
    if request.method == 'POST':
        uname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

       
        if(User.objects.filter(username=uname).exists()):
            return render(request, 'myapp/registration.html', {'err': 'User already exists'})
        
        User.objects.create_user(username=uname, email=email, password=password)

        return redirect("login")

    return render(request, 'myapp/registration.html')

@login_required
def addbook(request):
   if (request.method=="POST"):
      print(request.POST)
      bid= request.POST.get('bid')
      bookName= request.POST.get('bookName')
      author= request.POST.get('author')
      category=request.POST.get('category')
      publishedYear = request.POST.get("publishedYear")  
        

      publishedYear = datetime.strptime(publishedYear, "%Y-%m-%d").date()
      obj = Books(bid=bid, bookName=bookName, author=author, category=category, publishedYear =publishedYear)
      obj.save()
      return redirect('/main/')
   return render(request,'myapp/addbook.html')



@login_required
def main(request):
   db = Books.objects.all()
   context = {'db':db}
   return render(request,'myapp/main.html',context)

@login_required
def delete_view(request,n):
   obj= Books.objects.get(bid=n)
   obj.delete()
   return redirect("/main/")

@login_required
def update_view(request,n):
   obj = Books.objects.get(bid=n)

   if(request.method =='POST'):
      bookName= request.POST.get('bookName')
      author= request.POST.get('author')
      category=request.POST.get('category')
      publishedYear = request.POST.get("publishedYear") 


      obj.bookName = bookName
      obj.author = author
      obj.category = category
      obj.publishedYear = publishedYear
      obj.save()
      return redirect("/main/")  
   context= {"b":obj} 


   return render(request,'myapp/update.html',context)



def myadm(request):
    return render(request,'myapp/admin.html')