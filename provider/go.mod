module github.com/vincentbernat/pulumi-gandi/provider

go 1.16

replace (
	github.com/go-gandi/terraform-provider-gandi v1.1.2-0.20211213160242-5efce47f8b7f => github.com/vincentbernat/terraform-provider-gandi v1.1.2-0.20211221080826-5919ff43e733
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20210629210550-59d24255d71f
)

require (
	github.com/go-gandi/terraform-provider-gandi v1.1.2-0.20211213160242-5efce47f8b7f
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.13.0
	github.com/pulumi/pulumi/sdk/v3 v3.19.0
)
