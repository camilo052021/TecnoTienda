class Carro:
    # Constructor del carrito de compras:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        # Validación que exista el carrito:
        if not carro:
            carro =  self.session['carro']={}
        self.carro = carro

    # Métodos propios del carrito:
    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):   # Si el producto no se encuentra en el carro, agregar:
            self.carro[producto.id] = {                   # Creamos un diccionario con los atributos del producto, y este
                'producto_id': producto.id,               # se guarda por id, es decir por cada producto creamos esta 
                'nombre': producto.nombre_producto,       # estructura
                'precio': str(producto.precio),                # El campo precio lo pasamos como str,
                'cantidad': 1,
                'imagen': producto.imagen_producto.url,
            }
    
        else:
            # Si ya hay un producto actualizamos la cantidad de ese producto:
            for key, value in self.carro.items():                              # Recorremos todos los items del carrito 
                if key == str(producto.id):                                    # Si encontramos un producto que tiene ese id
                    value["cantidad"] = value["cantidad"] + 1                  # Sumamos el valor de la clave cantidad
                    value['precio'] = float(value['precio']) + producto.precio # Terminamos abruptamente el proceso
                    break
             # Por último guardamos el carrito de compras:
        self.guardarCarro()

    def guardarCarro(self):
        self.session['carro']=self.carro # Guardamos en la variable session, el objeto carro
        self.session.modified=True    # Asignamos el cambio de modificacion.

    def eliminar(self, producto):          
        producto.id = str(producto.id)   # asignamos el id delproducto
        if producto.id in self.carro:    # validamos que esté el producto en el carrito
            del self.carro[producto.id]  # Eliminamos el producto
            self.guardarCarro()          # Por último guardamos el carrito de compras: 

    def restarProducto(self, producto):                                    
        for key, value  in self.carro.items():                              # recorremos cada uno de los items del carrito
            if key == str(producto.id):                                     # si el id del producto es igual a la clave del objeto que estamos recorriendo
                value['cantidad'] = value['cantidad'] - 1                   # se toma el valor del item seleccionano y a la proiedad cantidad se le resta una unidad de la cantidad existente
                value['precio'] = float(value['precio']) - producto.precio  # lo mismo ocurre con la propiedad precio, se resta este completamente del objeto
                if value['cantidad'] < 1:                                   # evalua si la cantidad es menor que uno hace llamada a la función eliminar                                    
                    self.eliminar()
                break
        self.guardarCarro()                                                 # Por último guardamos el carrito de compras: 

    def limpiarCarro(self):
        self.session['carro'] = {}      # se referencia el carro de compras con el objeto session y se asigan un diccionario vacío
        self.session.modified = True    # se da procedencia  las modificaciones por medeio de un True en el metodo modified



