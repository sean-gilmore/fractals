# fractals

Drawing fractals with Python

Build the image:

docker build . -t fractals

Run the image:

docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" fractals
