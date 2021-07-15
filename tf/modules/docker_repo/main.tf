resource "google_container_registry" "registry" {
  project  = "flask-example"
  location = "EU"
}