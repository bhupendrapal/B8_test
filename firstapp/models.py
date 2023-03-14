from django.db import models


#model define karna hai
# Create your models here.    (books ke sare records table ke format me rahega) add karne hai form me edit nd delete option (crud opertion)
class Book(models.Model):
    name = models.CharField(max_length=100)  # 
    qty = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=100)
    is_published =models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book' 


#01.  makemigrations then migrate
# 02.views define:
# def home(request):
#     return render(request,"home.html")

# 03..url define
# from firstapp import views
# setting database seeeting and database create to mysqlclient

# 04.firstapp=Templates--home.html


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('welcome/',views.home, name = "home)")
# ]

# 04.py manage.py runserver
# 0.5..home.html me form create 
# 06.ef home(request):
    # if request.method == "POST":
    #     pass
    # elif request.method == "GET":
    #    return render(request,"home.html")

# 07..home.html--url define data type and form create and 

# 0..dynammic data  <input type = "submit" value = "submit"><br>