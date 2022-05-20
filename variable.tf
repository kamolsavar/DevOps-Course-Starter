
variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default     = "uksouth"
}

variable "clientId" {
  description = "Application Client Id"
  sensitive = true
}

variable "clientSecret" {
  description = "The Client secret for the Terraform app"
  sensitive = true
}

variable "databseName" {
  description = "The name of the database"
  default     = "kamol-terraform-cosmos-mongo-db"
}

variable "secretKey" {
  description = "The secret key"
  default     = "secret-key"
}
