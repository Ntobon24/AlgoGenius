import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from Taller_3.Model.Algoritmos.Insercion import insertion_sort
from Taller_3.Model.Algoritmos.Radix import radix_sort
from Taller_3.Model.Algoritmos.Bucket import bucket_sort
from Taller_3.Model.Algoritmos.Burbuja import bubble_sort
from Taller_3.Model.Algoritmos.Seleccion import selection_sort
from Taller_3.Model.Algoritmos.CountingSort import counting_sort
from Taller_3.Model.Algoritmos.HeapSort import heap_sort
from Taller_3.Model.Algoritmos.QuickSort import quick_sort
from Taller_3.Model.Algoritmos.MergeSort import merge_sort
from Taller_3.Model.Model import data


class SortingApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # Crear un menú desplegable para seleccionar la columna
        self.columna_spinner = Spinner(
            text='Seleccione la columna',
            values=('punt_global', 'punt_lectura_critica', 'punt_matematicas', 'punt_c_naturales', 'punt_sociales_ciudadanas', 'punt_ingles')
        )
        root.add_widget(self.columna_spinner)

        # Crear un menú desplegable para seleccionar el algoritmo de ordenamiento
        self.algoritmo_spinner = Spinner(
            text='Seleccione el algoritmo',
            values=('Insercion', 'Radix', 'Bucket', 'Burbuja', 'Seleccion', 'Counting Sort', 'Heap Sort', 'Quick Sort', 'Merge Sort')
        )
        root.add_widget(self.algoritmo_spinner)

        # Agregar un botón para iniciar el ordenamiento
        sort_button = Button(text='Ordenar', size_hint=(1, None), height=40)
        sort_button.bind(on_press=self.sort_data)
        root.add_widget(sort_button)

        # Crear un widget de texto para mostrar los resultados
        self.result_textinput = TextInput(readonly=True, multiline=True)
        root.add_widget(self.result_textinput)

        return root

    def sort_data(self, instance):
        # Obtener la columna seleccionada y el algoritmo de los menús desplegables
        selected_column = self.columna_spinner.text
        selected_algorithm = self.algoritmo_spinner.text

        # Llamar al algoritmo de ordenamiento correspondiente
        if selected_algorithm == 'Insercion':
            insertion_sort(data, selected_column)
        elif selected_algorithm == 'Radix':
            radix_sort(data, selected_column)
        elif selected_algorithm == 'Bucket':
            bucket_sort(data, selected_column)
        elif selected_algorithm == 'Burbuja':
            bubble_sort(data, selected_column)
        elif selected_algorithm == 'Seleccion':
            selection_sort(data, selected_column)
        elif selected_algorithm == 'Counting Sort':
            counting_sort(data, selected_column)
        elif selected_algorithm == 'Heap Sort':
            heap_sort(data, selected_column)
        elif selected_algorithm == 'Quick Sort':
            quick_sort(data, selected_column)
        elif selected_algorithm == 'Merge Sort':
            merge_sort(data, selected_column)

        # Mostrar los resultados en el widget de texto
        self.result_textinput.text = json.dumps(data, indent=4)


if __name__ == "__main__":
    SortingApp().run()
