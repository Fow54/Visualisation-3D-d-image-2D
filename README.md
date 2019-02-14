#3D model visualization

3D model visualization program built from induced properties of a 2D image.  The project is developped by Khalid Aissi and Abresol Victor and supervised by Romain Vuillemot (tutor).

Steps to Model a 2d Image into a 3D Model:

1-Choose a PNG format image

2-Put this image in the same directory as the python program PNGToTxt

3-Run the python program

4-Copy the file obtained in the same directory ("file1.txt" by default) and paste this file in the directory SimpleDataViewer-master

5-Launch the scene unites Demo1_simple and you get your model

Optional:

-Change the name of the txt file:

Name of the file txt (file1.txt) then it must also be read in the program unit "AsciiDataToParticle_simple" line 51

-Construct the vertical coordinate (y):

To change the construction of the vertical coordinates, you have to change the line 72 of the program "AsciiDataToParticle_simple"

This line is used for the three coordinates (x, y, z): _Atoms [_k] ._ position = new Vector3 (float.Parse (_data [0]), (float.Parse (_data [3]) -float. Parse (_data [5])) * _j * 5, float.Parse (_data [1]));

data [0] corresponds to the x coordinate of the 2D data image [1] corresponding to the y coordinate of the 2D data image [3] corresponding to the red component (R) data [4] corresponding to the Green component ( G) the data [5] corresponds to the blue component (B)

-Construct the number of particle / layer on the vertical axis and: Insert the number of particles you want to render instead of the number 10 to lines 58 and 67 of the program "AsciiDataToParticle_simple"
