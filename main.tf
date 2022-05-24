terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.49"
    } 
  }
  backend "azurerm" {
        resource_group_name  = "AmericanExpress21Group1_KamolSaha_ProjectExercise"
        storage_account_name = "kamol2022amex"
        container_name       = "terraform-state"
        key                  = "terraform.tfstate"
        access_key           = "aalgXIUW2QXHM5ngXCMtW3pq2bQsi7zVdQxqIn73HffrQbA1siAg6gZwxYTNmz7eVHBU93w7MAwrz3MwfJs5lg=="
    }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "AmericanExpress21Group1_KamolSaha_ProjectExercise"
}

resource "azurerm_app_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  kind                = "Linux"
  reserved            = true
  
  sku {
    tier = "Basic"
    size = "B1"
  } 
}

resource "azurerm_app_service" "main" {
  name                = "todo-terraform-app-kamol"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id

  site_config {
    app_command_line = ""
    linux_fx_version = "DOCKER|kamolsavar/todo-terraform-app:latest"
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "CLIENT_ID" = var.gitClientId
    "CLIENT_SECRET" = var.gitClientSecret
    "DATABASE_NAME" = var.databseName
    "DOCKER_ENABLE_CI" = true
    "MONGO_DB_CONNECTION" = azurerm_cosmosdb_account.db.connection_strings[0]
    "SECRET_KEY" = var.secretKey
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = false
  }

}

resource "azurerm_cosmosdb_account" "db" {
  name                = "tfex-cosmos-db-kamol-terraform-db"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities { 
    name = "EnableServerless" 
  }

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  lifecycle { 
    prevent_destroy = true 
    }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = data.azurerm_resource_group.main.location
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "myfirstTerraformDb" {
  name                = "kamol-terraform-cosmos-mongo-db"
  resource_group_name = azurerm_cosmosdb_account.db.resource_group_name
  account_name        = azurerm_cosmosdb_account.db.name
}
