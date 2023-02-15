---
author:

- Leonardo Toccafondi   
  date: February 15, 2022
  title: Componenti connesse e Minimium Spanning Tree di un grafo

---

# Introduzione

## Grafi

Un grafo $G$ è un insieme di elementi detti **vertici** (o nodi) che possono essere collegati fra di loro tramite linee chiamate **archi**. In particolare, si dice grafo la coppia ordinata di insiemi $G = (V, E)$, dove $V$ è l’insieme dei vertici di $G$ e $E$ è l’insieme degli archi di $G$.
Un grafo si dice **orientato** (o **diretto**) se $E$ è un insieme di archi *orientati*, cioè con una direzione (da sorgente a destinazione). Viceversa, un grafo si dice **non orientato** (o **indiretto**) se gli archi non sono orientati, dunque se la connessione tra due vertici ij ha lo stesso significato della connessione ji.
Si definisce come grado di un vertice: numero di archi che incidono nel vertice.
Inoltre, ad ogni arco di un grafo può essere assegnato un peso (che di solito corrisponde ad un numero reale, ma può essere anche ristretto agli interi).

I grafi sono utilizzati come strutture dati al fine di rappresentare relazioni tra elementi generici, espresse nel modo più semplice tramite gli archi, che evidenziano le connessioni tra gli elementi.

#### Rappresentazione

Un grafo può essere rappresentato con due tipologie di strutture dati:

- **Lista di adiacenza:** composta da un vettore $Adj$ composto da $|V|$ liste, una per ogni nodo, dove $Adj[u]$ contiene tutti i vertici $v$ t.c. $(u, v) \in E)$.
  
  La lista di adiacenza richiede uno spazio di memoria $\Theta(V + E)$, e un tempo $\Theta(u.degree)$ per determinare se due vertici qualsiasi $(u, v) \in E$.
  In questo caso $u.degree$ rappresenta il **grado** del vertice (u).

- **Matrice di adiacenza:** si introduce una matrice $A$ di dimensione $|V|\times|V|$, dove ogni elemento $(i,j)$ ha valore 1 se $(i, j) \in E)$, cioè se il vertice (j) è adiacente a (i), e valore 0 altrimenti. 
  La matrice di adiacenza richiede uno spazio di memoria $\Theta(V^2)$, quindi peggiore rispetto alla lista, però consente di determinare se due vertici qualsiasi $(u, v) \in E)$ in un tempo $\Theta(1)$, in quanto è sufficiente accedere all’elemento $A[u][v]$ e controllarne il valore.
  In generale, una matrice di adiacenza è più indicata per descrivere grafi densi e con molti archi.

Per gli esperimenti svolti sono state utilizzate entrambe le strutture dati.

Per estrapolare ulteriori informazioni, si utilizzano le cosiddette componenti connesse e l'albero ricoprente minimo (o Minimum Spanning Tree in inglese), quest'ultimo tramite alcuni algoritmi, tra cui quello di Kruskal. Tuttavia, è necessario prima introdurre una struttura dati per degli insiemi disgiunti, nota anche come *Union-find*

#### Union find

Gestisce una collezione di insiemi dinamici, ciascuno identificato da un rappresentante,
ovvero un elemento dell'insieme qualsiasi, a patto che rimanga sempre lo stesso.
Su questa struttura dati possiamo operare con tre funzioni:

- MakeSet(x): aggiunge alla collezione un nuovo insieme creato a partire dall’elemento x;

- FindSet(x): restituisce il rappresentante dell’insieme che contiene x;

- Union(x,y): se $x \in S_x, y \in S_y, \ \Rightarrow S \leftarrow S_x -S_y \bigcup \{S_x \cup S_y)$ 
  Quindi aggiunge alla collezione un nuovo insieme contenente gli elementi degli insiemi di x e y, e poi elimina gli insiemi d’origine. Il rappresentante diventa uno degli elementi di $S_x$ o di $S_y$

## Componenti connesse

Dato un grafo $G=(V,E)$, una componente connessa é un insieme massimale di vertici $C⊆V$ tale che per ogni coppia di nodi esiste un cammino che li collega. 
Sono utilizzate ad esempio per trovare "oggetti" all'interno di immagini, interpretando come nodi i singoli pixel dell'immagine stessa
L'algoritmo utilizzato all'interno di questo esperimento si basa sull'utilizzo di union-find come struttura dati.

## Albero ricoprente minimo (MST)

Si tratti di un albero di connessione T (sottoinsieme dell'insieme di archi $E$ come un grafo non diretto $G=(V,E)$) in cui la somma dei pesi dei suoi archi:

> $w(T) = \sum_{(u,v) \in T} \ w(u, v)$ 

sia minimo e connetta tutti i vertici.
Un MST ha $|V|-1$ archi, non ha cicli e *può non essere unico*.

Esiste un algoritmo generico che permette di costruire la soluzione e consiste in creare un insieme vuoto di archi $A$, per poi aggiungerne progressivamente conservando l'invariante di ciclo:

> ”Se A é un sottoinsieme di qualche MST, l’arco $(u,v)$ é *sicuro* per A se e solo se $A∪(u,v)$ é sottoinsieme di un qualche MST.”

Da questo è possibile ricavare che al fine di ottenere un albero ricoprente minimo sia necessario aggiungere solamente $N-1$ archi *sicuri*, con $N$ pari al numero di nodi.

Per ottenere l'algoritmo di Kruskal, che sarà utilizzato per gli esperimenti, è necessario introdurre il seguente *teorema*:

> "Sia A un sottoinsieme di qualche MST, $(S,V-S)$ un taglio che rispetta $A$ e $(u,v)$ un arco leggero che attraversa $(S,V-S)$. Allora $(u,v)$ é sicuro per $A$."

Anche in questo caso per l'implementazione pratica viene utilizzata la struttura dati *Union-find*
