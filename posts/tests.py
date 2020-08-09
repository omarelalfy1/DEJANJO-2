from django.test import TestCase
from .models import post
# Create your tests here.
class postmodeltest(testcase):
    def setup(self):
        post.object.create(text="just a test")
    
    def test_text_context(self):
        post=post.object.get(id=1)
        expected_test = post.text    
        self.assertEqual(expected_text,"just a test")