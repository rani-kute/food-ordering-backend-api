from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import FoodItem,Category,Restaurant,Cart,CartItem, Order, OrderItem
from.serializers import (
        FoodItemSerializer,
        CategorySerializer,
        RestaurantSerializer,
        CartSerializer,
        CartItemSerializer,
        OrderSerializer,
        OrderItemSerializer,
        UserSerializer,
)


class FoodItemListAPIView(APIView):
    def get( self,request):
      food_items = FoodItem.objects.all()
      serializer = FoodItemSerializer(food_items,many=True)
      return Response(serializer.data)

    def post(self, request):
        serializer= FoodItemSerializer(data=request.data)  
        print("POST DATA:",request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED) 
        print("SERIALIZEER ERRORS:",serializer.errors) 
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class FoodItemDetailAPIView(APIView):
        def get(self, request, pk):
                food_item = get_object_or_404(FoodItem, pk=pk)
                serializer= FoodItemSerializer(food_item)
                return Response(serializer.data)
        
        def put(self, request, pk):
                food_item = get_object_or_404(FoodItem, pk=pk)
                serializer= FoodItemSerializer(food_item,data=request.data)
                
                if serializer.is_valid():
                 serializer.save()
                return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def patch(self, request, pk):
                food_item= get_object_or_404(FoodItem, pk=pk)
                serializer= FoodItemSerializer(food_item,data=request.data,partial=True)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors, status=400)
        
        def delete(self,request,pk):
                food_item=get_object_or_404(FoodItem,pk=pk)
                food_item.delete()
                return Response(
                        {"message": "Food item deleted successfully"},
                        status=status.HTTP_200_OK)      

class CategoryListAPIView(APIView):
        def get(self,request):
            categories = Category.objects.all()
            serializer= CategorySerializer(categories,many=True)      
            return Response(serializer.data)          
    
class RestaurantListAPIView(APIView):
        def get(self, request):
                restaurants = Restaurant.objects.all()
                serializer = RestaurantSerializer(restaurants, many=True)
                return Response(serializer.data)
        
        

class CartListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data) 
           
class CartItemListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(cart__user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)

        food_item_id = request.data.get('food_item')
        quantity = request.data.get('quantity', 1)

        food_item = get_object_or_404(FoodItem, id=food_item_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            food_item=food_item,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
        
class OrderListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
class OrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        order = get_object_or_404(
            Order,
            pk=pk,
            user=request.user
        )

        new_status = request.data.get('status')

        allowed_statuses = [
            'pending',
            'confirmed',
            'preparing',
            'out_for_delivery',
            'delivered',
            'cancelled'
        ]

        if new_status not in allowed_statuses:
            return Response(
                {"error": "Invalid order status."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = new_status
        order.save(update_fields=['status'])

        return Response({
            "message": "Order status updated successfully!",
            "order_id": order.id,
            "status": order.status
        }, 
        status=status.HTTP_200_OK)       
        
class OrderItemListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_items = OrderItem.objects.filter(order__user=request.user)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            order = serializer.validated_data['order']

            if order.user != request.user:
                return Response(
                    {"error": "You can only add items to your own order."},
                    status=status.HTTP_403_FORBIDDEN
                )

            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "User registered successfully!",
                    "user": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )        