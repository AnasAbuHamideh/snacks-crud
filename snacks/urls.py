from django.urls import path
from .views import (
                    SnackListView,
                    SnackDetailView,
                    SnackCreateView,
                    SnackUpdateView,
                    SnackDeleteView
)


urlpatterns= [
   path('',SnackListView.as_view(), name= 'snacks-list'),
   path('create/', SnackCreateView.as_view(), name = "snacks-create"),
   path('<int:pk>', SnackDetailView.as_view(), name = "snacks-detail"),
   path('update/<int:pk>', SnackUpdateView.as_view(), name = "snacks-update"),
   path('delete/<int:pk>', SnackDeleteView.as_view(), name = "snacks-delete"),
]