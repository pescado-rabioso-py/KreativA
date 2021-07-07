from django.db import models
from django.db.models.signals import pre_save
from kreativa.utils import unique_slug_generator

# Create your models here.
# Home
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=6)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
#About
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)

#Skills
class Category(models.Model):
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)


#Portfolio
class Portfolio(models.Model):
    titulo = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/')
    slug = models.URLField(max_length=200, null=True, blank=True)
    details = models.TextField()
    class Meta:
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"

    def __str__(self):
        return f'Portfolio{self.id}'

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Portfolio)

#Slider
class Slider(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='slider/')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
