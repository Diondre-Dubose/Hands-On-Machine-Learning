FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python libraries via apt
RUN apt-get update && apt-get install -y \
    python3-numpy \
    python3-matplotlib \
    python3-seaborn \
    python3-flask \
    python3-sklearn \
    build-essential \
    procps \
    curl \
    file \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install kagglehub via pip (since it's not in apt)
RUN pip3 install --break-system-packages kagglehub

# Set working directory
WORKDIR /root/diondre

RUN git clone https://github.com/Diondre-Dubose/Hands-On-Machine-Learning.git

# Copy Dockerfile (if needed — usually not required inside the image itself)
# You probably want to copy your actual project files here
COPY Dockerfile /root/diondre/Hands-On-Machine-Learning/docker/
COPY requirements.txt /root/diondre/Hands-On-Machine-Learning/docker/


# Default command
CMD ["bash"]
