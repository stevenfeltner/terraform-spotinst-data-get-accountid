# Retrieve the Spot Account ID Information
data "external" "account" {
  program = [
    local.cmd,
    "get",
    "--filter=name=${var.name}",
    "--token=${var.spotinst_token}"
  ]
}