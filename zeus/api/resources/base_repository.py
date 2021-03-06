from flask import Response

from zeus.models import Repository

from .base import Resource


class BaseRepositoryResource(Resource):
    def dispatch_request(self, owner_name: str, repo_name: str, *args, **kwargs) -> Response:
        repo = Repository.query.filter(
            Repository.owner_name == owner_name,
            Repository.name == repo_name,
        ).first()
        if not repo:
            return self.not_found()
        return Resource.dispatch_request(self, repo, *args, **kwargs)
