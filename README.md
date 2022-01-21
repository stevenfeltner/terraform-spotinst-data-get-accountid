# Data-get-accountid

Module to call Spot API to retrieve the account ID

## Usage

```hcl
module "data-get-accountid" {
  source  = "stevenfeltner/data-get-accountid/spotinst"
  version = "0.1.0"
  name = "Sample Account"
  spotinst_token = "Redacted"
}

output "spotinst_account" {
  description = "Spot account ID"
  value       = module.data-get-accountid.spotinst_account
}
```

## Documentation

If you're new to [Spot](https://spot.io/) and want to get started, please checkout our [Getting Started](https://docs.spot.io/connect-your-cloud-provider/) guide, available on the [Spot Documentation](https://docs.spot.io/) website.

## Getting Help

We use GitHub issues for tracking bugs and feature requests. Please use these community resources for getting help:

- Ask a question on [Stack Overflow](https://stackoverflow.com/) and tag it with [terraform-spotinst](https://stackoverflow.com/questions/tagged/terraform-spotinst/).
- Join our [Spot](https://spot.io/) community on [Slack](http://slack.spot.io/).
- Open an issue.

## Community

- [Slack](http://slack.spot.io/)
- [Twitter](https://twitter.com/spot_hq/)

## Contributing

Please see the [contribution guidelines](.github/CONTRIBUTING.md).

## License

Code is licensed under the [Apache License 2.0](LICENSE).
