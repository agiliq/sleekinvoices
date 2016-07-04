from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SigninForm,CompanyCredentialsForm
from django.views.generic import View
from django.core.urlresolvers import reverse



def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active():
                login(request,user)
                return render(request,'invoiceapp/index.html',{'message':'You have successfully logged in'})
            return render(request, 'invoiceapp/index.html', {'message': 'Your Account is not Active, Contact the Administrator'})
        return render(request, 'invoiceapp/login.html', {'message': 'Wrong Username or Password'})
    else:
        if request.user.is_authenticated():
            return render(request, 'invoiceapp/index.html', {'message': 'Already logged in'})
        else:
            return render(request, 'invoiceapp/login.html')


def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request, 'invoiceapp/index.html', {'message': 'You have successfully logged out',})
    return render(request, 'invoiceapp/login.html',{'message':'log in first'})
    


class Account(View):
    form_class = CompanyCredentialsForm
    template_name = 'invoiceapp/account.html'
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect(reverse('invoiceapp:index'))

        return render(request, self.template_name, {'message': 'Fill your credentials again'})

class Index(View):
    form_class = SigninForm
    template_name = "invoiceapp/index.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect(reverse('invoiceapp:account'))

            return render(request, self.template_name, {'message': 'Sign in again ', 'form': form,})
        return render(request, self.template_name, {'message': 'Sign in again ', 'form': form,})






