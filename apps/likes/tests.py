from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from apps.users.models import User, UserPost
from .models import Like
from . import services


class LikesServiceTestCase(TestCase):
    def setUp(self):
        self.dummy_user = User.objects.create(
            first_name='John',
            last_name='Doe',
            username='dummyuser',
            email='dummy@ma.il',
            password='dummypass'
        )
        self.dummy_object = UserPost.objects.create(
            user=self.dummy_user,
            content='text text text',
            likes_count=10
        )

    def test_like_increments_post_likes_counter(self):
        initial_likes_count = self.dummy_object.likes_count
        services.like(self.dummy_user, self.dummy_object)
        self.assertEqual(self.dummy_object.likes_count, initial_likes_count+1)

    def test_like_unlike_counter_sanity(self):
        initial_likes_count = self.dummy_object.likes_count
        services.like(self.dummy_user, self.dummy_object)
        services.unlike(self.dummy_user, self.dummy_object)
        self.assertEqual(self.dummy_object.likes_count, initial_likes_count)

    def test_like_creates_relationship(self):
        services.like(self.dummy_user, self.dummy_object)
        obj_content_type = ContentType.objects.get_for_model(self.dummy_object)
        like = Like.objects.filter(
            user=self.dummy_user,
            content_type=obj_content_type.id,
            object_id=self.dummy_object.id
        )
        self.assertTrue(like)

    def test_unlike_destroys_relationship(self):
        services.like(self.dummy_user, self.dummy_object)
        services.unlike(self.dummy_user, self.dummy_object)
        obj_content_type = ContentType.objects.get_for_model(self.dummy_object)
        like = Like.objects.filter(
            user=self.dummy_user,
            content_type=obj_content_type.id,
            object_id=self.dummy_object.id
        )
        self.assertFalse(like)