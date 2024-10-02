from xmlrpc.server import SimpleXMLRPCServer


# Função do Sanji para preparar comida
def make_food(food):
    return f"Comida {food} está pronta!"


# Sanji escuta no Den Den Mushi (porta 8000)
sanji = SimpleXMLRPCServer(("localhost", 8000))
print("Sanji está pronto para cozinhar...")
sanji.register_function(make_food, "make_food")
sanji.serve_forever()
