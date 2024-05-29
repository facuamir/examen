# PARTE 1
# (class Producto) Desarrollar la clase Producto, que contará con los siguientes atributos.
# CODIGO: Identificador único. Formato: NNNN-XX donde N es numérico y X alfabético. Validar formato con
# expresiones regulares.
# DETALLE: Nombre del producto. Mínimo 1 carácter, Maximo 25 carácteres.
# USD COMPRA: Valor de importación.
# USD VENTA: Valor de comercialización.
# PESO: Peso unitario del producto en gramos.
# (Inventario) Desarrollar dos vectores que se comporten de manera paralela, donde un vector maneja códigos
# de productos y el otro vector, la cantidad total de productos (este valor debe coincidir con la sumatoria
# distribuida en los depósitos utilizado en [PARTE 2])
# 1 - ALTA DE PRODUCTO: Desarrollar la función producto_alta(path: str, inv1: list, inv2: list) -> bool, donde
# creará un nuevo producto y lo guardará en nuestra base de datos DB_PRODUCTOS.csv. Validar que no exista en
# nuestra base de datos el mismo código, de ser válida el alta, agregar el código de producto a nuestro inventario
# junto con la cantidad inicial en cero y guardarlo en nuestra base de datos. Devolverá un boolean por OK o FAIL.
# Informar por error: “[ERROR] Ítem existente.”
# 2 - BAJA DE PRODUCTO: Desarrollar la función producto_baja(path: str, inv1: list, inv2: list) -> bool, se
# encargará de listar todos los productos dados de alta, se seleccionara uno y solo se podrá dar de baja si la misma
# su cantidad en inventario es de cero; de ser asi, dar de baja en nuestra base de datos y en nuestro inventario.
# Informar por error: “[ERROR] Ítem con stock.”
# 3 - MODIFICAR PRODUCTO: Desarrollar la función producto_modificar_compra(path: str, codigo: str) y
# producto_modificar_venta(path: str, codigo: str), ambas funciones se encargan de setear un nuevo precio para
# la compra/venta del producto. Validar precio positivo. La modificación afectará a nuestra base de datos.
# 4 - LISTADO DE PRODUCTOS: Desarrollar la función producto_listar(path: str, inv1: list, inv2: list), donde
# desde nuestra base de datos e inventario, tome la información necesaria para listar la siguiente información:
# [CODIGO] [DETALLE] [PRECIO COMPRA] [PRECIO VENTA] [CANTIDAD EN INVENTARIO]

class Producto:
    def __init__(self, codigo, detalle, usd_compra, usd_venta, cantidad):
        self.codigo = codigo
        self.detalle = detalle
        self.usd_compra = usd_compra
        self.usd_venta = usd_venta
        self.cantidad = cantidad
class Inventario:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def producto_alta(self):
        codigo = input("Ingrese el código del producto: ")
        detalle = input("Ingrese el detalle del producto: ")
        usd_compra = float(input("Ingrese el precio de compra del producto: "))
        usd_venta = float(input("Ingrese el precio de venta del producto: "))
        cantidad = int(input("Ingrese la cantidad en inventario del producto: "))

        if any(p.codigo == codigo for p in self.productos):
            print("[ERROR] Ítem existente.")
            return False
        else:

            self.productos.append(Producto(codigo, detalle, usd_compra, usd_venta, cantidad))
            print("Producto agregado correctamente.")
            return True
    def producto_baja(self):

        if len(self.productos) == 0:
            print("[ERROR] No hay productos dados de alta.")
            return False
        print("Productos dados de alta:")
        for i, producto in enumerate(self.productos):
            print(f"{i+1}. {producto.detalle}")

        seleccion = int(input("Seleccione el número del producto a dar de baja: ")) - 1
        if seleccion < 0 or seleccion >= len(self.productos):
            print("[ERROR] Selección inválida.")
            return False
        if self.productos[seleccion].cantidad > 0:
            print("[ERROR] Ítem con stock.")
            return False
        else:
            del self.productos[seleccion]
            print("Producto dado de baja correctamente.")
            return True

    def producto_modificar_compra(self):
        codigo_producto = int(input("Ingrese el código del producto a modificar: "))
        nuevo_precio_compra = float(input("Ingrese el nuevo precio de compra: "))
        for producto in self.productos:
            if producto.codigo == codigo_producto:
                producto.usd_compra = nuevo_precio_compra
                print(f"Precio de compra del producto {producto.detalle} modificado correctamente.")
                return True
        print("[ERROR] Producto no encontrado.")
        return False

    def producto_modificar_venta(self):
        codigo_producto = int(input("Ingrese el código del producto a modificar: "))
        nuevo_precio_venta = float(input("Ingrese el nuevo precio de venta: "))
        for producto in self.productos:
            if producto.codigo == codigo_producto:
                producto.usd_venta = nuevo_precio_venta
                print(f"Precio de venta del producto {producto.detalle} modificado correctamente.")
                return True
        print("[ERROR] Producto no encontrado.")
        return False
inventario = Inventario()
while True:
    print("\n--- Menú ---")
    print("[1] Agregar Producto")
    print("[2] Dar de Baja Producto")
    print("[3] Modificar Precio de Compra")
    print("[4] Modificar Precio de Venta")
    print("[5] Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        inventario.producto_alta()
    elif opcion == "2":
        inventario.producto_baja()
    elif opcion == "3":
        inventario.producto_modificar_compra()
    elif opcion == "4":
        inventario.producto_modificar_venta()
    elif opcion == "5":
        print("Saliendo del programa...")
    break 
