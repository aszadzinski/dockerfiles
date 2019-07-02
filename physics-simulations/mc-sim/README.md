# MonteCarlo simulation toolkits  Dockerfile

Container contains:

- Geant4.10.05 (Monte Carlo GEometry ANd Tracking. A simulation toolkit for particle physics interactions)
- ROOT6 (C++ data analysis framework and interpreter from CERN)
- pluto (A Monte Carlo simulation tool for hadronic physics)
	

[Container](https://cloud.docker.com/repository/docker/aszadzinski/mc-sim)

## Building

clone repo:

`git clone https://github.com/aszadzinski/dockerfiles && cd dockerfiles/physics-simulations/mc-sim`

build container:

`docker build -t mc-sim .`

or use  [link](https://cloud.docker.com/repository/docker/aszadzinski/mc-sim):

`docker pull aszadzinski/mc-sim`

## Run

Create _run.sh_ script with instructions and put to \<your_dir\> with all nessesery files. 

### Execute:

`docker run -v <your_dir>:/root/Public -t mc-sim`

**Container closes after execution _run.sh_**. In order to keep session alive type:

`docker run -v <your_dir>:/root/Public -it mc-sim bash`

and run `sh init.sh` to execute _run.sh_. 

All created files outside the Public folder will be lost after closing container. All generated data should be in a shared folder \<your_dir\>|Public.





