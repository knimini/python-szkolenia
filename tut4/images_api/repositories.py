import os
import uuid


class ElementNotFoundError(Exception):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ImagesRepository:

    def __init__(self, db, model, storage_path, resource_name):
        self._db = db
        self._model = model
        self._dir = storage_path
        self._resource = resource_name

    def create(self, stream, ext):
        id_ = str(uuid.uuid4())
        filename = '{id}{ext}'.format(id=id_, ext=ext)
        image_path = os.path.join(self._dir, filename)
        image_uri = os.path.join(self._resource, filename.split('.')[0])

        with open(image_path, 'wb') as image_file:
            while True:
                chunk = stream.read(4096)
                if not chunk:
                    break

                image_file.write(chunk)
        image = self._model(id_, image_path, image_uri)
        self._db.images[id_] = image
        return image

    def get(self, image_id):

        try:
            image = self._db.images[image_id]
        except KeyError:
            raise ElementNotFoundError(
                field="id",
                message="Element with id {} doesn't exist".format(image_id),
                type=ElementNotFoundError.__name__,
            )

        file_ = open(image.path, 'rb')
        return image, file_

    def delete(self, image_id):

        try:
            image = self._db.images[image_id]
        except KeyError:
            raise ElementNotFoundError(
                field="id",
                message="Element with id {} doesn't exist".format(image_id),
                type=ElementNotFoundError.__name__,
            )

        try:
            os.remove(image.path)
        except OSError:
            raise ElementNotFoundError(
                field="id",
                message="Element with id {} doesn't exist".format(image_id),
                type=ElementNotFoundError.__name__,
            )

        del self._db.images[image_id]
