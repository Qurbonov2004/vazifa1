from django.db import models

class Our_Service(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xizmatlar"

class Client(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Mijozlar Fikri"

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Biz Bilan Bog'laning"

class OurGuard(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=55)
    status = models.CharField(max_length=55)

    class Meta:
        verbose_name_plural = "Shaxslar"
