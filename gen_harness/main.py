import os
import gen_harness.create_connector
from gen_harness.create_connector import HarnessConnector

base_url = os.getenv('HARNESS_BASE_URL')
org_name = os.getenv('HARNESS_ORG_NAME')
account_id = os.getenv('HARNESS_ACCOUNT_IDENTIFIER')
api_key = os.getenv('HARNESS_API_KEY')

url = '{}{}/api/connectors?accountIdentifier={}'.format(base_url, org_name, account_id)
print(url)
json_file = 'resources/connector.json'
harness_connector = HarnessConnector(url, json_file, api_key)
result = harness_connector.create_connector()
print(result)

if __name__ == '__main__':
    main()