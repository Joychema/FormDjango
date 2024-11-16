from django.shortcuts import render

# from .models import Form
# Create your views here.

# def detail(request):
#     form=Form.objects.all()
#     return render(request,'form.html',{'form':form})

from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # acces form data

                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

        # Here, you can save the data to the database or send an email, etc.
                messages.success(request,'Thank you for contacting us!')
                form = ContactForm()  #reset form after submission

        else:
            form = ContactForm()

        return render(request,'contact.html',{'form':form})

