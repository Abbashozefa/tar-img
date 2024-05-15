## Steps to create tarball

Create a directory with ProjectName and two folders in it, charts and images

# Steps to create image and tar of image

In terminal run (Note : image name shoudl be in lowercase)
`docker build -t dsanokia/ss7lbnew .`

To check if image is create run
`docker images`

To get the tar file of the image, run 
`docker save dsanokia/ss7lbnew > ss7lbnew.tar`

Cut this image tar and paste it inside the images folder.

# Steps to create helm chart and tar of it

In terminal, run (Note : add suffix "chart" after the service name)
`helm create ss7lbnewchart`

Open values.yaml in the newly created chart and modify the following

repository : dsanokia/ss7lbnew
tag : "latest"
port : 5000

To create a tar of the chart, run 
`helm package ss7lbnewchart`

Cut this tar and add in the charts folder of the project directory

Tar the entire project 
`tar -cf project1.tar project1`

To untar, run 
`tar -xf project1.tar`








