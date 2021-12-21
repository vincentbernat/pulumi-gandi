// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package email

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupMailbox(ctx *pulumi.Context, args *LookupMailboxArgs, opts ...pulumi.InvokeOption) (*LookupMailboxResult, error) {
	var rv LookupMailboxResult
	err := ctx.Invoke("gandi:email/getMailbox:getMailbox", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMailbox.
type LookupMailboxArgs struct {
	Domain    string `pulumi:"domain"`
	MailboxId string `pulumi:"mailboxId"`
}

// A collection of values returned by getMailbox.
type LookupMailboxResult struct {
	Domain string `pulumi:"domain"`
	// The provider-assigned unique ID for this managed resource.
	Id        string `pulumi:"id"`
	MailboxId string `pulumi:"mailboxId"`
}

func LookupMailboxOutput(ctx *pulumi.Context, args LookupMailboxOutputArgs, opts ...pulumi.InvokeOption) LookupMailboxResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMailboxResult, error) {
			args := v.(LookupMailboxArgs)
			r, err := LookupMailbox(ctx, &args, opts...)
			return *r, err
		}).(LookupMailboxResultOutput)
}

// A collection of arguments for invoking getMailbox.
type LookupMailboxOutputArgs struct {
	Domain    pulumi.StringInput `pulumi:"domain"`
	MailboxId pulumi.StringInput `pulumi:"mailboxId"`
}

func (LookupMailboxOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMailboxArgs)(nil)).Elem()
}

// A collection of values returned by getMailbox.
type LookupMailboxResultOutput struct{ *pulumi.OutputState }

func (LookupMailboxResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMailboxResult)(nil)).Elem()
}

func (o LookupMailboxResultOutput) ToLookupMailboxResultOutput() LookupMailboxResultOutput {
	return o
}

func (o LookupMailboxResultOutput) ToLookupMailboxResultOutputWithContext(ctx context.Context) LookupMailboxResultOutput {
	return o
}

func (o LookupMailboxResultOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMailboxResult) string { return v.Domain }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupMailboxResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMailboxResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupMailboxResultOutput) MailboxId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMailboxResult) string { return v.MailboxId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMailboxResultOutput{})
}
