from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import *
from .forms import ContactForm



# ============================
# HOME PAGE
# ============================
def home(request):
    context = {
        'hero': HeroSection.objects.filter(is_active=True).first(),
        'features': TrustFeature.objects.filter(is_active=True),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'qas': QA.objects.filter(is_active=True),
        'video': ProcessVideo.objects.filter(is_active=True).first(),
    }
    return render(request, 'main/home.html', context)



# ============================
# ABOUT PAGE
# ============================
def about(request):
    context = {
        'about': AboutUs.objects.filter(is_active=True).first(),
    }
    return render(request, 'main/about.html', context)



# ============================
# COURSES LIST PAGE
# ============================
def courses(request):
    context = {
        'courses': Course.objects.filter(is_active=True),
    }
    return render(request, 'main/courses.html', context)



# ============================
# COURSE DETAIL PAGE
# ============================
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    context = {
        'course': course,
    }
    return render(request, 'main/course_detail.html', context)



# ============================
# CONTACT PAGE + EMAIL
# ============================
def contact(request):
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    testimonials = Testimonial.objects.all()   # ⭐ ADD THIS


    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            # Save in database
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )

            # Email sending
            try:
                subject = f"New Message from {form.cleaned_data['name']}"
                message = f"""
Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}
Phone: {form.cleaned_data['phone']}

Message:
{form.cleaned_data['message']}
                """

                recipient_email = (
                    contact_info.email if contact_info else settings.DEFAULT_FROM_EMAIL
                )

                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent successfully!")

            except:
                messages.warning(
                    request,
                    "Message saved but email sending failed. We will check it manually."
                )

            return redirect('contact')

    else:
        form = ContactForm()

    context = {
        'form': form,
        'contact_info': contact_info,
        'testimonials': testimonials,
    }

    return render(request, 'main/contact.html', context)
