FROM archlinux/base

RUN pacman -Syu --noconfirm

RUN pacman -S wget awk grep filesystem cmake make vim gcc kdelibs4support git  xorg-server libglvnd libx11 --noconfirm

WORKDIR /root/

RUN wget http://cern.ch/geant4-data/releases/geant4.10.05.p01.tar.gz

RUN tar xvf geant4.10.05.p01.tar.gz 
RUN rm geant4.10.05.p01.tar.gz 
RUN mkdir geant4-install
RUN mkdir geant4-build

WORKDIR /root/geant4-build

RUN cmake -DCMAKE_INSTALL_PREFIX=/root/geant4-install -DGEANT4_INSTALL_DATA=ON -DGEANT4_BUILD_MULTITHREADED=ON -DGEANT4_USE_OPENGL_X11=ON /root/geant4.10.05.p01/
RUN make -j2
RUN make install
RUN rm -rf /root/geant4.10.05.p01/

WORKDIR /root/

RUN echo "source /root/geant4-install/bin/geant4.sh; " >> .bashrc

RUN echo "echo "Opening run file..."; sh run; echo "Starting bash:"; bash" >> init.sh 

CMD sh init.sh
