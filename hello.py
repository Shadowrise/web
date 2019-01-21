def test(env, start_response):
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	body = env['QUERY_STRING'].replace('&','\n')
	return [body]
