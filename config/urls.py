from django.contrib import admin
from django.urls import path
import teamapp.views


from teamapp.views  import BlogList, BlogDetail,BlogCreate,BlogDelete,BlogUpdate,signupview, loginview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',teamapp.views.welcome_html_temprate, name='welcome'),
    path('about/',teamapp.views.about_us_html_temprate, name='about_us'),
    path('contact/',teamapp.views.contact_us_html_temprate, name='contact_us'),
    path('signup/',signupview,name='signup'),
    path('login/',loginview,name='login'),
    path('list/',BlogList.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
    path('create/',BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>',BlogDelete.as_view(),name='delete'),
    path('update/<int:pk>',BlogUpdate.as_view(),name='update'),
]
