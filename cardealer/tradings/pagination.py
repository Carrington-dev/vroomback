from rest_framework import pagination
from rest_framework.response import Response


class VroomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
    
# pagination.py

# from rest_framework.pagination import PageNumberPagination

class CustomBrandPagination(pagination.PageNumberPagination):
    page_size = 40  # Number of items per page
    page_size_query_param = 'page_size'  # Allow the client to set the page size
    max_page_size = 200  # Maximum number of items per page allowed
    page_query_param = 'p'  # Custom query parameter for the page number
