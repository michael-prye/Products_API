from pickle import TRUE
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review

@api_view(['GET'])
def all_reviews(request):
    query_set =Review.objects.all()
    serializer = ReviewSerializer(query_set, many=TRUE)


    return Response(serializer.data)
