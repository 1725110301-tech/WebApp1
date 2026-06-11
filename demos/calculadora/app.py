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
        return render.calculadora()

    def POST(self):
        formulario = web.input()

        operacion = formulario.operacion

        if operacion == "limpiar":
            return render.calculadora()

        numero1 = float(formulario.numero_1)
        numero2 = float(formulario.numero_2)

        if operacion == "sumar":
            resultado = numero1 + numero2

        elif operacion == "restar":
            resultado = numero1 - numero2

        elif operacion == "multiplicar":
            resultado = numero1 * numero2

        elif operacion == "dividir":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "Error"

        elif operacion == "potencia":
            resultado = numero1 ** numero2

        elif operacion == "modulo":
            resultado = numero1 % numero2

        elif operacion == "raiz":
            resultado = math.sqrt(numero1)

        page = str(render.calculadora())
        page = page.replace(
            'id="resultado"',
            f'id="resultado" value="{resultado}"'
        )

        return page


        # TODO: programar la operación sumar
        # TODO: programar la operación restar
        # TODO: programar la operación dividir
        # TODO: programar la operación multiplicar
        # TODO: programar la operación raiz cuadrada al numero_1
        # TODO: programar la operación potencia numero_1 ** numero_2
        # TODO: programar la operación modulo
        # TODO: programar la operación limpiar los valores

if __name__ == "__main__":
    app.run()