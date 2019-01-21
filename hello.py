def test(env, start_response):
	status = '200 OK'
	data = env['QUERY_STRING'].replace('&','\n')
	headers = [('Content-Type', 'text/plain')]
	start_response(status, headers)
	return [data.encode('utf-8')]
