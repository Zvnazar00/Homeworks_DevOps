terraform {
  backend "s3" {
    bucket         = "tf-tfstate-danit-11"
    key            = "state/zvenyhorodskyi.nazar/terraform.tfstate"
    encrypt        = true
    region         = "eu-central-1"
  }
}