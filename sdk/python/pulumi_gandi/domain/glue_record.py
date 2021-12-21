# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GlueRecordArgs', 'GlueRecord']

@pulumi.input_type
class GlueRecordArgs:
    def __init__(__self__, *,
                 ips: pulumi.Input[Sequence[pulumi.Input[str]]],
                 zone: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GlueRecord resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: List of IP addresses
        :param pulumi.Input[str] zone: Domain name
        :param pulumi.Input[str] name: Host name of the glue record
        """
        pulumi.set(__self__, "ips", ips)
        pulumi.set(__self__, "zone", zone)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of IP addresses
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Input[str]:
        """
        Domain name
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Host name of the glue record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _GlueRecordState:
    def __init__(__self__, *,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GlueRecord resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: List of IP addresses
        :param pulumi.Input[str] name: Host name of the glue record
        :param pulumi.Input[str] zone: Domain name
        """
        if ips is not None:
            pulumi.set(__self__, "ips", ips)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of IP addresses
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Host name of the glue record
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Domain name
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class GlueRecord(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a GlueRecord resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: List of IP addresses
        :param pulumi.Input[str] name: Host name of the glue record
        :param pulumi.Input[str] zone: Domain name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GlueRecordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a GlueRecord resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param GlueRecordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlueRecordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlueRecordArgs.__new__(GlueRecordArgs)

            if ips is None and not opts.urn:
                raise TypeError("Missing required property 'ips'")
            __props__.__dict__["ips"] = ips
            __props__.__dict__["name"] = name
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__.__dict__["zone"] = zone
        super(GlueRecord, __self__).__init__(
            'gandi:domain/glueRecord:GlueRecord',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'GlueRecord':
        """
        Get an existing GlueRecord resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: List of IP addresses
        :param pulumi.Input[str] name: Host name of the glue record
        :param pulumi.Input[str] zone: Domain name
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GlueRecordState.__new__(_GlueRecordState)

        __props__.__dict__["ips"] = ips
        __props__.__dict__["name"] = name
        __props__.__dict__["zone"] = zone
        return GlueRecord(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Output[Sequence[str]]:
        """
        List of IP addresses
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Host name of the glue record
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        Domain name
        """
        return pulumi.get(self, "zone")

