from rest_framework.viewsets import ModelViewSet
from myApp.models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
class AuthorAPIView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['first_name',]
    ordering_fields=('first_name','last_name')
    pagination_class=PageNumberPagination

class BookAPIView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
   