import json
import mimetypes
import os

import falcon

from images_api.repositories import ElementNotFoundError


class ImagesCollectionResource:

    def __init__(self, repository, serializers):
        self.repository = repository
        self.serializers = serializers

    def on_post(self, request, response):
        image_ext = mimetypes.guess_extension(request.content_type)
        image_stream = request.stream
        image = self.repository.create(image_stream, image_ext)
        response.location = image.path
        response.status = falcon.HTTP_201
        response.body = self.serializers.ImageSerializer(image=image)


class ImageElementResource:

    def __init__(self, repository, serializers):
        self.repository = repository
        self.serializers = serializers

    def on_get(self, request, response, image_id):

        try:
            image, file_ = self.repository.get(image_id)
        except ElementNotFoundError as e:
            response.status = falcon.HTTP_404
            response.body = self.serializers.ErrorSerializer(e)
            return

        response.content_type = mimetypes.guess_type(image.path)[0]
        response.stream = file_
        response.stream_len = os.path.getsize(image.path)

    def on_delete(self, request, response, image_id):

        try:
            self.repository.delete(image_id)
        except ElementNotFoundError as e:
            response.status = falcon.HTTP_404
            response.body = self.serializers.ErrorSerializer(e)
            return

        response.status = falcon.HTTP_204
