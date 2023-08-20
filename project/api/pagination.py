from rest_framework.pagination import PageNumberPagination


class ProductAPIListPagination(PageNumberPagination):
    page_size = 5 # Сколько по умолчанию записей на одной странице
    page_size_query_param = 'page_size' # Какой параметр должен ввести пользователь, чтобы изменять количество записей
    max_page_size = 10000 # Максимальное количество записей на выходе