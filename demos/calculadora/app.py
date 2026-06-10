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
        return render.calculadora()

    def POST(self):
        formulario = web.input()
        numero1 = float(formulario.numero_1)
        numero2 = float(formulario.numero_2)
        resultado = numero1 + numero2
        page = str(render.calculadora())
        page = page.replace('id="resultado"', f'id="resultado" value="{resultado}"')
        return page


if __name__ == "__main__":
    app.run()
