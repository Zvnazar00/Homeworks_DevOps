[nginx_hosts]
%{ for ip in ips ~}
${ip} ansible_user=ubuntu
%{ endfor ~}