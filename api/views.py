from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .forms import Host
from .untils.http_response import http_response
from .untils.exe_commands import exe_command
from django.middleware.csrf import get_token

def index(request):
  return HttpResponse("Server is running!")

@ensure_csrf_cookie
def get_csrf_token(request):
  if request.method == 'GET':
    crsf_token = get_token(request)
    return JsonResponse({'csrf_token': crsf_token}, status=200)
  else:
    return JsonResponse({'error': 'method dont allowed'}, status=405)

@csrf_exempt
def host_command(request):
  if request.method == 'POST':
    form = Host(request.POST) 
    
    if form.is_valid():
      cleaned_data = form.cleaned_data
      command = cleaned_data.pop('command', None)
      commit = cleaned_data.pop('commit', None)
      enable = cleaned_data.pop('enable', None)

      output = exe_command(cleaned_data, command, commit, enable)
      if type(output) == dict: 
        return JsonResponse(output, status=200, safe=False)
      else: 
        return http_response(output, 400)
    
    error_message = "error in submitted form"
    for field, errors in form.errors.items():
      error_message += f"{field}: {', '.join(errors)}. "

    return http_response(error_message, 400)

  return http_response("method is wrong", 405)