#!/bin/bash

apt-get update
apt-get install -y ca-certificates curl gnupg lsb-release


install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg


echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null


apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin


groupadd docker || true
usermod -aG docker vagrant


cp /vagrant/Dockerfile /home/vagrant/Dockerfile
docker build -t jenkins-server /home/vagrant


docker volume create jenkins-data

docker run --name jenkins-blueocean --restart=on-failure -d \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins-server
