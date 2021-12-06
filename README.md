# Flask_app_on_kubernetes
A simple python web app written in Flask, turned into a Docker image, pushed into DockerHub and finally deployed on Google Kubernetes Engine as a Deployment resource. It listens on the port number 5000 exposing a REST api of the format &lt;localhost:5000/num> to which it prints the output: the square of &lt;num>. 
