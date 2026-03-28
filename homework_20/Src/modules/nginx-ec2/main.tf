# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = { Name = "${var.name_prefix}-vpc" }
}

# Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = { Name = "${var.name_prefix}-igw" }
}

# Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = { Name = "${var.name_prefix}-subnet" }
}

resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = { Name = "${var.name_prefix}-rt" }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.rt.id
}


# Security Group
resource "aws_security_group" "web_sg" {
  name   = "${var.name_prefix}-sg"
  vpc_id = aws_vpc.main.id

  dynamic "ingress" {
    for_each = var.list_of_open_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# AMI 
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
}

# EC2
resource "aws_instance" "nginx" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  
  user_data = <<-EOF
        #!/bin/bash
        apt-get update -y
        apt-get install -y nginx
        cat <<HTML > /var/www/html/index.html
        <!DOCTYPE html>
        <html>
        <head>
        <title>DevOps Project</title>
        <style>
                body {
                background-color: #2c3e50;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                .card {
                background: white;
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                text-align: center;
                }
                h1 { color: #e67e22; margin-bottom: 10px; }
                p { color: #7f8c8d; font-size: 1.2rem; }
                .badge {
                background: #27ae60;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-weight: bold;
                }
        </style>
        </head>
        <body>
        <div class="card">
                <h1>Welcome to Nginx Server</h1>
                <p>Deployed via <span class="badge">Terraform Modules</span></p>
                <p style="font-size: 0.9rem;">Infrastructure as Code Professional Solution</p>
        </div>
        </body>
        </html>
        HTML
        systemctl start nginx
        systemctl enable nginx
        EOF

  tags = { Name = "${var.name_prefix}-ec2" }
}
                                                                           
                                                                          