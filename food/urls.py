from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import(
    FoodItemListAPIView,
    FoodItemDetailAPIView,
    CategoryListAPIView, 
    RestaurantListAPIView,
    CartListAPIView, 
    CartItemListAPIView,
    OrderListAPIView,
    OrderItemListAPIView,
    UserRegistrationAPIView,
    OrderDetailAPIView,
)


urlpatterns = [
    path('food-items/',
    FoodItemListAPIView.as_view()),
    path('food-items/<int:pk>/',
    FoodItemDetailAPIView.as_view()),
    path('categories/',
CategoryListAPIView.as_view()), 
    path('restaurants/',
RestaurantListAPIView.as_view()),  
    path('carts/',
CartListAPIView.as_view()),
    path('cart-items/',
CartItemListAPIView.as_view()),
    path('orders/',
OrderListAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('order-items/',
OrderItemListAPIView.as_view()),         

    path('token/',
    TokenObtainPairView.as_view(),
    name='token_Obtain_pair'),
    path('token/refresh/',
    TokenRefreshView.as_view(),
    name='token_refresh'),
    
    path('register/',
    UserRegistrationAPIView.as_view(), name='register'),
   
]    