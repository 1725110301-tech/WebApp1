import web

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
        titulo = "Calculadora"
        descripcion = "Una calculadora de dos numeros"
        return render.calculadora(titulo, descripcion)
    def POST(self):
        formulario = web.input
        numero1 = formulario['numero_1']
        numero2 = formulario['numero_2']
        suma = 
        return numero1
    


if __name__ == "__main__":
    app.run()