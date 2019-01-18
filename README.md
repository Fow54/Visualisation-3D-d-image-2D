# Visualisation-3D-d-image-2D
Programme pour visualiser des modèles 3D construit à partir de propriétés induites d'une image 2D. Ce projet est réalisé par Khalid Aissi et Abresol Victor. Le projet est encadré par Romain Vuillemot (tuteur).

Etapes pour modéliser une image 2d en modèle 3D :

1-Choisir une image de format PNG
2-Mettez cette image dans le même répertoire que le programme python PNGToTxt
3-Executez le programme python
4-Copier le fichier obtenu dans le même répertoire ("file1.txt" par défault) et coller ce fichier dans le répertoire SimpleDataViewer-master
5-Lancer la scéne unity Demo1_simple et vous obtenez votre modèle

Facultatif :

-Changez le nom du fichier txt :

Si vous souhaitez changer le nom du fichier txt (file1.txt) alors il faut aussi le rennomer dans le programme unity "AsciiDataToParticle_simple" ligne 51

-Construire la coordonnée verticale (y) :

Pour changez la construction de la coordoonées verticale, il faut changer la ligne 72 du programme "AsciiDataToParticle_simple"

Cette ligne construit les trois coordonnées (x,y,z) en tant que vecteur de cette façon :
 _Atoms[_k]._position = new Vector3(float.Parse(_data[0]), (float.Parse(_data[3]) -float.Parse(_data[5])) * _j * 5, float.Parse(_data[1]));
 

data[0] correspond à la coordonnée x de l'image 2D
data[1] correspond à la coordonnée y de l'image 2D
data[3] correspond à la composante Rouge (R)
data[4] correspond à la composante Verte (G)
data[5] correspond à la composante Bleu (B)

-Construire le nombre de particule/couche sur l'axe vertical y :
Insérez le nombre de particule que vous souhaitez construire à la place du nombre 10 aux lignes 58 et 67 du programme "AsciiDataToParticle_simple"
