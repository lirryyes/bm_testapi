FROM harbor.bluemoon.com.cn/lw/python_ssh_fastapi:3.7
RUN mkdir /opt/server && \
    pip install uvicorn && \
    pip install fastapi && \
    pip install PyExecJS
COPY ../bm-testapi-master/bm_testapi /opt/server
COPY ../bm-testapi-master/node-v12.18.3-linux-x64.tar.xz /opt/node-v12.18.3-linux-x64.tar.xz
RUN cd /opt && \
    tar -xvJf node-v12.18.3-linux-x64.tar.xz && \
    mv /opt/node-v12.18.3-linux-x64 /usr/local/nodejs && \
    rm /opt/node-v12.18.3-linux-x64.tar.xz && \
    sed -i '$a\export PATH=/usr/local/nodejs/bin:$PATH' /etc/profile

ENV PATH=/usr/local/nodejs/bin:$PATH
WORKDIR /opt/server
CMD [ "python","server.py" ]