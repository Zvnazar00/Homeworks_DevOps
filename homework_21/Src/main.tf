provider "aws" {
  region = var.region
}

# VPC
data "aws_vpc" "default" { default = true }

# Security Group
resource "aws_security_group" "web_sg" {
  name   = "${var.name_prefix}-sg"
  vpc_id = data.aws_vpc.default.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = "${var.name_prefix}-key"
  public_key = file(var.public_key_path)
}

# EC2
resource "aws_instance" "web" {
  count         = var.instance_count
  ami           = "ami-0281b0943230d40d1" # Ubuntu 24.04 Frankfurt
  instance_type = "t3.micro"
  key_name      = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  associate_public_ip_address = true

  tags = { Name = "${var.name_prefix}-${count.index}" }
}

resource "null_resource" "mkdir" {
  provisioner "local-exec" {
    command = "mkdir -p ansible"
  }
}

resource "local_file" "ansible_inventory" {
  depends_on = [aws_instance.web, null_resource.mkdir]
  filename   = "${path.module}/ansible/hosts.txt"
  content    = <<-EOT
[nginx_hosts]
%{ for ip in aws_instance.web[*].public_ip ~}
${ip} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
%{ endfor ~}
EOT
}