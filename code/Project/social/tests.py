from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Post
from django.urls import reverse


class SocialAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            user=self.user,
            body='Test post body'
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.follows.count(), 1)
        self.assertEqual(
            self.profile.follows.first().id,
            self.profile.id
        )

    def test_post_creation(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.body, 'Test post body')

    def test_index_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('social'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'social.html')

    def test_all_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('all_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_profile.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile', args=[self.profile.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_follow_unfollow(self):
        self.client.login(username='testuser', password='testpassword')

        # Follow profile
        response = self.client.post(
            reverse('profile', args=[self.profile.pk]),
            {'follow': 'follow'}
        )
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(
            self.profile.followed_by.count(),
            1
        )

        # Unfollow profile
        response = self.client.post(
            reverse('profile', args=[self.profile.pk]),
            {'follow': 'unfollow'}
        )
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(
            self.profile.followed_by.count(),
            0
        )
