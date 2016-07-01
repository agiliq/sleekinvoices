from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import SigninForm,CompanyCredentialsForm,RaiseInvoiceForm
from django.views.generic import View
from django.core.urlresolvers import reverse
from .models import Company_credentials,Raise_invoice
from django.core.mail import send_mail,EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
import datetime
from io import BytesIO

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


def import_data():
    last_name = 'Setia'
    first_name = 'Gaurav'
    course_name = 'Agiliq'
    pdf_file_name = 'my_pdf' + '.pdf'
    pdf = generate_certificate(first_name, last_name, course_name, pdf_file_name)
    return pdf


def generate_certificate(first_name, last_name, course_name, pdf_file_name):
    attendee_name = first_name + ' ' + last_name
    buffer = BytesIO()
    c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))
    x = 570
    c.setFont('Helvetica-Bold', 13, leading=None)
    l = ['Agiliq info solutions', 'Opposite D-mart', 'Hyderabad']
    for i in l:
        c.drawCentredString(85, x, i)
        x = x - 16
    c.setFont('Helvetica-Bold', 44, leading=None)
    c.drawCentredString(398, 548, "INVOICE")
    now = datetime.datetime.now()
    c.setFont('Helvetica-Bold', 16, leading=None)
    c.drawCentredString(630, 554, str(now.year) + '/' + str(now.month) + '/' + str(now.day))
    c.line(10, 500, 1500, 500)
    c.setFont('Helvetica', 42, leading=None)
    c.drawCentredString(415, 450, "Certificate of Completion")
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 420, "This certificate is presented to:")
    c.setFont('Helvetica-Bold', 34, leading=None)
    c.drawCentredString(415, 365, attendee_name)
    c.setFont('Helvetica', 24, leading=None)
    c.drawCentredString(415, 320, "For completing the following course:")
    c.setFont('Helvetica', 20, leading=None)
    c.drawCentredString(415, 280, course_name)

    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf



class RaiseInvoice(View):
    form_class = RaiseInvoiceForm
    template_name = 'invoiceapp/raise_invoice.html'
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            subject = 'Invoice'
            message = form.cleaned_data['message']
            description_of_items = form.cleaned_data['description_of_items']
            raise_for = form.cleaned_data['raise_for']
            currency = form.cleaned_data['currency']
            total_money = form.cleaned_data['total_money']
            sender = request.user.email
            reciever = form.cleaned_data['email_to']
            receivers = ['gaurav_setia@yahoo.com']
            send_mail(subject, message, sender, receivers)
            pdf = import_data()
            msg = EmailMessage(subject,message,sender,receivers)
            msg.attach_file('my_pdf.pdf', pdf)
            msg.send(fail_silently=True)
            return redirect('invoiceapp:index')
        return render(request, self.template_name,{'form': self.form_class(None), 'message': "Please Fill the Form again",})