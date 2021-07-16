variable "GCP_project" {
    type = string
    default = "flask-example-319821"
}

variable "region" {
    type = string
    default = "europe-west2"
}

variable "environment" {
    type = string
    default = "staging"
}

provider "google" {
    credentials = file("../service_account.json")
    project     = var.GCP_project
    region      = var.region
}

resource "google_sql_database_instance" "master" {
  name                = "master-instance-staging"
  database_version    = "POSTGRES_11"
  region              =  var.region
  deletion_protection = false

  settings {
    tier = "db-f1-micro"
  }
}