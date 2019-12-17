from django.shortcuts import render

class MagazineProfile(View):
    def get(self, request):
        cache_key = 'GOG-' + request.GET['issue_id']
        cache_time = 7200
        data = cache.get(cache_key)
        if not data:
            params = get_params(request)
            general_connector = MagazineProfileConnector().call_endpoints(params)
            data = json.dumps(general_connector)
            cache.set(cache_key, data, cache_time)
        response = HttpResponse(data)
        response ['content-type'] = 'application/json'
        response ['Cache-Control'] =  'no-cache'
        return response
