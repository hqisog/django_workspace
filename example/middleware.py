from django.http import HttpResponse
class CheckSoureMiddware(object):
    def process_request(self, request):
        from_source = request.META['HTTP_USER_AGENT']
        print('from_source ',from_source)
        if 'iPhone' in from_source:
            request.session['from_source'] = 'iphone'
        else:
            request.session['from_source'] = 'pc'

    def process_response(self, request, response):
        res = 'hehe'
        print(res)
        return HttpResponse(res)

class ForbidSomeIpMiddleware(object):
    def process_request(self, request):
        allow_ip = ['127.0.0.1',]
        ip = request.META['REMOTE_ADDR']
        print('ip ', ip)
        if ip in allow_ip:
            print('ip not allowed')
            return HttpResponse('ip not allowed')

    def process_response(self, request, response):
        res = 'haha'
        print(res)
        return HttpResponse(res)