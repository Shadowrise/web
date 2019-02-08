class CheckSessionMiidleware(object):
  
  def __init__(self, get_response):
        self.get_response = get_response

  def __call__(self, request):
      return self.get_response(request)
    
  def process_request(self, request):
    try:
      sessid = request.COOKIE.get('sessid')
      session = Session.objects.get(key=sessid, expires__gt=datetime.now(),)
      request.session = session
      request.user = session.user
    except Session.DoesNotExist:
      request.session = None
      request.user = No
