from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from parking import views
from django.conf.urls import include

urlpatterns = format_suffix_patterns([
    #url(r'^$', views.api_root),
    
    url(r'^parking/$',
        views.ParkingSpotList.as_view(),
        name='park-list'),
    
    url(r'^userprofile/$',
        views.UserProfileList.as_view(),
        name='userprofile-list'),
    
    url(r'^carinfo/$',
        views.CarInfoList.as_view(),
        name='carinfo-list'),
    
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/create/$',
        views.UserCreate.as_view(),
        name='user-list'),

    url(r'^parking/search/$',
        views.ParkingSpotSearch.as_view(),
        name='park-search'),
    
     
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
