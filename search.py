import shodan
SHODAN_API_KEY = 'gPKaAj5nTPzjVvWJX1KjXo01YRsog6E1'
api=shodan.Shodan(SHODAN_API_KEY)


try:
	results = api.search('apache')
	print 'Results found: %s ' % results['total']
	for result in results['matches']:
		print 'IP: %s' % result['ip_str']
		print result['data']
		print ''

except shodan.APIError, e:
	print 'Error: %s' % e



# Lookup the host
host = api.host('217.140.75.46')

# Print general info
print """
        IP: %s
        Organization: %s
        Operating System: %s
""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))

# Print all banners
for item in host['data']:
        print """
                Port: %s
                Banner: %s

        """ % (item['port'], item['data'])