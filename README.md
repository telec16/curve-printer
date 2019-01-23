# Pour les fonctions du type z = f(x,y)

## Softs
* Python
 - Pandas
 - Numpy
 - Mathplotlib
 - =>depth.py
* Openscad
 - =>depth.scad

## Utilisation
### Python
CSV dans ./data/
Le programme va r�cup�rer autant de fonctions z=f(x) qu'il y a de CSV.
Il va ensuite faire une moyenne glissante et faire sauter des points (mean_length et step).
Puis il va 'empiler' sur y les fonctions r�cup�r�es pour obtenir une fonction z = f(x,y)
Finalement il sauve les donn�es dans depth.dat et affiche quelques graphiques
### Openscad
G�n�rer le STL gr�ce � openscad


# Pour les fonctions du type y=f(x), r�p�t�es sur z (non-bijectives)

## Softs
* Python
 - Pandas
 - Numpy
 - Mathplotlib
 - os
 - =>xy.py
* Openscad
 - =>xy.scad
* GhostScript
 - A installer
* pstoedit
 - A installer et mettre dans le path

## Utilisation
### Python
CSV dans ./data/
Le programme va r�cup�rer autant de fonctions y=f(x) qu'il y a de CSV.
Il va ensuite faire une moyenne glissante et faire sauter des points (mean_length et step).
Puis il affiche et enregistre chacune des courbes, et les tranforme en DXF avec pstoedit
### Openscad
G�n�rer le STL gr�ce � openscad
