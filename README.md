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
1. CSV dans ./data/
2. Le programme va récupérer autant de fonctions z=f(x) qu'il y a de CSV.
3. Il va ensuite faire une moyenne glissante et faire sauter des points (mean_length et step).
4. Puis il va 'empiler' sur y les fonctions récupérées pour obtenir une fonction z = f(x,y)
5. Finalement il sauve les données dans depth.dat et affiche quelques graphiques
### Openscad
Générer le STL grâce à openscad


# Pour les fonctions du type y=f(x), répétées sur z (non-bijectives)

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
1. CSV dans ./data/
2. Le programme va récupérer autant de fonctions y=f(x) qu'il y a de CSV.
3. Il va ensuite faire une moyenne glissante et faire sauter des points (mean_length et step).
4. Puis il affiche et enregistre chacune des courbes, et les tranforme en DXF avec pstoedit
### Openscad
Générer le STL grâce à openscad
