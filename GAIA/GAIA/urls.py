"""GAIA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from GAIA_ASSETS import views as VIEWS
from GAIA_ACCOUNTS import views as ACCOUNTS_VIEWS
from GAIA_ME_CORECTIVA import views as ME_CORECTIVA_VIEWS
from django.contrib.auth import views as auth_views

urlpatterns = [

    #choose your PATH

    path('home/', ACCOUNTS_VIEWS.home, name='home'), # logarea ca si administrator   
    
    #admin URL
    path('admin/', admin.site.urls, name='admin'), # logarea ca si administrator 

    #user URL
    # path('register/', ACCOUNTS_VIEWS.signup, name='user_registration'),   # crearea de utilizatori noi 
    path('login/',auth_views.LoginView.as_view(template_name='GAIA_ACCOUNTS/ACCOUNTS_LOGIN.html'), name='user_login'),   # crearea de utilizatori noi 
    path('logout/',auth_views.LogoutView.as_view(), name='user_logout'),


    #Maintenance  URL - Home

    path('maintenancehome/', VIEWS.home_maintenance, name='mhome'), # logarea ca si administrator   


    path('mnt_corectiva_mentenanta/vezi_raport_asset/<int:pk>' , ME_CORECTIVA_VIEWS.mnt_corectiva_mentenanta_vezi_rapoart_asset, name='mnt_corectiva_mentenanta_vezi_rapoart_asset') ,
    path('mnt_corectiva_mentenanta/vezi_raport_subasset/<int:pk>' , ME_CORECTIVA_VIEWS.mnt_corectiva_vezi_mentenanta_rapoart_subasset, name='mnt_corectiva_vezi_mentenanta_rapoart_subasset') ,
  
    
    #Maintenance Assets URL -airbag
    
    path('assets_airbag/', VIEWS.airbag_main,name='assets_airbag_main'),    # main airbag assets
    path('assets_airbag/new', VIEWS.NewAssetAirbagView,name='assets_airbag_newasset'),  # add new asset
    path('assets_airbag/<int:pk>', VIEWS.SubAssetAirbagView,name='subassets_airbag'),    # main airbag subasset
    path('assets_airbag/<int:pk>/newsubasset', VIEWS.NewSubAssetAirbagView,name='assets_airbag_newsubasset'),  # add new asset
    path('assets_airbag/<int:pk>/lista_avarii', VIEWS.airbag_lista_avarii,name='assets_airbag_lista_avarii'),    # lista avarii asset airbag
    path('assets_airbag/<int:pk>/lista_avarii/newavarie', VIEWS.NewAirbagAvarieView,name='assets_airbag_avarie_noua'),    # lista avarii asset airbag

    #Maintenance MNT CORECTIVA -aribag

    path('mnt_corectiva_mentenanta/airbag/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_airbag_rapoarte, name='mnt_corectiva_mentanta_airbag_rapoarte') , 
    path('mnt_corectiva_mentenanta/airbag/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_airbag_rapoarte_subassets, name='mnt_corectiva_mentenanta_airbag_rapoarte_subassets') , 


    #Maintenance Assets URL -asamblare
    path('assets_asamblare/', VIEWS.asamblare_main,name='assets_asamblare_main'),
    path('assets_assamblare/new', VIEWS.NewAssetAsamblareView,name='assets_asamblare_newasset'),  # add new asset
    path('assets_assamblare/<int:pk>', VIEWS.SubAssetAsamblareView,name='subassets_asamblare'),    # main airbag subasset
    path('assets_assamblare/<int:pk>/newsubasset', VIEWS.NewSubAssetAsamblareView,name='assets_asamblare_newsubasset'),  # add new asset
    path('assets_asamblare/<int:pk>/lista_avarii', VIEWS.asamblare_lista_avarii,name='assets_asamblare_lista_avarii'),    # lista avarii asset asamblare
    path('assets_asamblare/<int:pk>/lista_avarii/newavarie', VIEWS.NewAsamblareAvarieView,name='assets_asamblare_avarie_noua'),    # lista avarii asset asamblare

    #Maintenance MNT CORECTIVA -asamblare

    path('mnt_corectiva_mentenanta/asamblare/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_asamblare_rapoarte, name='mnt_corectiva_mentanta_asamblare_rapoarte') , 
    path('mnt_corectiva_mentenanta/asamblare/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_asamblare_rapoarte_subassets, name='mnt_corectiva_mentenanta_asamblare_rapoarte_subassets') , 


    #Maintenance DC URL -diecasting
    path('assets_diecasting/', VIEWS.diecasting_main,name='assets_diecasting_main'),
    path('assets_diecasting/new', VIEWS.NewAssetDiecastingView,name='assets_diecasting_newasset'),  # add new asset
    path('assets_diecasting/<int:pk>', VIEWS.SubAssetDiecastingView,name='subassets_diecasting'),    # main airbag subasset
    path('assets_diecasting/<int:pk>/newsubasset', VIEWS.NewSubAssetDiecastingView,name='assets_diecasting_newsubasset'),  # add new asset
    path('assets_diecasting/<int:pk>/lista_avarii', VIEWS.diecasting_lista_avarii,name='assets_diecasting_lista_avarii'),    # lista avarii asset diecasting
    path('assets_diecasting/<int:pk>/lista_avarii/newavarie', VIEWS.NewDiecastingAvarieView,name='assets_diecasting_avarie_noua'),    # lista avarii asset diecasting 

    #Maintenance MNT CORECTIVA -diecasting

    path('mnt_corectiva_mentenanta/diecasting/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_diecasting_rapoarte, name='mnt_corectiva_mentanta_diecasting_rapoarte') , 
    path('mnt_corectiva_mentenanta/diecasting/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_diecasting_rapoarte_subassets, name='mnt_corectiva_mentenanta_diecasting_rapoarte_subassets') ,    

    #Maintenance foaming URL -foaming
    path('assets_foaming/', VIEWS.foaming_main,name='assets_foaming_main'),
    path('assets_foaming/new', VIEWS.NewAssetFoamingView,name='assets_foaming_newasset'),  # add new asset
    path('assets_foaming/<int:pk>', VIEWS.SubAssetFoamingView,name='subassets_foaming'),    # main airbag subasset
    path('assets_foaming/<int:pk>/newsubasset', VIEWS.NewSubAssetFoamingView,name='assets_foaming_newsubasset'),  # add new asset
    path('assets_foaming/<int:pk>/lista_avarii', VIEWS.foaming_lista_avarii,name='assets_foaming_lista_avarii'),    # lista avarii asset foaming
    path('assets_foaming/<int:pk>/lista_avarii/newavarie', VIEWS.NewFoamingAvarieView,name='assets_foaming_avarie_noua'),    # lista avarii asset foaming  

    #Maintenance MNT CORECTIVA -foaming

    path('mnt_corectiva_mentenanta/foaming/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_foaming_rapoarte, name='mnt_corectiva_mentanta_foaming_rapoarte') , 
    path('mnt_corectiva_mentenanta/foaming/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_foaming_rapoarte_subassets, name='mnt_corectiva_mentenanta_foaming_rapoarte_subassets') ,   

    #Maintenance IMO URL -IMO
    path('assets_imo/', VIEWS.imo_main,name='assets_imo_main'),
    path('assets_imo/new', VIEWS.NewAssetImoView,name='assets_imo_newasset'),  # add new asset
    path('assets_imo/<int:pk>', VIEWS.SubAssetImoView,name='subassets_imo'),    # main airbag subasset
    path('assets_imo/<int:pk>/newsubasset', VIEWS.NewSubAssetImoView,name='assets_imo_newsubasset'),  # add new asset
    path('assets_imo/<int:pk>/lista_avarii', VIEWS.imo_lista_avarii,name='assets_imo_lista_avarii'),    # lista avarii asset imo
    path('assets_imo/<int:pk>/lista_avarii/newavarie', VIEWS.NewImoAvarieView,name='assets_imo_avarie_noua'),    # lista avarii asset imo    

    #Maintenance MNT CORECTIVA -IMO

    path('mnt_corectiva_mentenanta/imo/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_imo_rapoarte, name='mnt_corectiva_mentanta_imo_rapoarte') , 
    path('mnt_corectiva_mentenanta/imo/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_imo_rapoarte_subassets, name='mnt_corectiva_mentenanta_imo_rapoarte_subassets') ,  


    #Maintenance LW URL -asamblare
    path('assets_lw/', VIEWS.lw_main,name='assets_lw_main'),
    path('assets_lw/new', VIEWS.NewAssetLwView,name='assets_lw_newasset'),  # add new asset
    path('assets_lw/<int:pk>', VIEWS.SubAssetLwView,name='subassets_lw'),    # main airbag subasset
    path('assets_lw/<int:pk>/newsubasset', VIEWS.NewSubAssetLwView,name='assets_lw_newsubasset'),  # add new asset
    path('assets_lw/<int:pk>/lista_avarii', VIEWS.lw_lista_avarii,name='assets_lw_lista_avarii'),    # lista avarii asset lw
    path('assets_lw/<int:pk>/lista_avarii/newavarie', VIEWS.NewLwAvarieView,name='assets_lw_avarie_noua'),    # lista avarii asset lw   

   #Maintenance MNT CORECTIVA - LW

    path('mnt_corectiva_mentenanta/lw/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_lw_rapoarte, name='mnt_corectiva_mentanta_lw_rapoarte') , 
    path('mnt_corectiva_mentenanta/lw/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_lw_rapoarte_subassets, name='mnt_corectiva_mentenanta_lw_rapoarte_subassets') ,  


    #Maintenance TOOLSHOP URL -toolshop
    path('assets_toolshop/', VIEWS.toolshop_main,name='assets_toolshop_main'),
    path('assets_toolshop/new', VIEWS.NewAssetToolshopView,name='assets_toolshop_newasset'),  # add new asset
    path('assets_toolshop/<int:pk>', VIEWS.SubAssetToolshopView,name='subassets_toolshop'),    # main airbag subasset
    path('assets_toolshop/<int:pk>/newsubasset', VIEWS.NewSubAssetToolshopView,name='assets_toolshop_newsubasset'),  # add new asset
    path('assets_toolshop/<int:pk>/lista_avarii', VIEWS.toolshop_lista_avarii,name='assets_toolshop_lista_avarii'),    # lista avarii asset toolshop
    path('assets_toolshop/<int:pk>/lista_avarii/newavarie', VIEWS.NewToolshopAvarieView,name='assets_toolshop_avarie_noua'),    # lista avarii asset toolshop  

   #Maintenance MNT CORECTIVA -  toolshop

    path('mnt_corectiva_mentenanta/toolshop/rapoarte' , ME_CORECTIVA_VIEWS.mnt_corectiva_toolshop_rapoarte, name='mnt_corectiva_mentanta_toolshop_rapoarte') , 
    path('mnt_corectiva_mentenanta/toolshop/rapoarte_subassets' , ME_CORECTIVA_VIEWS.mnt_corectiva_toolshop_rapoarte_subassets, name='mnt_corectiva_mentenanta_toolshop_rapoarte_subassets') ,  






    #Maintenance -ME Corectiva - Raport  ASSET

    path('me_corectiva_productie/<int:pk>/raportnouasset0.0', ME_CORECTIVA_VIEWS.NewRaportAsset00VIEW,name='raportnouasset0.0'),    #  raport nou asset 0.0
    path('me_corectiva_productie/<int:pk>/raportnouasset0.0.1', ME_CORECTIVA_VIEWS.NewRaportAsset001VIEW,name='raportnouasset0.0.1'),    # cofirmare preluare
    path('me_corectiva_productie/<int:pk>/raportnouasset0.1', ME_CORECTIVA_VIEWS.NewRaportAsset01VIEW,name='raportnouasset0.1'),    #  raport nou asset 0.1
    path('me_corectiva_productie/<int:pk>/raportnouasset1.1', ME_CORECTIVA_VIEWS.NewRaportAsset11VIEW,name='raportnouasset1.1'),    #  raport nou asset 1.1



    path('me_corectiva_productie/<int:Asset_pk>/<int:pk>/raportnousubasset0.0', ME_CORECTIVA_VIEWS.NewRaportSubAsset00VIEW,name='raportnousubasset0.0'),    # raport nou subasset 0.0
    path('me_corectiva_productie/<int:pk>/raportnousubasset0.0.1', ME_CORECTIVA_VIEWS.NewRaportSubAsset001VIEW,name='raportnousubasset0.0.1'),    # araport nou subasset 0.0
    path('me_corectiva_productie/<int:pk>/raportnousubasset0.1', ME_CORECTIVA_VIEWS.NewRaportSubAsset01VIEW,name='raportnousubasset0.1'),    #  raport nou subasset 0.1
    path('me_corectiva_productie/<int:pk>/raportnousubasset1.1', ME_CORECTIVA_VIEWS.NewRaportSubAsset11VIEW,name='raportnousubasset1.1'), 


    path('me_corectiva_productie/vezi_raport_asset/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_vezi_rapoart_asset, name='me_corectiva_vezi_rapoart_asset') ,
    path('me_corectiva_productie/vezi_raport_subasset/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_vezi_rapoart_subasset, name='me_corectiva_vezi_rapoart_subasset') ,


    #Maintenance -ME Corectiva - Productie 

    path('productiehome/', ME_CORECTIVA_VIEWS.home_productie, name='phome'), # logarea ca si administrator 


    #Maintenance -ME Corectiva - ASAMBLARE
    path('me_corectiva_productie/asamblare' , ME_CORECTIVA_VIEWS.me_corectiva_asamblare, name='me_corectiva_asamblare') , 
    path('me_corectiva_productie/asamblare/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_asamblare_subasset, name='me_corectiva_asamblare_subasset') , 
    path('me_corectiva_productie/asamblare/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_asamblare_rapoarte, name='me_corectiva_asamblare_rapoarte') , 
    path('me_corectiva_productie/asamblare/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_asamblare_rapoarte_subassets, name='me_corectiva_asamblare_rapoarte_subassets') , 


    #Maintenance -ME Corectiva - AIRBAG
    path('me_corectiva_productie/airbag' , ME_CORECTIVA_VIEWS.me_corectiva_airbag, name='me_corectiva_airbag') , 
    path('me_corectiva_productie/airbag/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_airbag_subasset, name='me_corectiva_airbag_subasset') ,
    path('me_corectiva_productie/airbag/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_airbag_rapoarte, name='me_corectiva_airbag_rapoarte') , 
    path('me_corectiva_productie/airbag/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_airbag_rapoarte_subassets, name='me_corectiva_airbag_rapoarte_subassets') ,


    #Maintenance -ME Corectiva - DIECASTING
    path('me_corectiva_productie/diecasting' , ME_CORECTIVA_VIEWS.me_corectiva_diecasting, name='me_corectiva_diecasting') , 
    path('me_corectiva_productie/diecasting/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_diecasting_subasset, name='me_corectiva_diecasting_subasset') ,
    path('me_corectiva_productie/diecasting/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_diecasting_rapoarte, name='me_corectiva_diecasting_rapoarte') , 
    path('me_corectiva_productie/diecasting/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_diecasting_rapoarte_subassets, name='me_corectiva_diecasting_rapoarte_subassets') ,


    #Maintenance -ME Corectiva - FOAMING
    path('me_corectiva_productie/foaming' , ME_CORECTIVA_VIEWS.me_corectiva_foaming, name='me_corectiva_foaming') , 
    path('me_corectiva_productie/foaming/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_foaming_subasset, name='me_corectiva_foaming_subasset') ,
    path('me_corectiva_productie/foaming/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_foaming_rapoarte, name='me_corectiva_foaming_rapoarte') , 
    path('me_corectiva_productie/foaming/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_foaming_rapoarte_subassets, name='me_corectiva_foaming_rapoarte_subassets') ,



    #Maintenance -ME Corectiva - IMO
    path('me_corectiva_productie/imo' , ME_CORECTIVA_VIEWS.me_corectiva_imo, name='me_corectiva_imo') , 
    path('me_corectiva_productie/imo/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_imo_subasset, name='me_corectiva_imo_subasset') ,
    path('me_corectiva_productie/imo/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_imo_rapoarte, name='me_corectiva_imo_rapoarte') , 
    path('me_corectiva_productie/imo/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_imo_rapoarte_subassets, name='me_corectiva_imo_rapoarte_subassets') ,

    #Maintenance -ME Corectiva - LW
    path('me_corectiva_productie/lw' , ME_CORECTIVA_VIEWS.me_corectiva_lw, name='me_corectiva_lw') , 
    path('me_corectiva_productie/lw/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_lw_subasset, name='me_corectiva_lw_subasset') ,
    path('me_corectiva_productie/lw/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_lw_rapoarte, name='me_corectiva_lw_rapoarte') , 
    path('me_corectiva_productie/lw/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_lw_rapoarte_subassets, name='me_corectiva_lw_rapoarte_subassets') ,

    #Maintenance -ME Corectiva - toolshop
    path('me_corectiva_productie/toolshop' , ME_CORECTIVA_VIEWS.me_corectiva_toolshop, name='me_corectiva_toolshop') , 
    path('me_corectiva_productie/toolshop/<int:pk>' , ME_CORECTIVA_VIEWS.me_corectiva_toolshop_subasset, name='me_corectiva_toolshop_subasset') ,
    path('me_corectiva_productie/toolshop/rapoarte' , ME_CORECTIVA_VIEWS.me_corectiva_toolshop_rapoarte, name='me_corectiva_toolshop_rapoarte') ,
    path('me_corectiva_productie/toolshop/rapoarte_subassets' , ME_CORECTIVA_VIEWS.me_corectiva_toolshop_rapoarte_subassets, name='me_corectiva_toolshop_rapoarte_subassets') , 





    #RAPORTARI //////////////////////////////////////////////////////////////////////////////////////////////////////

    path('maintenance_raportari/', include("GAIA_RAPORTARI.urls")),


    #MAGAZIE ////////////////////////////////////////////////////////////////////////////////////////////////////////


    path('maintenance_magazie/', include("GAIA_MAGAZIE.urls")),


    #PLAN ACTIUNI ////////////////////////////////////////////////////////////////////////////////////////////////////


    path('maintenance_plan_actiuni/',include("GAIA_PLAN_ACTIUNI.urls")),


    #ACCOUNTS ////////////////////////////////////////////////////////////////////////////////////////////////////////
     path('account/',include("GAIA_ACCOUNTS.urls")),

     ]


