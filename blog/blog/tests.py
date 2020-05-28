from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):    
    def setUp(self):
        user = User(1)
        user.save()
        # model = Post()
        # model.title = "Home"     
        # model.author = user   
        # model.body = "This is welcome page"
        # model.save()        
        Post.objects.create(title="Home", author=user, body="This is welcome page")
        Post.objects.create(title="About", author=user, body="About Us")
        Post.objects.create(title="Contact", author=user, body="Contact Us @")
        Post.objects.create(title="Customers", author=user, body="Our Customers are:")

    def test_post_object(self):
        home = Post.objects.get(title="Home")
        self.assertEqual(home.title, "Home")
        self.assertEqual(home.body, "This is welcome page")
        about = Post.objects.get(title="About")
        self.assertEqual(about.title, "About")
        self.assertEqual(about.body, "About Us")
        contact = Post.objects.get(title="Contact")
        self.assertEqual(contact.title, "Contact")
        self.assertEqual(contact.body, "Contact Us @")
        customer = Post.objects.get(title="Customers")
        self.assertEqual(customer.title, "Customers")
        self.assertEqual(customer.body, "Our Customers are:")

    def test_post_detail_view(self):
        home = Post.objects.get(pk=1)
        self.assertEqual(home.title, "Home")
        self.assertEqual(home.body, "This is welcome page")
        about = Post.objects.get(pk=2)
        self.assertEqual(about.title, "About")
        self.assertEqual(about.body, "About Us")
        contact = Post.objects.get(pk=3)
        self.assertEqual(contact.title, "Contact")
        self.assertEqual(contact.body, "Contact Us @")
        customer = Post.objects.get(pk=4)
        self.assertEqual(customer.title, "Customers")
        self.assertEqual(customer.body, "Our Customers are:")

    def test_string_representaion(self):
        home = Post.objects.get(title="Home")
        self.assertEqual(home.__str__(), "Home - This is welcome page")    
        about = Post.objects.get(title="About")   
        self.assertEqual(about.__str__(), "About - About Us")
        contact = Post.objects.get(title="Contact")
        self.assertEqual(contact.__str__(), "Contact - Contact Us @")
        customer = Post.objects.get(title="Customers")
        self.assertEqual(customer.__str__(), "Customers - Our Customers are:")

class HomePageViewTest(TestCase):
    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html') 

    