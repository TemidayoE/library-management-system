from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.pagination import PageNumberPagination
from lib_app.models import Book
from lib_app.serializer import BookSerializer
from lib_app.maxins import RateLimitHeadersMixin
from rest_framework.throttling import UserRateThrottle

def error_response(status,code,message,details = None):
  return{
    "status": status,
    "code": code,
    "message": message,
    "errors": {"details": details},
}

class BookThrottle(UserRateThrottle):
  rate = "100/min"
  
class BookListCreateView(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  throttle_classes = [BookThrottle]
  pagination_class = PageNumberPagination
  
class BookRetrievalUpdateDeleteView(RateLimitHeadersMixin, APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
          return Response(
            error_response(
              status= "error",
              code=404,
              message= f'Book with id: {pk}, not found',
              details= "No books was found with the provided ID, try another"
            )
          )
          
        serializer = BookSerializer(book)
        
        throttle = UserRateThrottle()
        throttle.allow_request(request,self)
        
        rate_limit_headers = {
          'X-RateLimit-Limit': throttle.rate,
          'X-RateLimit-Remaining': max(0, throttle.num_requests - len(throttle.history)),
          'X-RateLimit-Reset': throttle.wait()
          }
        
        
        response_data = {
            "book": serializer.data,
            "status": "success",
            "message": "Book details retrieved successfully.",
            "header": rate_limit_headers
        }
        return Response(response_data)
  
    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
          return Response(
            error_response(
              status= "error",
              code=404,
              message= f'Book with id: {pk}, not found',
              details= "No books was found with the provided ID, try another"
            ), status=status.HTTP_404_NOT_FOUND
          )
          
        serializer = BookSerializer(book, data=request.data, partial=True)
        
        if serializer.is_valid():
          serializer.save()
          return Response({
            "status": "Success",
            "message": "Book updated successfully",
            "book": serializer.data
          }, status=status.HTTP_200_OK
                          )

        return Response(
            {
              "status": "error",
              "code": 404,
              "message": "Invalid data",
              "errors": serializer.errors,
            }, status= status.HTTP_400_BAD_REQUEST
          )
  
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
          return Response(
            error_response(
              status= "error",
              code=404,
              message= f'Book with id: {pk}, not found',
              details= "No books was found with the provided ID, try another"
            ), status=status.HTTP_404_NOT_FOUND
          )
        
        book.delete()
        return Response({
            "status": "Success",
            "message": "Book deleted successfully",
          }, status=status.HTTP_204_NO_CONTENT
        )
