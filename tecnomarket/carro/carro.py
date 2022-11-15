class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre_producto,
                "precio":str(producto.precio),
                "cantidad":1,
                "subtotal":str(producto.precio),
                "imagen":producto.imagen_producto.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(producto.precio)
                    value["subtotal"]=float(producto.precio)*value["cantidad"]
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(producto.precio)
                value["subtotal"]=float(producto.precio)*value["cantidad"]
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break       
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
