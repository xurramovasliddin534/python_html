from django.urls import path
from .views import news_veiw

urlpatterns=[
    path('', news_veiw, name='news_page')
]
