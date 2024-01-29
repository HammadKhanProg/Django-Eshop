from django.shortcuts import render,redirect

def auth_midddleware (get_response):

    def middleware (request):
        return_url=request.META["PATH_INFO"]
        print(return_url)
        if not request.session.get('customer_id'):
            return redirect (f'/login?return_url={return_url}')
        else:
            response=get_response(request)
            return response
    return middleware