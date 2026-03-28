variable "list_of_open_ports" {
  type        = list(number)
  default     = [80, 22]
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "name_prefix" {
  type    = string
  default = "danit-hw20"
}