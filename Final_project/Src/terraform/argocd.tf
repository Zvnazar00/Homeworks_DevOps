resource "helm_release" "argocd" {
  name             = "argocd"
  repository       = "https://argoproj.github.io/argo-helm"
  chart            = "argo-cd"
  namespace        = "argocd"
  create_namespace = true

  values = [
    <<-EOF
    server:
      ingress:
        enabled: true
        ingressClassName: nginx
        annotations:
          external-dns.alpha.kubernetes.io/hostname: "argocd.${var.name}.${var.zone_name}"
        hosts:
          - "argocd.${var.name}.${var.zone_name}"
      extraArgs:
        - --insecure
    EOF
  ]

  depends_on = [helm_release.nginx_ingress]
}