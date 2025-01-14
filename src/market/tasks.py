from django.apps import apps



def sync_company_stock_quotes(company_id):
    Company = apps.get_model("market", "Company")
    company_obj = Company.objects.get(id=company_id)


def sync_stock_data():
    Company = apps.get_model("market", "Company")
    companies = Company.objects.filter(active=True).values_list('id')
    for company_id in companies:
        sync_company_stock_quotes(company_id)