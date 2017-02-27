import shodan
import sys

API_KEY = "gPKaAj5nTPzjVvWJX1KjXo01YRsog6E1"

if len(sys.argv) ==1:
	print 'Usage: %s <search query>' %sys.argv[0]
	sys.exit(1)

try:

	api = shodan.Shodan(API_KEY)

	query = ' '.join(sys.argv[1:])
	result = api.search('asd')

	for service in result['matches	']:
		print service['ip_str']

except Exception as e:
	print 'Error: %s' % e
	sys.exit(1)
