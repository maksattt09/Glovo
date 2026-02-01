from django.urls import path, include
from rest_framework.routers import  SimpleRouter,DefaultRouter
from .views import ( UserProfileListAPIView, CategoryViewSet, StoreListAPIView,
                     StoreDetailAPIView, StoreMenuViewSet, ContactViewSet, AddressViewSet,
                     ProductListAPIView, ProductDetailAPIView, OrderListAPIView, OrderDetailAPIView,
                     CourierProductViewSet, ReviewViewSet, UserProfileDetailAPIView,
                     RegisterView, LogoutView, LoginView)

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('storeMenu', StoreMenuViewSet)
router.register('contact', ContactViewSet)
router.register('address', AddressViewSet)
router.register('courierProduct', CourierProductViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='userprofile-list'),
    path('users/<int:pk>/',UserProfileDetailAPIView.as_view(), name='userprofile-detail'),
    path('store/', StoreListAPIView.as_view(), name='store-list'),
    path('store/<int:pk>/',StoreDetailAPIView.as_view(), name='store-detail'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('order/', OrderListAPIView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail'),
    path('register/',RegisterView.as_view(), name='register-list'),
    path('login/', LoginView.as_view(), name='login-list'),
    path('logout/', LogoutView.as_view(), name='logout-list'),

]