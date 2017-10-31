import os
import unittest

from django.test import TestCase
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse

from .models import User, UserPost
from .forms import UserPostForm

from django.conf import settings


class UserPostFormTestCase(TestCase):
    def setUp(self):
        self.dummy_user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='dummyuser',
            email='dummy@ma.il',
            password='dummypass'
        )

        # FIXME: UserPost doesn't accept such an image object, so thumbnail tests cannot be accomplished
        image_path = os.path.join(settings.BASE_DIR, 'static/img/placeholder-image.png')
        self.dummy_image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/png')

    def test_create_empty_post(self):
        form = UserPostForm({'user_id': self.dummy_user.id})
        self.assertEqual(False, form.is_valid())

    def test_create_post_with_title_only(self):
        form = UserPostForm({'user_id': self.dummy_user.id, 'title': 'Some title'})
        self.assertEqual(False, form.is_valid())

    def test_create_post_with_excerpt_but_no_content(self):
        form = UserPostForm({'user_id': self.dummy_user.id, 'excerpt': 'Some text'})
        self.assertEqual(False, form.is_valid())

    def test_create_post_with_content_only(self):
        form = UserPostForm({'user_id': self.dummy_user.id, 'content': 'Some text'})
        self.assertEqual(True, form.is_valid())

    @unittest.skip("Dummy image object need to be fixed")
    def test_create_post_with_thumbnail_only(self):
        form = UserPostForm({'user_id': self.dummy_user.id, 'thumbnail': self.dummy_image})
        # import pudb; pudb.set_trace()
        self.assertEqual(True, form.is_valid())


class PostCreateViewTest(TestCase):
    def setUp(self):
        self.dummy_user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='dummyuser',
            email='dummy@ma.il',
        )
        self.dummy_user.set_password('dummypass')
        self.dummy_user.save()

    def test_call_view_denies_anonymous(self):
        response = self.client.get(reverse('user_post_create'), follow=True)
        self.assertRedirects(response, "%s?next=%s" % (reverse('auth_login'), reverse('user_post_create')) )

    def test_call_view_accepts_logged_user(self):
        self.client.login(username='dummyuser', password='dummypass')
        response = self.client.get(reverse('user_post_create'))
        self.assertEqual(response.status_code, 200)


class UserDetailViewTestCase(TestCase):
    def setUp(self):
        self.dummy_user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='dummyuser',
            email='dummy@ma.il',
            password='dummypass'
        )

    def test_user_empty_posts_board(self):
        """
        If user have no posts, there should be a message that tells "no posts" or something.
        """
        response = self.client.get(reverse('user_detail', args=[self.dummy_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'section-placeholder')
        self.assertNotContains(response, 'entities-list')

    def test_user_not_empty_posts_board(self):
        UserPost.objects.create(content='sdfsdfsdfsdf', user=self.dummy_user)
        response = self.client.get(reverse('user_detail', args=[self.dummy_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'entities-list')
        self.assertNotContains(response, 'section-placeholder')