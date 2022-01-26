locals {
  cmd = "${path.module}/scripts/spot-account-id"
  account_id = data.external.account.result["account_id"]
}