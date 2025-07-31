#!/bin/bash

apt-get update


apt-get install -y openjdk-17-jdk git wget ca-certificates curl gnupg lsb-release


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

systemctl enable docker
systemctl start docker


mkdir -p /home/vagrant/agent
cd /home/vagrant/agent

wget http://192.168.56.10:8080/jnlpJars/agent.jar
