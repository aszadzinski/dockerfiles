FROM archlinux/base

RUN pacman -Syu --noconfirm

RUN pacman -S wget awk grep filesystem cmake make vim gcc kdelibs4support git  xorg-server libglvnd libx11 root --noconfirm

WORKDIR /root/

RUN wget http://cern.ch/geant4-data/releases/geant4.10.05.p01.tar.gz \
	&& wget https://plutouser.github.io/v6.01/pluto_v6.01.tar.gz \
	&& tar xvf geant4.10.05.p01.tar.gz \
	&& tar xvf pluto_v6.01.tar.gz \
	&& rm geant4.10.05.p01.tar.gz \
	&& rm pluto_v6.01.tar.gz \
	&& mkdir geant4-install \
	&& mkdir geant4-build \
	&& mkdir pluto_v6.01/build \
	&& cd /root/geant4-build \
	&& cmake -DCMAKE_INSTALL_PREFIX=/root/geant4-install -DGEANT4_INSTALL_DATA=ON -DGEANT4_BUILD_MULTITHREADED=ON -DGEANT4_USE_OPENGL_X11=ON /root/geant4.10.05.p01/ \
	&& make -j5 \
	&& make install \
	&& rm -rf /root/geant4.10.05.p01/ \ 
	&& cd /root/pluto_v6.01/build \
	&& cmake ../ . \
	&& make -j4 \
	&& cd /root/ 

RUN echo "source /root/geant4-install/bin/geant4.sh; " >> .bashrc
RUN echo "echo "Opening run file..."; sh run; echo "Starting bash:"; bash" >> init.sh 

CMD sh init.sh
