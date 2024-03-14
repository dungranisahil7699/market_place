from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Users, Product, Purchase
from .serializers import UserSerializer, ProductSerializer, PurchaseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from marketplace_project.settings import EMAIL_HOST_USER

class UserRegistrationView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        data = {
            "success": True,
            "message": "User registration successful!"
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = Users.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PurchaseCreateView(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

        # # Send email notification
        # subject = 'Purchase Confirmation'
        # message = 'Thank you for your purchase!'
        # from_email = EMAIL_HOST_USER
        # to_email = [self.request.user.email]
        # send_mail(subject, message, from_email, to_email)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'price']
    ordering_fields = ['name', 'price']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
