# pluto-GSI Dockerfile

Container contains:

- ROOT6 (C++ data analysis framework and interpreter from CERN)
- pluto (A Monte Carlo simulation tool for hadronic physics)

[Container](https://cloud.docker.com/u/aszadzinski/repository/docker/aszadzinski/pluto-gsi)

## Building

clone repo:

`git clone https://github.com/aszadzinski/dockerfiles && cd dockerfiles/physics-simulations/pluto-GSI`

build container:

`docker build -t pluto-gsi`

or use  [link](https://cloud.docker.com/u/aszadzinski/repository/docker/aszadzinski/pluto-gsi):

`docker pull aszadzinski/pluto-gsi`

## Execute

Create _run.sh_ script with instructions and put to \<your_dir\> with all nessesery files. 

### Execute:

`docker run -v <your_dir>:/root/Public -t pluto-gsi`

**Container closes after execution _run.sh_**. In order to keep session alive type:

`docker run -v <your_dir>:/root/Public -it pluto-gsi bash`

and run `sh init.sh` to execute _run.sh_. 

All created files outside the Public folder will be lost after closing container. All generated data should be in a shared folder \<your_dir\>|Public.





