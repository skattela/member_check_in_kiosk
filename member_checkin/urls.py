from django.urls import path

from . import views

app_name = 'member_checkin'
urlpatterns = [
    path('', views.MembersView.as_view(), name='members'),

    path('member', views.MembersView.as_view(), name='members'),
    path('member/create', views.MemberCreateView.as_view(), name='member_create'),
    path('member/<str:pk>/', views.MemberView.as_view(), name='member'),
    path('member/<str:pk>/update', views.MemberUpdateView.as_view(), name='member_update'),
    path('member/<str:pk>/delete', views.MemberDeleteView.as_view(), name='member_delete'),

    path('checkin', views.CheckInsView.as_view(), name='checkins'),
    path('checkin/create', views.CheckInCreateView.as_view(), name='checkin_create'),
    path('checkin/<int:pk>/', views.CheckInView.as_view(), name='checkin'),
    path('checkin/<int:pk>/delete/', views.CheckInDeleteView.as_view(), name='checkin_delete'),
]
