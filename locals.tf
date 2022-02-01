locals {
  cmd = "${path.module}/scripts/spot-account"
  account_id = data.external.account.result["account_id"]
}