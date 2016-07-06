from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SigninForm, CompanyCredentialsForm, RaiseInvoiceForm
from django.views.generic import View
from django.views import generic
from django.core.urlresolvers import reverse
from .models import Company_credentials, Raise_invoice
from django.core.mail import send_mail, EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
import datetime
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'invoiceapp/index.html', {'message': 'You have successfully logged in'})
            return render(request, 'invoiceapp/index.html',
                          {'message': 'Your Account is not Active, Contact the Administrator'})
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
    return render(request, 'invoiceapp/login.html', {'message': 'log in first'})


class Account(View):
    form_class = CompanyCredentialsForm
    template_name = 'invoiceapp/account.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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




def generate_certificate(description_of_items,total_money ):

    buffer = BytesIO()
    styleSheet = getSampleStyleSheet()
    style = styleSheet['Normal']
    canv = Canvas('my_pdf.pdf')
    canv.setFont('Helvetica-Bold', 44, leading=None)
    canv.drawCentredString(308, 800, "INVOICE")
    canv.line(0, 785, 800, 785)
    canv.setFont('Helvetica', 21, leading=None)
    canv.drawCentredString(68, 760, "Description:")
    P = Paragraph(description_of_items, style)
    canv.setFont('Helvetica', 6, leading=None)
    aW = 500  # available width and height
    aH = 720
    w, h = P.wrap(aW, aH)  # find required space
    print(w)
    print(h)
    if w <= aW and h <= aH:
        P.drawOn(canv, 12, aH)
    # aH = aH - h # reduce the available height
    print(aH)
    canv.line(0, aH - 10, 800, aH - 10)
    canv.setFont('Helvetica', 18, leading=None)
    canv.drawCentredString(80, aH - 35, "Amount Payable:")
    canv.setFont('Helvetica', 12, leading=None)
    canv.drawCentredString(45, aH - 55, str(total_money) + ' ' + 'Dollars')
    canv.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


class RaiseInvoice(View):
    form_class = RaiseInvoiceForm
    template_name = 'invoiceapp/raise_invoice.html'

    def get(self, request):
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
            receivers = [reciever]
            pdf = generate_certificate(description_of_items,total_money)
            msg = EmailMessage(subject, message, sender, receivers)
            msg.attach_file('my_pdf.pdf', pdf)
            msg.send(fail_silently=True)
            raiseinvoice = form.save(commit=False)
            raiseinvoice.user = request.user
            raiseinvoice.save()
            return redirect('invoiceapp:index')
        return render(request, self.template_name,{'form': self.form_class(None), 'message': "Please Fill the Form again",})




def Estimates(request):
    if not request.user.is_authenticated():
        return render(request,'invoiceapp/login.html',{'message':'Login First'})
    template_name = 'invoiceapp/estimates.html'
    all_invoices = Raise_invoice.objects.filter(user=request.user).order_by('-pk')
    total = 0
    for invoice in all_invoices:
        total = total + invoice.total_money
    return render(request,template_name,{'all_invoices':all_invoices,'amount':total})




def Changestatus(request,id):
    selected_invoice = Raise_invoice.objects.get(pk=id)
    amount = request.POST['amount']
    amount = int(amount)
    total_money = selected_invoice.total_money
    if amount >  total_money:
        pass
    else:
        selected_invoice.total_money = (total_money) - amount
    selected_invoice.save()
    return redirect('invoiceapp:estimates')








    """if selected_invoice.paid == True:
        selected_invoice.paid = False
    else:
        selected_invoice.paid = True
    selected_invoice.save()
    return redirect('invoiceapp:estimates')"""



















