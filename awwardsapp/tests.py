from django.test import TestCase
from .models import Profile,Post

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile = Profile(name="james",user_name="jay",prof_pic="image.jpeg",bio="just testing")
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    
class PostTestClass(TestCase):

    def setUp(self):
        self.new_post=Post(sitename="techs",url="https://w3resource.com",Description="test app stuff",image="image.jpeg",Technology="basic",country="kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))    
    

