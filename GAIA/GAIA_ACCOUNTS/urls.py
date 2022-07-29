from django.urls import include,path

app_name="GAIA_ACCOUNTS"

from . import views as GAIA_ACCOUNTS_VIEWS




urlpatterns = [
	path('user_details/',GAIA_ACCOUNTS_VIEWS.main,name='accounts_main'),
	path('new_user_me/',GAIA_ACCOUNTS_VIEWS.creare_utilizator_me,name='creare_utilizator_me'),
	path('new_user_mnt/',GAIA_ACCOUNTS_VIEWS.creare_utilizator_mnt,name='creare_utilizator_mnt'),
]