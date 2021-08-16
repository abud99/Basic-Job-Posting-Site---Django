from django.urls import path
from . import views
from .views import JobListView, JobDetailView, JobCreateView, JobDeleteView, JobListViewFiltered, ReviewDeleteView, ReviewSearchBar, WriteReview, ReviewDetailView, JobUpdateView, ReviewListView, ReviewUpdate, ChartTransaction
from django.contrib import admin
from django.urls import path, include
from freelancerwebsite import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', JobListView.as_view(), name = "Main-Page"),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('job/new/', JobCreateView.as_view(), name='jobpost'),
    path('job/review/', WriteReview.as_view(), name='review'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='jobdelete'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('job/review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('review/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('buyjob/<int:pk>', user_views.BuyJob, name='buy-job'),
    path('review/home/', ReviewListView.as_view(), name='home-review'),
    path('review/search/', ReviewSearchBar, name='review-search'),
    path('job/search/', JobListViewFiltered, name='job-search'),
    path('job/statistics/', ChartTransaction, name='statistics'),
]


