from django.contrib import admin
from django.urls import path, include
import teamapp.views
from teamapp.views  import BlogList, BlogDetail,BlogCreate,BlogDelete,BlogUpdate,signupview, loginview
from contact_form.views import ContactFormView, ThanksView

app_name = 'contact_form'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',teamapp.views.welcome_html_temprate, name='welcome'),
    path('about/',teamapp.views.about_us_html_temprate, name='about_us'),
    path('signup/',signupview,name='signup'),
    path('login_sample/',loginview,name='login_sample'),
    path('list/',BlogList.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
    path('create/',BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>',BlogDelete.as_view(),name='delete'),
    path('update/<int:pk>',BlogUpdate.as_view(),name='update'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
