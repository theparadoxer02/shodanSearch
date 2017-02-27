from django.shortcuts import render
import shodan
import sys
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def shodsearch(request):
	if request.method == 'POST':
		term = request.POST.get("q")
		API_KEY = "gPKaAj5nTPzjVvWJX1KjXo01YRsog6E1"
		api = shodan.Shodan(API_KEY)
		result = api.search(term)
		final = []
		subtitle = "The following IPs were detected :"
		for ip in result['matches']:
			final.append(ip['ip_str'])
		#paginator = Paginator(final,10)
		# print (final)
		# page = request.GET.get('page')
		# try:
		# 	ips = paginator.page(page)
		# except PageNotAnInteger:
		# 	ips = paginator.page(1)
		# except EmptyPage:
		# 	ips = paginator.page(paginator.num_pages)
		return render(request,'shodan_search.html', {'IPS': final,'subtitle':subtitle })
	else:
		return render(request,'shodan_search.html')


def index2(request):
	return render(request,'custom_index.html')