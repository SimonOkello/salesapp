from django.urls import path
from .views import(
    home_view,
    SaleListView,
    SaleDetailView,
)
app_name='sales'
urlpatterns = [
    path('', home_view, name='sales-index'),
    path('sales/', SaleListView.as_view(), name='sales'),
    path('sales/<pk>/', SaleDetailView.as_view(), name='detail'),
]