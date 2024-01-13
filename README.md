# steamvr-vmat-generator
Some simple Python code I created to be able to mass-convert image files into .vmat files. This greatly speeds up the development process when importing a model from a site like Skecthfab.

This is a very simple script for converting images to simple VMAT files.

Keep in mind this will work ONLY for steamVR environments as far as I know, although I guess it could be modified to work with other source 2 versions.

It creates a standard vr shader and replaces the TextureColor with a path of the image that it found. Then it will save it as a .vmat file with the same name. (coconut.png => coconut.vmat)

It goes through every image that is in the same folder and WILL override any VMATs which are already written with the same name as an image.

Don't bother with cmd, just double-click it to run. Python must be installed of course.

For any qs feel free to contact me at adam.bajgar@gmail.com.

Adam Bajgar
