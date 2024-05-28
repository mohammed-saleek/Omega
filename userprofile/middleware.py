import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Login and Register Urls to be exempt from validation
        exempt_urls= [
            'token_obtain_pair',
            'register-user',
            'user-chat'
        ]
        try:
            # Resolve the current URL
            current_url = resolve(request.path_info).url_name

            # Skip the check for exempt URLs
            if current_url in exempt_urls:
                return None

            # Get the Authorization header
            auth_header = request.headers.get('Authorization')

            if not auth_header:
                return JsonResponse({'error': 'Authorization header missing'}, status=401)

            if not auth_header.startswith('JWT '):
                return JsonResponse({'error': 'Invalid token prefix'}, status=401)

            # Extract the token (assuming format "JWT <token>")
            token = auth_header.split(' ')[1]
            
            # Decode the token to validate it
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user_payload = payload  # Attach payload to request for later use
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token has been expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid token'}, status=401)
        
        except Exception as exception:
            print("error has been occured")
            print(str(exception))