import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QComboBox, QPushButton, QLabel
from datetime import datetime

class SelectorHorario(QWidget):
    """
    Selector Inteligente de Horarios

    Descripción General:
    --------------------
    Este componente personalizado permite al usuario seleccionar una fecha utilizando un calendario,
    y automáticamente le muestra una lista de horarios disponibles para ese día. 
    Además, permite confirmar la selección y visualizar la fecha y hora elegida.

    Utilidad:
    ---------
    Facilita la gestión de citas o reservas de una manera rápida e intuitiva, 
    ideal para sistemas de reservas de consultorios, salones de belleza, entre otros.

    Componentes Gráficos Utilizados:
    --------------------------------
    - QCalendarWidget: Para la selección de fechas.
    - QComboBox: Para desplegar horarios disponibles.
    - QPushButton: Para confirmar la selección.
    - QLabel: Para mostrar el resultado al usuario.
    """

    def __init__(self):
        """
        Constructor del componente SelectorHorario.

        Inicializa la ventana y los componentes gráficos.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Configura la interfaz gráfica del selector de horarios.
        """
        self.setWindowTitle("Selector Inteligente de Horarios")

        # Crear y configurar los componentes gráficos
        self.calendario = QCalendarWidget(self)
        self.calendario.clicked.connect(self.load_available_times)  # Conectar la selección de fecha al método

        self.comboHorarios = QComboBox(self)  # Lista desplegable de horarios

        self.btnConfirmar = QPushButton("Confirmar Horario", self)
        self.btnConfirmar.clicked.connect(self.confirm_selection)  # Botón para confirmar selección

        self.lblResultado = QLabel("Seleccione una fecha y un horario", self)  # Etiqueta para mostrar el resultado

        # Layout para organizar los componentes
        layout = QVBoxLayout()
        layout.addWidget(self.calendario)
        layout.addWidget(self.comboHorarios)
        layout.addWidget(self.btnConfirmar)
        layout.addWidget(self.lblResultado)

        self.setLayout(layout)

    def load_available_times(self):
        """
        Carga los horarios disponibles para la fecha seleccionada.
        
        Por simplicidad, carga un listado fijo de horarios.
        """
        self.comboHorarios.clear()
        horarios = ["09:00 AM", "11:00 AM", "02:00 PM", "04:00 PM"]
        self.comboHorarios.addItems(horarios)

    def confirm_selection(self):
        """
        Confirma la selección de fecha y horario y muestra el resultado en pantalla.
        """
        fecha = self.calendario.selectedDate().toString("dd/MM/yyyy")
        horario = self.comboHorarios.currentText()
        self.lblResultado.setText(f"Seleccionado: {fecha} a las {horario}")

if __name__ == '__main__':
    """
    Punto de entrada de la aplicación.

    Instrucciones:
    --------------
    Para ejecutar, asegúrese de tener instaladas las dependencias:
    - PyQt5

    Instalación de PyQt5:
    ---------------------
    Puede instalarse mediante pip:
    pip install PyQt5
    """
    app = QApplication(sys.argv)
    ventana = SelectorHorario()
    ventana.show()
    sys.exit(app.exec_())
