variable "GCP_project" {
    type = string
    default = "flask-example-319821"
}

variable "region" {
    type = string
    default = "europe-west2"
}

provider "google" {
    credentials = file("../service_account.json")
    project     = var.GCP_project
    region      = var.region
}

resource "google_sql_database_instance" "master" {
  name             = "master-instance"
  database_version = "POSTGRES_11"
  region           =  var.region

  settings {
    tier = "db-f1-micro"
  }
}