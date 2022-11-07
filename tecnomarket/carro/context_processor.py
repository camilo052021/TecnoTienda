# Importamos el modelo de datos de productos:
def carritoCompras(request):
    total = 0 
    
    cantidad = 0 
    # Validación de que el carro exita:
    if 'carro' not in request.session:
        request.session['carro'] = {}
    # Validación si usuario está autenticado:
    if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total = total + (float(value['precio']) * float(value['cantidad']))
            cantidad = cantidad + int(value['cantidad'])
            
    return {'Total_Carro':total, 'Cantidad_Carro': cantidad}
