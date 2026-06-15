import web
import math

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)

app = web.application(urls, globals())
render = web.template.render('calc')
class Index:
    def GET(self):
        return render.index()
class Calculadora:
    def GET(self):
        numero_1 = 0
        numero_2 = 0
        resultado = 0
        return render.calculadora(numero_1, numero_2, resultado)

    def POST(self):
        formulario = web.input()

        operacion = formulario['operacion']

        if operacion == "limpiar":
            return render.calculadora(0, 0, 0)

        numero_1 = int(formulario['numero_1'])
        numero_2 = int(formulario['numero_2'])

        if operacion == "sumar":
            resultado = numero_1 + numero_2

        elif operacion == "restar":
            resultado = numero_1 - numero_2

        elif operacion == "multiplicar":
            resultado = numero_1 * numero_2

        elif operacion == "dividir":
            if numero_2 != 0:
                resultado = numero_1 / numero_2
            else:
                resultado = "Error"

        elif operacion == "potencia":
            resultado = numero_1 ** numero_2

        elif operacion == "modulo":
            if numero_2 != 0:
                resultado = numero_1 % numero_2
            else:
                resultado = "Error"

        elif operacion == "raiz":
            if numero_1 >= 0:
                resultado = math.sqrt(numero_1)
            else:
                resultado = "Error"

        else:
            resultado = 0

        return render.calculadora(numero_1, numero_2, resultado)


if __name__ == "__main__":
    app.run()