#!/usr/bin/env python
#
# query-summary.py
# Search Shodan and print summary information for the query.
#
# Author: achillean

import shodan
import sys

# Configuration
API_KEY = 'gPKaAj5nTPzjVvWJX1KjXo01YRsog6E1'

# The list of properties we want summary information on
FACETS = [
    'org',
    'domain',
    'port',
    'asn',

    # We only care about the top 5 countries, this is how we let Shodan know to return 5 instead of the
    # default 10 for a facet. If you want to see more than 10, you could do ('country', 1000) for example
    # to see the top 1,000 countries for a search query.
    ('country', 5),
]

FACET_TITLES = {
    'org': 'Top 10 Organizations',
    'domain': 'Top 10 Domains',
    'port': 'Top 10 Ports',
    'asn': 'Top 10 Autonomous Systems',
    'country': 'Top 5 Countries',
}

# Input validation
if len(sys.argv) == 1:
    print 'Usage: %s <search query>' % sys.argv[0]
    sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Generate a query string out of the command-line arguments
    query = ' '.join(sys.argv[1:])

    # Use the count() method because it doesn't return results and doesn't require a paid API plan
    # And it also runs faster than doing a search().
    result = api.count(query, facets=FACETS)

    print 'Shodan Summary Information'
    print 'Query: %s' % query
    print 'Total Results: %s\n' % result['total']

    # Print the summary info from the facets
    for facet in result['facets']:
        print FACET_TITLES[facet]

        for term in result['facets'][facet]:
            print '%s: %s' % (term['value'], term['count'])

        # Print an empty line between summary info
        print ''

except Exception, e:
    print 'Error: %s' % e
    sys.exit(1)
