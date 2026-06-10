import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)

app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Parametros:
    def GET(self):
        titulo = "Página con parametros"
        descripcion = '''Lorem ipsum dolor sit amet consectetur adipiscing elit augue tincidunt, feugiat aliquam volutpat ac lobortis bibendum iaculis. Facilisis sapien iaculis cubilia tristique suscipit varius himenaeos, ullamcorper ridiculus dignissim litora per morbi, vitae convallis sagittis dui luctus cum. Eleifend sed primis turpis facilisi tellus metus mattis auctor, eros torquent tincidunt vehicula et laoreet aptent dictumst posuere, non nullam eu lobortis luctus viverra curae.
        Aptent litora risus vestibulum per praesent platea nostra congue, turpis magnis eleifend dictumst posuere at. Tellus in leo cursus erat mi ridiculus est rhoncus, malesuada diam penatibus primis scelerisque gravida risus, ante vitae senectus blandit accumsan duis vulputate. Maecenas phasellus fusce integer facilisi praesent egestas augue vitae quam etiam quisque, magna enim suspendisse metus class habitant sociosqu cubilia curae.'''

        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()