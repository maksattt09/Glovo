from  rest_framework.pagination import PageNumberPagination


class ProductListAPIViewPagination(PageNumberPagination):
    page_size = 3

class OrderListAPIViewPagination(PageNumberPagination):
    page_size = 4