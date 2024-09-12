from django.http import HttpResponse

def http_response(message, status):
  return HttpResponse(message, status=status)