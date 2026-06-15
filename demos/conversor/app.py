import web

urls = (
    '/','Index',
    '/conversor','Conversor'
)

app= web.application(urls,globals())
render= web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Conversor:
    temperatura = 0
    resultado = 0
    def GET(self):
        # primera vez que entra: todo en 0
        return render.conversor(0, 0)  # (temperatura, resultado)

    def POST(self):
        formulario = web.input()  # lee lo que mando el formulario
        operacion  = formulario['operacion']  # que boton presiono

        # limpiar va ANTES de float(), si no crashea
        if operacion == 'limpiar':
            return render.conversor(0, 0)

        # float() porque las temperaturas tienen decimales
        temperatura = float(formulario['temperatura'])

        if operacion == 'a_fahrenheit':       # boton "a Fahrenheit" (desde Celsius)
            resultado = (temperatura * 9/5) + 32

        elif operacion == 'a_kelvin':         # boton "a Kelvin" (desde Celsius)
            resultado = temperatura + 273.15

        elif operacion == 'a_celsius_f':      # boton "a Celsius" (desde Fahrenheit)
            resultado = (temperatura - 32) * 5/9

        elif operacion == 'a_celsius_k':      # boton "a Celsius" (desde Kelvin)
            resultado = temperatura - 273.15

        else:
            resultado = 0
 
        return render.conversor(temperatura,resultado)


if __name__ == '__main__':
    app.run()