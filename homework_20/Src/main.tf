module "web_server" {
  source             = "./modules/nginx-ec2"
  list_of_open_ports = var.list_of_open_ports
  instance_type      = var.instance_type
  name_prefix        = var.name_prefix
}