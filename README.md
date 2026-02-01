# napredne2
Naziv projekta:
2D celularni automati (Conway’s Game of Life)

Cilj projekta:
Cilj projekta je implementacija simulacije 2D celularnog automata kroz više iteracija, kao i poređenje sekvencijalne i paralelne implementacije u okviru istog programskog jezika.

Opis problema:
Simulira se 2D binarni celularni automat na mreži dimenzija N×M. Svaka ćelija može biti u stanju živa (1) ili mrtva (0). Stanje sistema se menja iterativno na osnovu stanja susednih ćelija po pravilima Conway’s Game of Life (Moore okolina). Granični uslovi su torus (wrap-around).

Tehnologije:

Programsko okruženje: Python 3

Paralelizacija: multiprocessing biblioteka

Izvršavanje: komandna linija (CLI)

Implementacija:

Sekvencijalna implementacija simulacije celularnog automata u Python-u.

Paralelna implementacija u Python-u korišćenjem multiprocessing biblioteke, gde se mreža deli po redovima između više procesa.

Svaka iteracija se računa na osnovu prethodnog stanja (double buffering).

Ulazni parametri:

Dimenzije mreže (N, M)

Broj iteracija (T)

Početno stanje (nasumično, uz zadati seed)

Izlaz:

Datoteka (states.csv) koja sadrži stanja sistema po iteracijama (za svaku iteraciju zapis stanja mreže).

Validacija:

Sekvencijalna i paralelna verzija moraju davati identične rezultate za iste ulazne parametre.

Obim projekta :
Projekat obuhvata samo Python implementaciju (sekvencijalnu i paralelnu).

