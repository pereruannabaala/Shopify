from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_598f1362-004c-4d26-be47-8cee94c488cc'

API_TOKEN = 'ISSecretKey_test_e0561796-274b-458f-b0fa-76bbced5a59d'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)
