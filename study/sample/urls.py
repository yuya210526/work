from django.urls import path
from sample import views

app_name = 'sample'
urlpatterns = [
    path('company/', views.CompanyList.as_view(), name='company_list'),
    path('balancingGroup/<int:company_id>/', views.BalancingGroupList.as_view(), name='balancing_group_list'),
    path('companyNavigation/', views.CompanyNavigation.as_view(), name='company_navigation'),
]
