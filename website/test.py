from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_598f1362-004c-4d26-be47-8cee94c488cc'

API_TOKEN = 'ISSecretKey_test_dca8e55e-97fa-43c8-a4b1-fff179cf560b'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)

create_order = service.collect.mpesa_stk_push(phone_number='+254757364069', 
                                              email='test@gmail.com', 
                                              amount=100,
                                              narrative='Purchase of Items')

print(create_order)