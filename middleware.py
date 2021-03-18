def uniauth_django_middleware(get_response):

    def Redirect(request):

        response = get_response(request)

        return response
	
	def Callback(request):
		
        response = get_response(request)

        return response

    return middleware