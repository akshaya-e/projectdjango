from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home, name="home"),
    path('base/',v.base, name="base"),
    path('about/',v.about, name="about"),
    path('enquiry/',v.enquiry,name="enquiry"),
    path('student/',v.student,name="student"),
    path('test/',v.test,name="test"), 
    path('register/',v.register,name="register"),
    path('userlogin/',v.userlogin,name="userlogin"),
    path('userlogout',v.userlogout,name="userlogout"),
    path('books/',v.books,name="books"),
    path('bookdetails/',v.bookdetails,name="bookdetails"),
    path('item/<int:pk>/delete/',v.delt,name="delt"),
    path('item/<int:pk>/edit/',v.edit,name="edit"),
]
