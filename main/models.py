from django.db import models
from django.utils.text import slugify


# -----------------------------------------------------
# HERO SECTION
# -----------------------------------------------------
class HeroSection(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    subtitle = models.CharField(max_length=300, verbose_name='Subtitle')
    cta_text = models.CharField(max_length=50, verbose_name='Button Text')
    cta_link = models.CharField(max_length=200, verbose_name='Button Link')
    background_image = models.ImageField(upload_to='hero/', verbose_name='Background Image', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Sections'

    def __str__(self):
        return self.title


# -----------------------------------------------------
# WHY TRUST US FEATURES
# -----------------------------------------------------
class TrustFeature(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    icon = models.ImageField(upload_to='features/', verbose_name='Icon', blank=True)
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Trust Feature'
        verbose_name_plural = 'Trust Features'
        ordering = ['order']

    def __str__(self):
        return self.title


# -----------------------------------------------------
# TESTIMONIALS
# -----------------------------------------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    position = models.CharField(max_length=100, verbose_name='Position', blank=True)
    company = models.CharField(max_length=100, verbose_name='Company', blank=True)
    content = models.TextField(verbose_name='Testimonial Text')
    photo = models.ImageField(upload_to='testimonials/', verbose_name='Photo', blank=True)
    rating = models.IntegerField(default=5, verbose_name='Rating', choices=[(i, i) for i in range(1, 6)])
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.company}"


# -----------------------------------------------------
# FAQ - QUESTIONS & ANSWERS
# -----------------------------------------------------
class QA(models.Model):
    question = models.CharField(max_length=300, verbose_name='Question')
    answer = models.TextField(verbose_name='Answer')
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'
        ordering = ['order']

    def __str__(self):
        return self.question


# -----------------------------------------------------
# PROCESS VIDEO SECTION
# -----------------------------------------------------
class ProcessVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Description', blank=True)
    video_url = models.URLField(verbose_name='Video URL (YouTube/Vimeo)')
    thumbnail = models.ImageField(upload_to='videos/', verbose_name='Thumbnail', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Process Video'
        verbose_name_plural = 'Process Videos'

    def __str__(self):
        return self.title


# -----------------------------------------------------
# ABOUT US SECTION
# -----------------------------------------------------
class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    mission = models.TextField(verbose_name='Mission')
    vision = models.TextField(verbose_name='Vision')
    content = models.TextField(verbose_name='Company Description')
    image = models.ImageField(upload_to='about/', verbose_name='Image', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


# -----------------------------------------------------
# COURSES
# -----------------------------------------------------
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course Name')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug', blank=True)
    description = models.TextField(verbose_name='Short Description')
    detailed_content = models.TextField(verbose_name='Detailed Content')
    image = models.ImageField(upload_to='courses/', verbose_name='Course Image')
    duration = models.CharField(max_length=50, verbose_name='Course Duration', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', null=True, blank=True)
    level = models.CharField(max_length=50, verbose_name='Difficulty Level', blank=True)
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# -----------------------------------------------------
# CONTACT PAGE: COMPANY INFO
# -----------------------------------------------------
class ContactInfo(models.Model):
    company_name = models.CharField(max_length=200, verbose_name='Company Name')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=50, verbose_name='Phone Number')
    email = models.EmailField(verbose_name='Email')
    wechat = models.CharField(max_length=100, verbose_name='WeChat', blank=True)
    privacy_policy = models.TextField(verbose_name='Privacy Policy')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return self.company_name


# -----------------------------------------------------
# CONTACT FORM MESSAGES
# -----------------------------------------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')
    is_read = models.BooleanField(default=False, verbose_name='Read')

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
