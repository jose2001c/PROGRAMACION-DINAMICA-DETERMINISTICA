import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Grafo:
  def __init__(self,aristas, nodos):
    #inicializa un grafo vacio
    self.G=nx.DiGraph()
    #agrega los nodos y aristas
    self.aristas=aristas
    self.nodos=nodos
    for i in aristas:
      for j in i:
        self.G.add_edge(j[0],j[1],weight=j[2])

  def __hallar(self,origen,destino,i=-1,r={},min=True):
    #Este método se encarga de encontrar el valor minimo desde un nodo hasta el destino
    #Si el indice en el que se está mirando corresponde a la capa cero de aristas se termina el proceso
    if len(self.aristas)+i<0:
      return r
    #Se recorren las aristas en la capa i
    for j in self.aristas[i]:
      #Si el destino de la arista coincide con el destino entonces se asigna inmediatemante el peso hasta la arista
      if(j[1]==destino):
        r[j[0]]=(j[1],j[2])
      else:
        #Primero se asigna un valaor muy grande o muy pequeño, dependiendo de si se está optimizando o minimizando
        if not (j[0] in r):
          r[j[0]]=(None,np.infty if min else -np.infty)
        else:
          #Si se está minimizando y el camino evaluado desde un nodo hasta otro es menor que el peso asignado anteriormente, entonces se remplaza
          if (j[2]+r[j[1]][1])r[j[0]][1] and not min:
            r[j[0]]=(j[1],j[2]+r[j[1]][1])
    #Cuando se termina con la capa i, se procede con la capa i-1
    return self.__hallar(origen,destino,i-1,r,min)
def caminoA(self,origen,destino,min=True):
    #CaminoA es un método que sirve para juntar la ruta directamente
    r=self.__hallar(origen,destino,min=min)
    camino=[origen]
    while camino[-1]!=destino:
      camino.append(r[camino[-1]][0])
    return camino,r[camino[0]][1]


class Graficador:
  def __init__(self,grafo:Grafo):
    self.grafo=grafo

  def calcularpos(self):
    #calcular pos asigna unas coordenadas a cada nodo para asegurarse que se pueda mostrar de forma secuencial
    pos={}
    #básicamente se basa en el indice al que corresponde el nodo, exceptuando en la altura, en la cual ademas se suma el la distancia promedio para que quede centrado
    for i in range(len(self.grafo.nodos)):
      for j in range(len(self.grafo.nodos[i])):
        pos[self.grafo.nodos[i][j]]=(i,(-j+(len(self.grafo.nodos[i])-1)/2))
    return pos
  
  def graficar(self,opcionesNodos,opcionesAristas):
    pos=self.calcularpos()
    plt.figure(figsize=(9,9))
    #graficacion base del grafo
    nx.draw_networkx(self.grafo.G, pos,**opcionesNodos)
    edge_labels = nx.get_edge_attributes(self.grafo.G, "weight")
    #graficación de las aristas
    nx.draw_networkx_edge_labels(self.grafo.G, pos, edge_labels, **opcionesAristas)#edge_labels,label_pos=.8,rotate=False,font_size=12)
    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("Grafo.pdf",dpi=500)
    return plt


  def graficarCamino(self,A,B,min,opcionesNodos,opcionesAristas):
    plt=self.graficar(opcionesNodos,opcionesAristas)
    sol=self.grafo.caminoA(A,B,min)[0]
    pos=self.calcularpos()
    Gs=self.grafo.G.subgraph(sol)

    edge_labels = nx.get_edge_attributes(Gs, "weight")
    #Graficación del camino solucion
    nx.draw_networkx(Gs, pos,**opcionesNodos,edge_color="red")
   
    nx.draw_networkx_edge_labels(Gs, pos, edge_labels, **opcionesAristas)
    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("Grafosolucion.pdf",dpi=500)
    return plt