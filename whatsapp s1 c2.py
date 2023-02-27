senders = ['tú', 'otra persona', 'tú', 'otra persona']
fechas = ['10/10/2020', '10/10/2020', '10/10/2020', '13/10/2020']
horas = ['18', '18', '18', '2']
minutos = ['50', '50', '51', '01']
mensajes = ['holi', 'hola', 'netflix and chill?', 'no']
sentimiento = ['casual', 'casual', 'romantico', 'bateao']


def senderIndice(arreglo):
    """Pasa el arreglo con los nombres de quién mandó el mensaje. """
    valoresUnicos = []
    indicesUnicos = []

    for elemento in arreglo:
        if elemento not in valoresUnicos:
            valoresUnicos.append(elemento)

    for elementoUnico in valoresUnicos:
        listaUnica = []
        for idx, elemento in enumerate(arreglo):
            if elemento == elementoUnico:
                listaUnica.append(idx)
                print(listaUnica)
            if idx == len(arreglo) - 1:
                indicesUnicos.append(listaUnica)
                print(indicesUnicos)

    return tuple(zip(indicesUnicos, valoresUnicos))


def poblarDiccionario(senders, fechas, horas, minutos, mensajes):
    diccionario = {}

    indices = senderIndice(senders)

    for elemento in indices:
        print(elemento)
        diccionario[elemento[1]] = {'fechas': [fechas[i] for i in elemento[0]],
                                    'horas': [horas[i] for i in elemento[0]],
                                    'minutos': [minutos[i] for i in elemento[0]],
                                    'mensajes': [mensajes[i] for i in elemento[0]],
                                    'sentimiento': [sentimiento[i] for i in elemento[0]]
                                    }
        print("Elemento 0 = ")
        print(elemento[0])
        print("Elemento 1 = ")
        print(elemento[1])
    return diccionario


baseDatos = poblarDiccionario(senders, fechas, horas, minutos, mensajes)

baseDatos['tú']