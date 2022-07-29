from django.urls import include, path

app_name = "GAIA_RAPORTARI"

from . import views as RAPORTARI_VIEWS

urlpatterns = [
	path('main/<str:nume_zona>/',RAPORTARI_VIEWS.main,name='raportari_main'),
	path('main/<str:nume_zona>/filtru_rapoarte_data/assets',RAPORTARI_VIEWS.main_filtru_rapoarte_data_assets,name='raportari_main_filtru_rapoarte_assets'),
	path('main/<str:nume_zona>/filtru_rapoarte_data/subassets',RAPORTARI_VIEWS.main_filtru_rapoarte_data_subassets,name='raportari_main_filtru_rapoarte_subassets'),
	path('main/<str:nume_zona>/filtru_rapoarte_top10/assets',RAPORTARI_VIEWS.main_filtru_rapoarte_top10_assets,name='raportari_main_filtru_rapoarte_top10_assets'),
	path('main/<str:nume_zona>/filtru_rapoarte_top10/subassets',RAPORTARI_VIEWS.main_filtru_rapoarte_top10_subassets,name='raportari_main_filtru_rapoarte_top10_subassets'),
	path('main/<str:nume_zona>/filtru_rapoarte_top10_recurenta/assets',RAPORTARI_VIEWS.main_filtru_rapoarte_top10_recurenta_assets,name='raportari_main_filtru_rapoarte_top10_recurenta_assets'),
	path('main/<str:nume_zona>/filtru_rapoarte_top10_recurenta/subassets',RAPORTARI_VIEWS.main_filtru_rapoarte_top10_recurenta_subassets,name='raportari_main_filtru_rapoarte_top10_recurenta_subassets'),
	path('main/<str:nume_zona>/filtru_rapoarte_MTBF/assets',RAPORTARI_VIEWS.main_filtru_rapoarte_MTBF_assets,name='raportari_main_filtru_rapoarte_MTBF_assets'),
	path('main/<str:nume_zona>/filtru_rapoarte_MTBF/subassets',RAPORTARI_VIEWS.main_filtru_rapoarte_MTBF_subassets,name='raportari_main_filtru_rapoarte_MTBF_subassets'),
	path('main/<str:nume_zona>/filtru_rapoarte_MTTR/assets',RAPORTARI_VIEWS.main_filtru_rapoarte_MTTR_assets,name='raportari_main_filtru_rapoarte_MTTR_assets'),
	path('main/<str:nume_zona>/filtru_rapoarte_MTTR/subassets',RAPORTARI_VIEWS.main_filtru_rapoarte_MTTR_subassets,name='raportari_main_filtru_rapoarte_MTTR_subassets'),

]
