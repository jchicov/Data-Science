#Aquí recopilaré todo el código que aprenda o se me ocurra y que me resulte útli para el Data Science
import numpy as np

#Calcula la media de una lista de valores
def mean_lst(lst):
  sum = 0
  l = len(lst)
  for i in lst:
    sum += i
  m = sum/l
  return(m)

#Calcula la varianza de una lista de valores
def var_lst(lst):
  media = mean(lst)
  l = []
  for i in lst:
    l.append((i-media0)**2)
  v = mean(l)
  return(v)

#Calcula la Desviación Típica (Standart Deviation) de una lista de valores
def sd_lst(lst):
  sd = (var(lst))**(0.5)
  return(sd)

