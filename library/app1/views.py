from django.shortcuts import render,redirect
from.models import Signup,Book,Issue
from django.http import HttpResponse
# Create your views here.

def view(request):
    return render(request,'signup.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        data = Signup.objects.create(name=name,phone=phone,email=email,username=username,password=password,type=1)
        data.save()
        return render(request,'signin.html')



def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            data = Signup.objects.get(username=username)
            if data.password == password:
                request.session['id'] = data.id                                 #session created to continue
                if data.type == 1:
                 return redirect(bookstore)
                else:
                    return redirect(librarian)
            else:
                return  HttpResponse("PASSWORD ERROR")
        except Exception:
            return HttpResponse("USERNAME ERROR")
    else:
        return render(request, 'signin.html')




def signout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(signin)





def signuptosignin(request):
    return redirect(signin)

def signintosignup(request):
    return redirect(view)



def bookstore(request):
    if 'id' in request.session:
     userid = request.session['id']
     user = Signup.objects.get(id=userid)
     data = Book.objects.all()
    # data1 = Book.objects.get()
    return render(request,'bookstore.html',{'data':data,'user':user})


def changepassword(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method == "POST":
            password = request.POST['password']
            newpass = request.POST['newpass']
            try:
                data1 = Signup.objects.get(id=user)
                if data1.password == password:
                    data1.password = newpass
                    data1.save()
                    return render(request,'passchangedview.html')
                else:
                     return HttpResponse("password error")
            except Exception:
              return HttpResponse("username error")
        else:
            return redirect(changepassword)



def passview(request):
    return render(request,'passview.html')







def bookstore(request):
    if 'id' in request.session:
        userid = request.session['id']
        user = Signup.objects.get(id=userid)
        data = Book.objects.all()
        context={
            'data': data,
            'user': user
        }
        return render(request,'bookstore.html',context)
    else:
        return redirect(signin)



def librarian(request):
    data=Book.objects.all()
    return render(request,'librarian.html',{'data':data})

def addbookview(request):
    return render(request,'addbookview.html')

def addbook(request):
    if request.method == 'POST':
        bookname = request.POST['bookname']
        author = request.POST['author']
        genre = request.POST['genre']
        description = request.POST['description']
        bookcover = request.FILES['bookcover']
        booklink = request.POST['booklink']
        buylink = request.POST['buylink']
        data = Book.objects.create(bookname=bookname, author=author, genre=genre,description=description,bookcover=bookcover,booklink=booklink,buylink=buylink)
        data.save()
        return render(request, 'addbooksuccess.html')



def editbooksuccess(request):
    return render(request, 'editbooksuccess.html')



def editbook(request,id):
    data = Book.objects.get(id=id)
    if request.method == "POST":
        newbookname = request.POST['newbookname']
        newauthor = request.POST['newauthor']
        newgenre = request.POST['newgenre']
        newdescription = request.POST['newdescription']
        newbookcover = request.POST['newbookcover']
        newbooklink = request.POST['newbooklink']
        newbuylink = request.POST['newbuylink']

        try:
            data = Book.objects.get(id=id)
            if data.id == id:
                data.bookname = newbookname
                data.author = newauthor
                data.genre = newgenre
                data.description = newdescription
                data.bookcover = newbookcover
                data.booklink = newbooklink
                data.buylink = newbuylink
                data.save()
                return redirect(editbooksuccess)
            else:
                return HttpResponse("Book not Found")
        except Exception:
            return HttpResponse("Check the Book name")
    else:
        return render(request, 'editbookview.html', {'data':data})


def deletebook(request, id):
  data = Book.objects.get(id=id)
  data.delete()
  return redirect(librarian)





def editprofilesuccess(request):
    return render(request, 'editprofilesuccess.html')
def editprofileview(request):
    return render(request,'editprofileview.html')
def editprofile(request):
    if request.method == "POST":
        if 'id' in request.session:
            user = request.session['id']
            password = request.POST['password']
            newname = request.POST['newname']
            newphone = request.POST['newphone']
            newemail = request.POST['newemail']
            try:
                data=Signup.objects.get(id=user)
                print(data)
                if data.password==password:
                     data.name=newname
                     data.phone=newphone
                     data.email=newemail
                     data.save()
                     return render(request,'editprofilesuccess.html')
                else:
                    return HttpResponse("Password Incorrect")
            except Exception:
                 return HttpResponse("error")
    else:
         return render(request, 'editprofileview.html')

def changepassword(request):
    if 'id' in request.session:
        user=request.session['id']
        if request.method == "POST":
            password = request.POST['password']
            newpass = request.POST['newpass']
            try:
                data1 = Signup.objects.get(id=user)
                if data1.password == password:
                    data1.password = newpass
                    data1.save()
                    return render(request,'passchangedview.html')
                else:
                     return HttpResponse("password error")
            except Exception:
              return HttpResponse("username error")
        else:
            return redirect(changepassword)


def alreadyissued(request):
    return render(request,"alreadyissued.html")


def getbook(request):
 if 'id' in request.session:
     userid = request.session['id']
     user = Signup.objects.get(id=userid)
     if request.method == 'POST':
         bookid = request.POST["bookid"]
         # print(bookid)
         currentbook = Book.objects.get(id=bookid)
         if Issue.objects.filter(bookname=currentbook).exists():
             return redirect(alreadyissued)
         else:
             data = Issue.objects.create(username=user, bookname=currentbook)
             data.save()
             return render(request,"bookissuesuccess.html")
     else:
         return HttpResponse("error")




def userrenthistoryview(request):
    data1=Issue.objects.all()
    return render(request,'userrenthistory.html',{'data1':data1})



def userrenthistory(request):
    if 'id' in request.session:
        username = request.session['id']
        if request.method=='GET':
            data=Signup.objects.get(id=username)
            data1=Issue.objects.get(username=username).all()
            return render(request, "userrenthistory.html",{'data':data,'data1':data1})


def returnbook(request,id):
    data1 = Issue.objects.get(id=id)
    data1.delete()
    return redirect(userrenthistoryview)









  # data.name = newname
  # data.phone = newphone
  # data.email = newemail
  # data.save()
  # return redirect(editprofilesuccess)

#     else:
#         return render(request,'editprofileview.html',{'data':data})
# else:
#     return HttpResponse("error")








