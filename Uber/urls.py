from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from account import views as acc_view
from service import views as ser_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileListAPIView)

serv_router = DefaultRouter()
serv_router.register('taxi', ser_view.TaxiViewSet)

# posts_router = DefaultRouter()
# posts_router.register('tweet', posts_view.TweetViewSet)
# posts_router.register('comments', posts_view.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    # path('api/auth/token/', obtain_auth_token),


    path('api/account/', include(acc_router.urls)),

    path('api/service/', include(serv_router.urls)),

    path('api/service/taxi/<int:taxi_id>/order/', ser_view.OrderListCreateAPIView.as_view()),
    path('api/service/taxi/<int:taxi_id>/order/<int:pk>/', ser_view.OrderRetrieveUpdateDestroy.as_view()),

]

