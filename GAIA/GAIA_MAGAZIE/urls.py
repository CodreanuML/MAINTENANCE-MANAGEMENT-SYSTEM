from django.urls import include, path

from . import views as MAGAZIE_VIEWS

app_name = "GAIA_MAGAZIE"



urlpatterns = [path('main_locatii/',MAGAZIE_VIEWS.main_locatii,name='magazie_main_locatii'),
			   path('add_location/',MAGAZIE_VIEWS.add_location,name='magazie_add_location'),
			   path('main_items/',MAGAZIE_VIEWS.main_items,name='magazie_main_items'),
			   path('add_item/',MAGAZIE_VIEWS.add_item,name='magazie_add_item'),
			   path('vezi_continut_locatie/<int:pk>/',MAGAZIE_VIEWS.vezi_continut_locatie,name='continut_locatie'),
			   path('item_modify_plus/<int:pk>/',MAGAZIE_VIEWS.item_modify_plus,name='item_modify_plus'),
			   path('item_modify_minus/<int:pk>/',MAGAZIE_VIEWS.item_modify_minus,name='item_modify_minus'),
			   path('detalii_obiect/<int:pk>/',MAGAZIE_VIEWS.vezi_detalii_obiect,name='detalii_obiect'),
			   

]
