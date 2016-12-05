import falcon

from images_api import (
    resources,
    repositories,
    serializers,
    db,
    models,
)

image_storage_path = "images_api/images"
image_resource_name = "images"

images_repository = repositories.ImagesRepository(
    db=db,
    model=models.Image,
    storage_path=image_storage_path,
    resource_name=image_resource_name,
)

images_collection_resource = resources.ImagesCollectionResource(
    repository=images_repository,
    serializers=serializers,
)
image_element_resource = resources.ImageElementResource(
    repository=images_repository,
    serializers=serializers,
)

application = falcon.API()
application.add_route('/v1/images', images_collection_resource)
application.add_route('/v1/images/{image_id}', image_element_resource)
