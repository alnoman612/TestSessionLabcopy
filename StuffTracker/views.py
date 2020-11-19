from django.shortcuts import render, redirect
from django.views import View
from .models import Stuff, MyUser
# Create your views here.

class Home(View):
    def get(self,request):
        request.session["current"] = ""
        return render(request,"home.html",{})

    def post(self,request):
        try:
            myuser = MyUser.objects.get(name=request.POST['name'], password=request.POST['password'])
            request.session["current"] = myuser.id
            return redirect("/things/")
        except Exception as e:
            return render(request,"home.html",{})


class Things(View):
    def get(self,request):

        user = request.session.get("current", False)
        # things = str(Stuff.objects.filter(user=user))
         #things = map(str,list(Stuff.objects.all()))
        things = map(str, list(Stuff.objects.filter(user=user)))

        return render(request, "things.html", {"things":things})
    def post(self,request):
        s = request.POST.get('stuff','')

        user = request.session.get("current",False )
        # region = list(Region.objects.all().values())
        # regions.append(newRegion)


        if s != '':
            newThing = Stuff(name=s, user=MyUser.objects.get(id=user))
            newThing.save()
        things = map(str, list(Stuff.objects.filter(user=user)))
        return render(request, "things.html", {"things":things})
