from dash.serializers import DashboardSerializerElectro, DashboardSerializerFashion, DashboardSerializerHouseHome, DashboardSerializerKids, DashboardSerializerBeautyHealth


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
    elif tienda == "househome":
        serializer = DashboardSerializerHouseHome(data=body)
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
    elif tienda == "kids":
        serializer = DashboardSerializerKids(data=body)
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
    elif tienda == "beautyhealth":
        serializer = DashboardSerializerBeautyHealth(data=body)
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
