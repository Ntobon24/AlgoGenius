#from . import .

class ViewExercise:
    def __init__(self):
        self.solucion = Clase()


    def mostrar_menu():
        print("Programa de ejercicios de variaciones, permutaciones y combinaciones\n")

    while True:
        print("Responde las siguientes preguntas: ")    
        print("¿El orden en que se seleccionan los elementos importa? (s/n)")
        orden_importa = input().lower() == 's'

        print("¿Se repiten elementos en la selección? (s/n) ")
        elementos_se_repiten = input().lower() == 's'
            
        print("¿Entran todos los elementos disponibles? (s/n)")
        todos_elementos_seleccionados = input().lower() == 's'

        tecnica = self.determinar_tecnica(orden_importa, elementos_se_repiten, todos_elementos_seleccionados)
        print("La técnica que se debe utilizar es {tecnica}\n")

        print("¿Deseas resolver otro ejercicio? (s/n)")
        continuar = input().lower() == 's'
        if not continuar:
            break

        
    def determinar_tecnica(self, orden_importa, elementos_se_repiten, todos_elementos_seleccionados):
        if todos_elementos_seleccionados:
            if orden_importa:
                if elementos_se_repiten:
                    return "Permutaciones con repetición"
                else:
                    return "Permutaciones sin repetición"    
                
            else:
                return "El orden sí importa para las permutaciones"    
            
        else: 
            if orden_importa:
                if elementos_se_repiten:
                    return "Variaciones con repeticion"
                else:
                    return "Variaciones sin repeticion"     
                
            else:
                if elementos_se_repiten:
                    return "Combinaciones con repeticion"
                else: 
                    return "Combinaciones sin repeticion"
                

if __name__ == "__main__":
    vista = ViewExercise()
    vista.mostrar_menu()

            
