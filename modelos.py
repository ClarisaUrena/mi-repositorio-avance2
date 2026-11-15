"""
Clarisa Ureña Segura clase 7:00-9:00 POO
Avance 3 (Final): Composición y Módulos - modelos.py

Contiene todas las clases del sistema de la veterinaria:
- Propietario y Consulta: clases auxiliares usadas en la Composición.
- Mascota: clase base (Encapsulamiento + Composición).
- MascotaHospitalizada: subclase (Herencia + Polimorfismo).
"""


# 1. CLASES AUXILIARES PARA COMPOSICIÓN
class Propietario:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def contactar(self):
        return f"{self.nombre} (Tel: {self.telefono})"


class Consulta:
    def __init__(self, motivo, costo):
        self.motivo = motivo
        self.costo = costo

    def descripcion(self):
        return f"{self.motivo} - ${self.costo} MXN"


# 2. CLASE BASE (Superclase)
class Mascota:
    def __init__(self, nombre, especie, edad, peso, propietario):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        # Encapsulamiento: el peso se guarda en un atributo privado
        self.__peso = None
        self.peso = peso  # Pasa por el setter, así se valida desde que se crea el objeto
        self.vacunas = []
        # Composición: una Mascota "tiene-un" Propietario y "tiene" varias Consultas
        self.propietario = propietario
        self._historial = []  # Lista de objetos Consulta (atributo protegido)

    # Encapsulamiento (@property)
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El peso debe ser un número mayor que 0.")
        self.__peso = valor

    @property
    def consultas(self):
        return len(self._historial)

    # Métodos de la clase base
    def registrar_consulta(self, motivo, costo=0):
        # Composición: se crea un objeto Consulta y se guarda dentro de la mascota
        consulta = Consulta(motivo, costo)
        self._historial.append(consulta)
        print(f"[Consulta #{self.consultas}] {self.nombre} ({self.especie}) "
              f"fue atendido por: {consulta.descripcion()}.")

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

    def total_gastado(self):
        # Delegación: cada objeto Consulta aporta su propio costo
        return sum(consulta.costo for consulta in self._historial)

    def mostrar_ficha(self):
        vacunas = ", ".join(self.vacunas) if self.vacunas else "ninguna"
        print(f"--- Ficha de {self.nombre} ---")
        print(f"Especie: {self.especie} | Edad: {self.edad} años | Peso: {self.peso} kg")
        print(f"Vacunas: {vacunas}")
        # Delegación: se usa el método del objeto Propietario contenido
        print(f"Propietario: {self.propietario.contactar()}")
        print(f"Consultas realizadas: {self.consultas} | Total gastado: ${self.total_gastado()} MXN\n")


# 3. SUBCLASE (Herencia con super())
class MascotaHospitalizada(Mascota):
    def __init__(self, nombre, especie, edad, peso, propietario, diagnostico, dias_internado, costo_por_dia=500):
        super().__init__(nombre, especie, edad, peso, propietario)
        self.diagnostico = diagnostico
        self.dias_internado = dias_internado
        self._costo_por_dia = costo_por_dia  # Atributo protegido

    def extender_estancia(self, dias):
        self.dias_internado += dias
        print(f"{self.nombre} se queda {dias} día(s) más. Total internado: {self.dias_internado} días.")

    def calcular_costo(self):
        total = self.dias_internado * self._costo_por_dia
        print(f"Costo de hospitalización de {self.nombre}: ${total} MXN "
              f"({self.dias_internado} días x ${self._costo_por_dia}).")

    # Sobrescritura (Polimorfismo)
    def mostrar_ficha(self):
        super().mostrar_ficha()
        print(f"*** HOSPITALIZADO *** Diagnóstico: {self.diagnostico} | "
              f"Días internado: {self.dias_internado}\n")
