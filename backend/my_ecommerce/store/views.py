from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # This ensures normal users can only READ, but Admins can ADD and EDIT
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]