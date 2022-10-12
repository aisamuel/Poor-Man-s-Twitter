from .serializer import TweetSerializer
from .models import Tweet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TweetAPIView(APIView):
    """
    List all tweets, or create a new tweet.
    """
    def get(self, request, format=None):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response({
            "responseCode": '100',
            'data': serializer.data,
            "message": "List of Tweets"
        },
        status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                        "responseCode": '100',
                        "message": "Tweet successfully created"
                    },
                    status=status.HTTP_200_OK)
        return Response({"message": "Validation Error", "responseCode": "103", "errors": serializer.errors},
                                 status=status.HTTP_400_BAD_REQUEST)
