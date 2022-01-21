# Call Spot API to create the Spot Account
resource "null_resource" "account" {
  triggers = {
    cmd     = "${path.module}/scripts/spot-account"
    name    = var.name
  }
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]
    command = "${self.triggers.cmd} get --filter=name=${self.triggers.name} --attr=account_id)"
  }
}
