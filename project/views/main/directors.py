from flask_restx import Namespace, Resource

from project.dao import director
from project.container import directors_service
from project.setup.api.parsers import page_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.expect(page_parser)
    # Декоратор который получает данные и проверяет их формат
    @director_ns.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return directors_service.get_all(**page_parser.parse_args())


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    @director_ns.response(404, 'Not Found')
    @director_ns.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id.
        """
        return directors_service.get_item(director_id)
