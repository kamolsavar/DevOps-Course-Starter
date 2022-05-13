terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.49"
    } 
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "AmericanExpress21Group1_KamolSaha_ProjectExercise"
}
