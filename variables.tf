variable "name" {
  type        = string
  description = "Name of the account/project/subscription in Spot to retrieve accountID"
}

variable "spotinst_token" {
  type        = string
  description = "Token for Spot by NetApp"
  sensitive   = true
}