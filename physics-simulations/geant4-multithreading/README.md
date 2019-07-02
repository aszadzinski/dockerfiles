# Geant4-multithreading Dockerfile

Container contains:

- Geant4.10.05 (Monte Carlo GEometry ANd Tracking. A simulation toolkit for particle physics interactions)

with flags:
	- -DGEANT4\_INSTALL\_DATA
	- -DGEANT4\_BUILD\_MULTITHREADED
	- -DGEANT4\_USE\_OPENGL\_X11
	

[Container](https://cloud.docker.com/repository/docker/aszadzinski/geant4-multithreading)

## Building

clone repo:

`git clone https://github.com/aszadzinski/dockerfiles && cd dockerfiles/physics-simulations/geant4-multithreading`

build container:

`docker build -t g4-mt .`

or use  [link](https://cloud.docker.com/repository/docker/aszadzinski/geant4-multithreading):

`docker pull aszadzinski/geant4-multithreading`

## Run

Create _run.sh_ script with instructions and put to \<your_dir\> with all nessesery files. 

### Execute:

`docker run -v <your_dir>:/root/Public -t g4-mt`

**Container closes after execution _run.sh_**. In order to keep session alive type:

`docker run -v <your_dir>:/root/Public -it g4-mt bash`

and run `sh init.sh` to execute _run.sh_. 

All created files outside the Public folder will be lost after closing container. All generated data should be in a shared folder \<your_dir\>|Public.





