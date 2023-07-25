import pandas as pd
from data.platos import platosPopulares
from data.crearTabla import crearTabla
from data.reservas import reservas

from data.Proveedores import proveedores 

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos,"tablaplatospopulares")

tablaReservas=pd.DataFrame(reservas)
print(tablaReservas)
crearTabla(tablaReservas,"tablareservas")

tablaProveedores=pd.DataFrame(proveedores)
print(tablaProveedores)
crearTabla(tablaProveedores,"tablaProveedores")