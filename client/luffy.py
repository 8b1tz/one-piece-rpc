import xmlrpc.client

# Luffy usa o Den Den Mushi (rede) para se comunicar com Sanji
den_den_mushi = xmlrpc.client.ServerProxy("http://localhost:8000/")
food_request = "carne"
print(f"Luffy: Quero {food_request} para quando eu voltar!")
response = den_den_mushi.make_food(food_request)
print(f"Sanji responde: {response}")
