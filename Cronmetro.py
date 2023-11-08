import tkinter as tk
import time

class GuardadorTiempo:
    def __init__(self):
        self.tiempos_guardados = []

    def guardar(self, tiempo_actual):
        tiempo_formateado = self.formatear_tiempo(tiempo_actual)
        self.tiempos_guardados.append(tiempo_formateado)

    def obtener_tiempos_guardados(self):
        return self.tiempos_guardados

    def formatear_tiempo(self, tiempo):
        return time.strftime("%H:%M:%S", time.gmtime(tiempo))

class Cronometro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.guardador_tiempo = GuardadorTiempo()
        self.ventana.title("Cronómetro")

        self.tiempo_inicial = 0
        self.tiempo_actual = 0
        self.iniciado = False

        self.etiqueta = tk.Label(ventana, text="0:00:00", font=("Arial", 24))
        self.etiqueta.pack()

        self.boton_iniciar = tk.Button(ventana, text="Iniciar", command=self.iniciar)
        self.boton_pausar = tk.Button(ventana, text="Pausar", command=self.pausar)
        self.boton_guardar = tk.Button(ventana, text="Guardar", command=self.guardar_tiempo)
        self.boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=self.reiniciar)
        self.boton_ver_tiempos = tk.Button(ventana, text="Ver Tiempos Guardados", command=self.ver_tiempos_guardados)

        self.boton_iniciar.pack()
        self.boton_pausar.pack()
        self.boton_guardar.pack()
        self.boton_reiniciar.pack()
        self.boton_ver_tiempos.pack()

        self.actualizar()

    def iniciar(self):
        if not self.iniciado:
            self.iniciado = True
            self.tiempo_inicial = time.time() - self.tiempo_actual

    def pausar(self):
        if self.iniciado:
            self.iniciado = False
            self.tiempo_actual = time.time() - self.tiempo_inicial

    def guardar_tiempo(self):
        if self.iniciado:
            self.guardador_tiempo.guardar(self.tiempo_actual)

    def reiniciar(self):
        self.iniciado = False
        self.tiempo_inicial = 0
        self.tiempo_actual = 0
        self.etiqueta.config(text="0:00:00")

    def ver_tiempos_guardados(self):
        tiempos_guardados = self.guardador_tiempo.obtener_tiempos_guardados()
        ventana_tiempos = tk.Toplevel()
        ventana_tiempos.title("Tiempos Guardados")
        for tiempo in tiempos_guardados:
            tk.Label(ventana_tiempos, text=tiempo, font=("Arial", 16)).pack()

    def actualizar(self):
        if self.iniciado:
            self.tiempo_actual = time.time() - self.tiempo_inicial
        tiempo_formateado = self.guardador_tiempo.formatear_tiempo(self.tiempo_actual)
        self.etiqueta.config(text=tiempo_formateado)
        self.ventana.after(1000, self.actualizar)

if __name__ == '__main__':
    ventana_principal = tk.Tk()
    cronometro = Cronometro(ventana_principal)
    ventana_principal.mainloop()
