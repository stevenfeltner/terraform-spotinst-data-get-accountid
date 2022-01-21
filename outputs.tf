output "spotinst_account" {
  description = "Spot account ID"
  value       = data.external.account.result["account_id"]
}


