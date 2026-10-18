"""
Clarisa Ureña Segura clase 7:00-9:00 POO
Avance 2: Herencia, Encapsulamiento y Diagrama UML

Sistema de una veterinaria. La clase base Mascota representa a cada paciente
registrado (nombre, especie, edad, peso, vacunas y consultas). La subclase
MascotaHospitalizada hereda de Mascota y agrega los datos de una internación
(diagnóstico, días internado y costo por día).
"""


# 1. CREACIÓN DE LA CLASE BASE (Superclase)
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        # Aplicación de Encapsulamiento: el peso se guarda en un atributo privado
        self.__peso = None
        self.peso = peso  # Pasa por el setter, así se valida desde que se crea el objeto
        self.vacunas = []
        self.consultas = 0

    # 2. APLICACIÓN DE ENCAPSULAMIENTO (@property)
    # Getter: consulta el peso privado de forma segura
    @property
    def peso(self):
        return self.__peso

    # Setter: modifica el peso solo si el valor es válido
    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El peso debe ser un número mayor que 0.")
        self.__peso = valor

    # Métodos de la clase base
    def registrar_consulta(self, motivo):
        self.consultas += 1
        print(f"[Consulta #{self.consultas}] {self.nombre} ({self.especie}) fue atendido por: {motivo}.")

    def aplicar_vacuna(self, vacuna):
        if vacuna in self.vacunas:
            print(f"{self.nombre} ya tiene la vacuna '{vacuna}'. No se repite.")
        else:
            self.vacunas.append(vacuna)
            print(f"Se aplicó la vacuna '{vacuna}' a {self.nombre}. "
                  f"Total de vacunas: {len(self.vacunas)}.")

    def actualizar_peso(self, nuevo_peso):
        peso_anterior = self.peso
        self.peso = nuevo_peso  # Usa el setter, que valida el valor
        diferencia = round(nuevo_peso - peso_anterior, 2)
        if diferencia > 0:
            print(f"{self.nombre} subió {diferencia} kg. Peso actual: {self.peso} kg.")
        elif diferencia < 0:
            print(f"{self.nombre} bajó {abs(diferencia)} kg. Peso actual: {self.peso} kg.")
        else:
            print(f"{self.nombre} mantiene su peso de {self.peso} kg.")

    def mostrar_ficha(self):
        vacunas = ", ".join(self.vacunas) if self.vacunas else "ninguna"
        print(f"--- Ficha de {self.nombre} ---")
        print(f"Especie: {self.especie} | Edad: {self.edad} años | Peso: {self.peso} kg")
        print(f"Vacunas: {vacunas}")
        print(f"Consultas realizadas: {self.consultas}\n")


# 3. USO DE super() Y HERENCIA (Subclase)
class MascotaHospitalizada(Mascota):
    def __init__(self, nombre, especie, edad, peso, diagnostico, dias_internado, costo_por_dia=500):
        # super() reutiliza el constructor de Mascota
        super().__init__(nombre, especie, edad, peso)
        # Atributos nuevos propios de la subclase
        self.diagnostico = diagnostico
        self.dias_internado = dias_internado
        # Atributo protegido (un guion bajo)
        self._costo_por_dia = costo_por_dia

    # Métodos propios de la subclase
    def extender_estancia(self, dias):
        self.dias_internado += dias
        print(f"{self.nombre} se queda {dias} día(s) más. Total internado: {self.dias_internado} días.")

    def calcular_costo(self):
        total = self.dias_internado * self._costo_por_dia
        print(f"Costo de hospitalización de {self.nombre}: ${total} MXN "
              f"({self.dias_internado} días x ${self._costo_por_dia}).")

    # 4. SOBRESCRITURA DE MÉTODOS (Polimorfismo)
    def mostrar_ficha(self):
        super().mostrar_ficha()  # Reutiliza la ficha de la clase base
        print(f"*** HOSPITALIZADO *** Diagnóstico: {self.diagnostico} | "
              f"Días internado: {self.dias_internado}\n")


# 5. INSTANCIACIÓN Y PRUEBAS
if __name__ == "__main__":
    # 1 objeto de la clase base y 2 de la subclase
    mascota1 = Mascota("Firulais", "Perro", 5, 18.5)
    mascota2 = MascotaHospitalizada("Michi", "Gato", 2, 4.2, "Infección respiratoria", 3)
    mascota3 = MascotaHospitalizada("Copito", "Conejo", 1, 1.8, "Problema digestivo", 2, costo_por_dia=350)

    print("=== Estado inicial (método mostrar_ficha, sobrescrito en la subclase) ===")
    mascota1.mostrar_ficha()
    mascota2.mostrar_ficha()
    mascota3.mostrar_ficha()

    print("=== Acciones en la veterinaria ===")
    mascota1.registrar_consulta("revisión anual")
    mascota1.aplicar_vacuna("Rabia")
    mascota1.aplicar_vacuna("Rabia")
    mascota1.actualizar_peso(19.3)

    # La subclase también usa los métodos heredados
    mascota2.registrar_consulta("seguimiento")
    mascota2.aplicar_vacuna("Triple felina")
    mascota2.actualizar_peso(4.0)
    mascota2.calcular_costo()
    mascota2.extender_estancia(2)
    mascota2.calcular_costo()

    mascota3.calcular_costo()

    print("\n=== Demostración de Encapsulamiento ===")
    print(f"Peso de Firulais (getter): {mascota1.peso} kg")
    try:
        mascota1.peso = -3  # El setter rechaza valores inválidos
    except ValueError as error:
        print(f"Error de validación: {error}")
    try:
        print(mascota1.__peso)  # El atributo privado no es accesible directamente
    except AttributeError:
        print("No se puede acceder directamente a __peso (atributo privado).")

    print("\n=== Estado final (cada objeto conserva sus propios datos) ===")
    mascota1.mostrar_ficha()
    mascota2.mostrar_ficha()
    mascota3.mostrar_ficha()
