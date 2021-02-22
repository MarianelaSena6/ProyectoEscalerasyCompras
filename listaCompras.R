#install.packages("rjason")
library(rjson)
library(dplyr)
library(tidyr)
library(date)

#setwd("C:.../Proyectos/compras") Set working directory

#Se lee el archivo .json:
comprasJson <- fromJSON("archivoCompras.json")


#Se convierte a data frame:
comprasDF <- comprasJson[["customer"]]$purchases%>% as.data.frame()

#Transformar columna de fechas de char a date
comprasDF$date = as.Date(comprasDF$date)

#Aplanar lista de compras para acceder a los datos
fechaySkuProducto <- (unnest_legacy(comprasDF) %>% select(date, sku))

#Obtener la cantidad de veces que se repiten los productos
#Se filtra los que se repiten al menos dos veces
cantidadPorProductos <- (unnest_legacy(comprasDF) %>%
                           select(date, sku) %>%
                           count(sku) %>%
                           filter(n>1))

#Se obtiene un JOIN entre los DF por el "sku" del producto
productosRepetidos <- merge(fechaySkuProducto,cantidadPorProductos,by="sku")


#Se separan los productos segun tengan el mismo "sku"
productosSeparados <- split(productosRepetidos, f = productosRepetidos$sku)


#La lista anterior contiene DataFrames
#Se envia al GlobalEnvironment los DF por separado
#list2env(productosSeparadosSku, .GlobalEnv)


#Fencion que calcula la fecha de recompra sacando el promedio de fechas de compra de los productos de diferente "sku"

calcularFechaRecompra <- function(){
  nroProductos= 1
  while (nroProductos <= (length(productosSeparados))){
    acum = 0 
    x = cantidadPorProductos$n[nroProductos]
    for (i in 2:x){
      acum =  acum  + (productosSeparados[[nroProductos]]$date[i] - productosSeparados[[nroProductos]]$date[i-1])
    }
    print(nroProductos)
    promedioFechas = acum/(x-1)
    print(promedioFechas)
    print(productosSeparados[[nroProductos]])
    fechaRecompra <- productosSeparados[[nroProductos]]$date[x] + promedioFechas
    print("Fecha de recompra")
    print(fechaRecompra)
    print("")
    nroProductos = nroProductos + 1}
}

calcularFechaRecompra()