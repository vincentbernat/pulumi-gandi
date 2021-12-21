# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DnssecKeyArgs', 'DnssecKey']

@pulumi.input_type
class DnssecKeyArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input[int],
                 domain: pulumi.Input[str],
                 public_key: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        The set of arguments for constructing a DnssecKey resource.
        :param pulumi.Input[int] algorithm: DNSSEC algorithm type
        :param pulumi.Input[str] domain: Domain name
        :param pulumi.Input[str] public_key: DNSSEC public key
        :param pulumi.Input[str] type: DNSSEC key type
        """
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "public_key", public_key)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[int]:
        """
        DNSSEC algorithm type
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input[int]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Domain name
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[str]:
        """
        DNSSEC public key
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        DNSSEC key type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _DnssecKeyState:
    def __init__(__self__, *,
                 algorithm: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DnssecKey resources.
        :param pulumi.Input[int] algorithm: DNSSEC algorithm type
        :param pulumi.Input[str] domain: Domain name
        :param pulumi.Input[str] public_key: DNSSEC public key
        :param pulumi.Input[str] type: DNSSEC key type
        """
        if algorithm is not None:
            pulumi.set(__self__, "algorithm", algorithm)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[int]]:
        """
        DNSSEC algorithm type
        """
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Domain name
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        DNSSEC public key
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        DNSSEC key type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class DnssecKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DnssecKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] algorithm: DNSSEC algorithm type
        :param pulumi.Input[str] domain: Domain name
        :param pulumi.Input[str] public_key: DNSSEC public key
        :param pulumi.Input[str] type: DNSSEC key type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DnssecKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DnssecKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DnssecKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DnssecKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input[int]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = DnssecKeyArgs.__new__(DnssecKeyArgs)

            if algorithm is None and not opts.urn:
                raise TypeError("Missing required property 'algorithm'")
            __props__.__dict__["algorithm"] = algorithm
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            if public_key is None and not opts.urn:
                raise TypeError("Missing required property 'public_key'")
            __props__.__dict__["public_key"] = public_key
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(DnssecKey, __self__).__init__(
            'gandi:domain/dnssecKey:DnssecKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            algorithm: Optional[pulumi.Input[int]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'DnssecKey':
        """
        Get an existing DnssecKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] algorithm: DNSSEC algorithm type
        :param pulumi.Input[str] domain: Domain name
        :param pulumi.Input[str] public_key: DNSSEC public key
        :param pulumi.Input[str] type: DNSSEC key type
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DnssecKeyState.__new__(_DnssecKeyState)

        __props__.__dict__["algorithm"] = algorithm
        __props__.__dict__["domain"] = domain
        __props__.__dict__["public_key"] = public_key
        __props__.__dict__["type"] = type
        return DnssecKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Output[int]:
        """
        DNSSEC algorithm type
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Domain name
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        DNSSEC public key
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        DNSSEC key type
        """
        return pulumi.get(self, "type")

