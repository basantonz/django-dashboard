from dash.serializers import DashboardSerializerElectro, DashboardSerializerFashion, DashboardSerializerHouseful, DashboardSerializerKid, DashboardSerializerPets


def savedash(body, tienda):
    if tienda == "electro":
        serializer = DashboardSerializerElectro(data=body)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
        if serializer.is_valid():
            print("Se pudo guardar")
            serializer.save()
        else:
            print("No se pudo guardar")
        return True
    elif tienda == "fashion":
        serializer = DashboardSerializerFashion(data=body)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
        if serializer.is_valid():
            print("Se pudo guardar")
            serializer.save()
        else:
            print("No se pudo guardar")
        return True
    elif tienda == "houseful":
        serializer = DashboardSerializerHouseful(data=body)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
        if serializer.is_valid():
            print("Se pudo guardar")
            serializer.save()
        else:
            print("No se pudo guardar")
        return True
    elif tienda == "kid":
        serializer = DashboardSerializerKid(data=body)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
        if serializer.is_valid():
            print("Se pudo guardar")
            serializer.save()
        else:
            print("No se pudo guardar")
        return True
    elif tienda == "pets":
        serializer = DashboardSerializerPets(data=body)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
        if serializer.is_valid():
            print("Se pudo guardar")
            serializer.save()
        else:
            print("No se pudo guardar")
        return True
