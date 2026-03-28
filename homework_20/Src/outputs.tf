output "instance_ip" {
  value = module.web_server.public_ip
}

output "web_url" {
  value       = "http://${module.web_server.public_ip}"
  description = "Клікніть по цьому посиланню, щоб перевірити Nginx"
}