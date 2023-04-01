from flask_restx import Namespace, Resource
from flask import request
from project.dao import movie
from project.services import movies_service
from project.setup.api.parsers import page_parser, status_page_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    @movie_ns.expect(status_page_parser)
    # Декоратор который получает данные и проверяет их формат
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        status = request.args.get('status')
        return movie_ns.get_all(status=status, **page_parser.parse_args())


@movie_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    @movie_ns.response(404, 'Not Found')
    @movie_ns.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movies_service.get_item(movie_id)
