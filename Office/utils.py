from multitenant.settings import TENANTS_AND_DATABASE_MAPPING


def hostname_from_the_request(request):
	return request.get_host().split(":")[0].lower()


def tenant_db_from_the_request(request):
	hostname = hostname_from_the_request(request)
	tenants_map = get_tenants_map()
	return tenants_map.get(hostname)


def get_tenants_map():
	return TENANTS_AND_DATABASE_MAPPING
