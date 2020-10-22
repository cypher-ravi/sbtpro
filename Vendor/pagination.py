from rest_framework.pagination import PageNumberPagination

class PaginationForVendor(PageNumberPagination):
    page_size = 2
    max_page_size = 20
    page_size_query_param = 'page_size'
