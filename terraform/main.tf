# Basic AWS S3 Bucket
# Note: This bucket is intentionally insecure for DevSecOps demo purposes (no encryption, public access)

provider "aws" {
  region = var.aws_region
}

# trivy:ignore:AVD-AWS-0132 (We don't want KMS encryption for this demo)
# trivy:ignore:AVD-AWS-0089 (We don't want access logging for this demo)
# trivy:ignore:AVD-AWS-0090 (We don't want versioning for this demo)
resource "aws_s3_bucket" "demo_bucket" {
  bucket = "devsecops-demo-bucket-${var.environment}"
}

resource "aws_s3_bucket_public_access_block" "demo_bucket_access" {
  bucket = aws_s3_bucket.demo_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

