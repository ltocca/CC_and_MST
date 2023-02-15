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
Inoltre, ad ogni arco di un grafo può essere assegnato un peso (che di solito corrisponde ad un numero reale, ma può essere anche ristretto agli interi).

I grafi sono utilizzati come strutture dati al fine di rappresentare relazioni tra elementi generici, espresse nel modo più semplice tramite gli archi, che evidenziano le connessioni tra gli elementi.

Per estrapolare ulteriori informazioni, si utilizzano le cosiddette componenti connesse e l'albero ricoprente minimo (o Minimum Spanning Tree in inglese), quest'ultimo tramite alcuni algoritmi, tra cui quello di Kruskal.
