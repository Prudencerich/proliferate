from django.db import transaction

class AtomicTransactionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        with transaction.atomic():
            response = self.get_response(request)
        return response
