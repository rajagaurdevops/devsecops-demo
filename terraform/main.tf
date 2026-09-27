# Basic AWS S3 Bucket
# Note: This bucket is intentionally insecure for DevSecOps demo purposes (no encryption, public access)

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "devsecops-demo-bucket-${var.environment}"
}

resource "aws_s3_bucket_public_access_block" "demo_bucket_access" {
  bucket = aws_s3_bucket.demo_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
