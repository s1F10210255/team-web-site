from django.db import models
<<<<<<< Updated upstream
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at= models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank= True, null=True)
    like = models.IntegerField(default=0)

    def publish(self):
        self.published_at= timezone.now()
        self.save()

    def __str__(self):
        return self.title
=======
from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin
)

class Users(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=100)
  email = models.EmailField(max_length=100, unique=True)
  date_of_birth = models.DateField()
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  picture = models.FileField(null=True, upload_to='picture/')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  class Meta:
    db_table = 'user'
>>>>>>> Stashed changes

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
