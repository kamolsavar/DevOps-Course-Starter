
variable "prefix" {
  description = "The prefix used for all resources in this environment"
}

variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default     = "uksouth"
}

variable "clientId" {
  description = "Application Client Id"
  default     = "3f595d12ffb8865be659"
}

variable "clientSecret" {
  description = "The Client secret for the Terraform app"
  default     = "c603a5441e90d11ac3490e055d04929ceca0fa41"
}

variable "databseName" {
  description = "The name of the database"
  default     = "kamol-terraform-cosmos-mongo-db"
}

variable "secretKey" {
  description = "The secret key"
  default     = "secret-key"
}

