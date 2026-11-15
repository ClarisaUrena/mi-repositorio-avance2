"""
Clarisa Ureña Segura clase 7:00-9:00 POO
Avance 3 (Final): Composición y Módulos - main.py

Archivo principal: solo importa las clases de modelos.py, crea los objetos
y ejecuta las pruebas de Herencia, Polimorfismo, Encapsulamiento y Composición.
"""

# 1. IMPORTACIÓN DE LAS CLASES DESDE EL MÓDULO modelos.py
from modelos import Propietario, Mascota, MascotaHospitalizada

# 2. INSTANCIACIÓN DE OBJETOS
dueno1 = Propietario("Laura Gómez", "33-1234-5678")
dueno2 = Propietario("Carlos Ruiz", "33-8765-4321")

mascota1 = Mascota("Firulais", "Perro", 5, 18.5, dueno1)  # Clase base
mascota2 = MascotaHospitalizada("Michi", "Gato", 2, 4.2, dueno2, "Infección respiratoria", 3)  # Subclase
mascota3 = MascotaHospitalizada("Copito", "Conejo", 1, 1.8, dueno2, "Problema digestivo", 2, costo_por_dia=350)  # Subclase

# 3. PRUEBA DE POLIMORFISMO (mostrar_ficha sobrescrito en la subclase)
print("=== Estado inicial ===")
for mascota in (mascota1, mascota2, mascota3):
    mascota.mostrar_ficha()

# 4. PRUEBA DE COMPOSICIÓN (la mascota delega en Consulta y Propietario)
print("=== Acciones en la veterinaria ===")
mascota1.registrar_consulta("revisión anual", 400)
mascota1.registrar_consulta("limpieza dental", 650)
mascota1.aplicar_vacuna("Rabia")
mascota1.aplicar_vacuna("Rabia")
mascota1.actualizar_peso(19.3)

mascota2.registrar_consulta("seguimiento", 300)
mascota2.aplicar_vacuna("Triple felina")
mascota2.actualizar_peso(4.0)

# 5. PRUEBA DE HERENCIA (métodos propios de la subclase)
mascota2.calcular_costo()
mascota2.extender_estancia(2)
mascota2.calcular_costo()
mascota3.calcular_costo()

print(f"\nContacto del dueño de Firulais (objeto contenido): {mascota1.propietario.contactar()}")
print(f"Total gastado por Firulais (suma de sus objetos Consulta): ${mascota1.total_gastado()} MXN")

# 6. PRUEBA DE ENCAPSULAMIENTO
print("\n=== Encapsulamiento ===")
print(f"Peso de Firulais (getter): {mascota1.peso} kg")
try:
    mascota1.peso = -3  # El setter rechaza valores inválidos
except ValueError as error:
    print(f"Error de validación: {error}")
try:
    print(mascota1.__peso)  # El atributo privado no es accesible directamente
except AttributeError:
    print("No se puede acceder directamente a __peso (atributo privado).")

# 7. INDEPENDENCIA DE LOS OBJETOS
print("\n=== Estado final (cada objeto conserva sus propios datos) ===")
for mascota in (mascota1, mascota2, mascota3):
    mascota.mostrar_ficha()
