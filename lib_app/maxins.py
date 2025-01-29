from rest_framework.response import Response
from rest_framework.views import APIView

class RateLimitHeadersMixin(APIView):
    def finalize_response(self, request, response, *args, **kwargs):
        # Retrieve throttling details
        throttle = getattr(self, "DEFAULT_THROTTLE_CLASSES", None)

        return super().finalize_response(request, response, *args, **kwargs)
