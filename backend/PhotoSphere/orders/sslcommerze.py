import os
from sslcommerz_lib import SSLCOMMERZ


def get_sslcommerz_settings(is_sandbox=True):
    return {
        'store_id': os.getenv('SSL_COMMERZ_STORE_ID'),
        'store_pass': os.getenv('SSL_COMMERZ_PASSWORD'),
        'issandbox': is_sandbox
    }


def get_hostname(request):
    scheme = 'https' if request.is_secure() else 'http'
    return '{scheme}://{host_name}'.format(scheme=scheme, host_name=request.get_host())


class SSLPaymentSessionGenerator:
    def __init__(self, transaction_id, total_amount, is_sandbox=True):
        self.request_maker = SSLCOMMERZ(get_sslcommerz_settings(is_sandbox=is_sandbox))
        self.has_customer_details_been_added = False
        self.has_product_details_been_added = False
        self.post_body = {
            'tran_id': transaction_id,
            'total_amount': total_amount,
            'currency': 'BDT',
            'success_url': '{host_name}/order/payment/success/'.format(host_name="http://127.0.0.1:8000"),
            'fail_url': '{host_name}/order/payment/failed/'.format(host_name="http://127.0.0.1:8000"),
            'cancel_url': '{host_name}/order/payment/canceled/'.format(host_name="http://127.0.0.1:8000"),
        }

    def add_customer_details(self, name, phone, email, address, city, country='Bangladesh'):
        self.has_customer_details_been_added = True
        self.post_body['cus_name'] = name
        self.post_body['cus_email'] = email
        self.post_body['cus_phone'] = phone
        self.post_body['cus_add1'] = address
        self.post_body['cus_city'] = city
        self.post_body['cus_country'] = country
        return self

    def add_product_details(self, name, category='Art Work', profile='general'):
        self.has_product_details_been_added = True
        self.post_body['shipping_method'] = "NO"
        self.post_body['product_name'] = name
        self.post_body['product_category'] = category
        self.post_body['product_profile'] = profile
        return self

    def get_session(self):
        assert self.has_customer_details_been_added
        assert self.has_product_details_been_added
        return self.request_maker.createSession(self.post_body)


class SSLPaymentSuccessValidator:
    def __init__(self, query_dict, is_sandbox=True):
        self.request_maker = SSLCOMMERZ(get_sslcommerz_settings(is_sandbox=is_sandbox))
        self.post_body = {}
        for key in query_dict:
            self.post_body[key] = query_dict.get(key)

    def is_valid(self):
        return self.request_maker.hash_validate_ipn(post_body=self.post_body)
