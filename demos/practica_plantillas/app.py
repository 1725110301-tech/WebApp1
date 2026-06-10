import web

urls = (
    '/', 'Index',
    '/productos', 'Productos',
    '/clientes', 'Clientes',
    '/usuarios', 'Usuarios',
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.index()

class Productos:
    def GET(self):
        return render.productos()

class Clientes:
    def GET(self):
        return render.clientes()

class Usuarios:
    def GET(self):
        return render.usuarios()

if __name__ == "__main__":
    app.run()