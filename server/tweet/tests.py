from xxlimited import foo
from django.test import TestCase, Client

from tweet.models import Tweet

# Create your tests here.
class TestTweetCase(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        
    def test_tweet_view(self):
        url = "/api/tweet/tweets/"
        
        tweet1 = {"name": "First Tweet", "content": "This is my first tweet i hope you guys love it"}
        
        resp1 = self.client.post(url, data=tweet1)
        queryset = Tweet.objects.first()
        
        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp1.json()["responseCode"], "100")
        self.assertEqual(queryset.name, tweet1["name"])
        self.assertEqual(queryset.content, tweet1["content"])
        
        #Post tweet with content length is greater than 50
        tweet2 = {"name": "First Tweet", "content": "This is my first tweet i hope you guys love it. \
                  Oops i can't post this tweet because the content length is greater than 50."}
        
        resp2 = self.client.post(url, data=tweet2)
        queryset_count = Tweet.objects.count()
        self.assertEqual(resp2.json()["responseCode"], "103")
        self.assertEqual(resp2.status_code, 400)
        self.assertEqual(queryset_count, 1)
        
        tweet3 = {"name": "Third Tweet", "content": "This is my third tweet i hope you guys love it"}
        tweet4 = {"name": "Forth Tweet", "content": "This is my forth tweet i hope you guys love it"}
        tweet5 = {"name": "Fifth Tweet", "content": "This is my fifth tweet i hope you guys love it"}
        
        self.client.post(url, data=tweet3)
        self.client.post(url, data=tweet4)
        self.client.post(url, data=tweet5)
        
        resp3 = self.client.get(url)
        self.assertEqual(resp3.status_code, 200)
        self.assertEqual(resp3.json()["responseCode"], "100")
        self.assertEqual(len(resp3.json()["data"]), 4)
        
        
        
        
        
        