import mimetypes

from urllib.request import urlopen
from urllib.error import HTTPError

from django.conf import settings
from social_core.backends.twitter import TwitterOAuth
from social_core.backends.facebook import FacebookOAuth2


def get_user_avatar(backend, details, response, *args, **kwargs):
    url = None
    if backend.__class__ == TwitterOAuth:
        url = response.get('profile_image_url', '').replace('_normal', '')

    elif backend.__class__ == FacebookOAuth2:
        url = "http://graph.facebook.com/%s/picture?type=large" \
              % response["id"]

    if url:
        try:
            resp = urlopen(url)

            content_type = resp.headers['content-type']
            extension = mimetypes.guess_extension(content_type)

            user = kwargs['user']

            image_name = "{username}_avatar.{extension}".format(username=user.username, extension=extension)

            filepath = settings.MEDIA_ROOT + image_name
            fout = open(filepath, "wb")
            fout.write(resp.read())
            fout.close()

            image_url = settings.MEDIA_URL + image_name
            user.profile_pic = image_url
            user.save()

        except HTTPError:
            pass