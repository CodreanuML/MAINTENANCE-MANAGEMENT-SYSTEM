from django.urls import include, path

app_name = "GAIA_PLAN_ACTIUNI"

from . import views as PLAN_ACTIUNI_VIEWS

urlpatterns = [
	path('asamblare_main/',PLAN_ACTIUNI_VIEWS.asamblare_actiuni_main,name='asamblare_actiuni_main'),
	path('airbag_main/',PLAN_ACTIUNI_VIEWS.airbag_actiuni_main,name='airbag_actiuni_main'),
	path('diecasting_main/',PLAN_ACTIUNI_VIEWS.diecasting_actiuni_main,name='diecasting_actiuni_main'),
	path('foaming_main/',PLAN_ACTIUNI_VIEWS.foaming_actiuni_main,name='foaming_actiuni_main'),
	path('lw_main/',PLAN_ACTIUNI_VIEWS.lw_actiuni_main,name='lw_actiuni_main'),
	path('imo_main/',PLAN_ACTIUNI_VIEWS.imo_actiuni_main,name='imo_actiuni_main'),
	path('toolshop_main/',PLAN_ACTIUNI_VIEWS.toolshop_actiuni_main,name='toolshop_actiuni_main'),
	



	path('adauga_actiune/',PLAN_ACTIUNI_VIEWS.add_actiune,name='adauga_actiune'),
	path('vizualizare_actiune/<int:pk>/',PLAN_ACTIUNI_VIEWS.vizualizare_actiune,name='vizualizare_actiune'),
	path('editare_actiune/<int:pk>/',PLAN_ACTIUNI_VIEWS.editeaza_actiune,name='editeaza_actiune'),
]
