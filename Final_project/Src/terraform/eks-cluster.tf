resource "aws_eks_cluster" "danit" {
  name     = var.name
  role_arn = aws_iam_role.cluster.arn

  vpc_config {
    security_group_ids = [aws_security_group.danit-cluster.id]
    subnet_ids         = module.vpc.private_subnets
  }

  depends_on = [
    aws_iam_role_policy_attachment.kubeedge-cluster-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.kubeedge-cluster-AmazonEKSVPCResourceController,
    module.vpc # 
  ]

  tags = merge(
    var.tags,
    { Name = "${var.name}" }
  )
}

data "aws_eks_cluster_auth" "danit" {
  name = aws_eks_cluster.danit.name
}

resource "aws_eks_addon" "coredns" {
  cluster_name                = aws_eks_cluster.danit.name 
  addon_name                  = "coredns"
  resolve_conflicts_on_create = "OVERWRITE"

  depends_on = [aws_eks_node_group.danit]
}