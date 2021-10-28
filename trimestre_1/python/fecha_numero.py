def fecha():
    meses = ["",
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre"
        ]
    fecha = raw_input("Introduce una fecha(dd/mm/nn): ")
    dia, mes, anio = fecha.split("/")
    print "Feliz %s" % (meses[int(mes)])
    
fecha()
