import django
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
from django.utils import simplejson

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.resources import ModelResource
from tastypie.utils.mime import build_content_type

from emberplay.models import Message


class EmberModelResource(ModelResource):
    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        if type(data) is Bundle:
            data = {
                self.Meta.resource_name: data
            }
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


class UserResource(EmberModelResource):
    # messages = fields.ToManyField('emberplay.api.MessageResource', 'messages')

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

        always_return_data = True
        fields = ['id', 'username']
        allowed_methods = ['get']
        collection_name = "users"
        include_resource_uri = False

    def dehydrate(self, bundle):
        bundle.data['screen_name'] = "steveWINton"
        return bundle


class MessageResource(EmberModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'

        always_return_data = True
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
        collection_name = "messages"
        include_resource_uri = False

    def dehydrate(self, bundle):
        bundle.data['user_id'] = bundle.obj.user.id
        return bundle
