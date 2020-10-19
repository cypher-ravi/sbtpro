from rest_framework.pagination import PageNumberPagination

class PaginationForVendorAndCategory(PageNumberPagination):
    page_size = 10
    max_page_size = 20
    page_size_query_param = 'page_size'
     