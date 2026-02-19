import time


def request_timing_middleware(get_response):
    def middleware(request):
        start = time.time()
        response = get_response(request)
        duration = time.time() - start
        print(f"Request {request.path} took {duration} to complete with status {response.status_code}")
        return response
    return middleware