from django.db import connection

class RlsMiddleware(object):

    print("--mideellw------------------")
    def __init__ (self, get_response):
        self.get_response = get_response
        
    def __call__ (self, request):
        user_id = request.user.id
        print("---------user_id-------",user_id)
        with connection.cursor() as cursor:
            cursor.execute(f'SET ROLE "{user_id}" ')

        response = self.get_response(request)
        print("------response-------",response)
        return response

        # current_site = get_current_site(request)
        # with connection.cursor() as cursor:
        #         cursor.execute('SET SESSION "django.site" = %s;' % 
        #         current_site.id)
        # response = self.get_response(request)
        # with connection.cursor() as cursor:
        #         cursor.execute('SET SESSION "django.site" = -1;')
        # return response