import json


class _ImageSerializer:

    def __call__(self, image):
        return json.dumps({
            "id": str(image.id),
            "actions": {
                "get": image.uri,
                "delete": image.uri,
            }
        })


class _ErrorSerializer:

    def __call__(self, e):
        return json.dumps(e.__dict__)


ImageSerializer = _ImageSerializer()
ErrorSerializer = _ErrorSerializer()
