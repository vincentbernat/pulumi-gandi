# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 owners: pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]],
                 admins: Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]] = None,
                 autorenew: Optional[pulumi.Input[bool]] = None,
                 billings: Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 teches: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[bool] autorenew: Should the domain autorenew
        :param pulumi.Input[str] name: The FQDN of the domain
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of nameservers for the domain
        """
        pulumi.set(__self__, "owners", owners)
        if admins is not None:
            pulumi.set(__self__, "admins", admins)
        if autorenew is not None:
            pulumi.set(__self__, "autorenew", autorenew)
        if billings is not None:
            pulumi.set(__self__, "billings", billings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nameservers is not None:
            warnings.warn("""This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""", DeprecationWarning)
            pulumi.log.warn("""nameservers is deprecated: This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""")
        if nameservers is not None:
            pulumi.set(__self__, "nameservers", nameservers)
        if teches is not None:
            pulumi.set(__self__, "teches", teches)

    @property
    @pulumi.getter
    def owners(self) -> pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]]:
        return pulumi.get(self, "owners")

    @owners.setter
    def owners(self, value: pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]]):
        pulumi.set(self, "owners", value)

    @property
    @pulumi.getter
    def admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]]:
        return pulumi.get(self, "admins")

    @admins.setter
    def admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]]):
        pulumi.set(self, "admins", value)

    @property
    @pulumi.getter
    def autorenew(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the domain autorenew
        """
        return pulumi.get(self, "autorenew")

    @autorenew.setter
    def autorenew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "autorenew", value)

    @property
    @pulumi.getter
    def billings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]]:
        return pulumi.get(self, "billings")

    @billings.setter
    def billings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]]):
        pulumi.set(self, "billings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the domain
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nameservers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of nameservers for the domain
        """
        return pulumi.get(self, "nameservers")

    @nameservers.setter
    def nameservers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nameservers", value)

    @property
    @pulumi.getter
    def teches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]]:
        return pulumi.get(self, "teches")

    @teches.setter
    def teches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]]):
        pulumi.set(self, "teches", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 admins: Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]] = None,
                 autorenew: Optional[pulumi.Input[bool]] = None,
                 billings: Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]]] = None,
                 teches: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        :param pulumi.Input[bool] autorenew: Should the domain autorenew
        :param pulumi.Input[str] name: The FQDN of the domain
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of nameservers for the domain
        """
        if admins is not None:
            pulumi.set(__self__, "admins", admins)
        if autorenew is not None:
            pulumi.set(__self__, "autorenew", autorenew)
        if billings is not None:
            pulumi.set(__self__, "billings", billings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nameservers is not None:
            warnings.warn("""This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""", DeprecationWarning)
            pulumi.log.warn("""nameservers is deprecated: This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""")
        if nameservers is not None:
            pulumi.set(__self__, "nameservers", nameservers)
        if owners is not None:
            pulumi.set(__self__, "owners", owners)
        if teches is not None:
            pulumi.set(__self__, "teches", teches)

    @property
    @pulumi.getter
    def admins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]]:
        return pulumi.get(self, "admins")

    @admins.setter
    def admins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainAdminArgs']]]]):
        pulumi.set(self, "admins", value)

    @property
    @pulumi.getter
    def autorenew(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the domain autorenew
        """
        return pulumi.get(self, "autorenew")

    @autorenew.setter
    def autorenew(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "autorenew", value)

    @property
    @pulumi.getter
    def billings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]]:
        return pulumi.get(self, "billings")

    @billings.setter
    def billings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainBillingArgs']]]]):
        pulumi.set(self, "billings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The FQDN of the domain
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nameservers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of nameservers for the domain
        """
        return pulumi.get(self, "nameservers")

    @nameservers.setter
    def nameservers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nameservers", value)

    @property
    @pulumi.getter
    def owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]]]:
        return pulumi.get(self, "owners")

    @owners.setter
    def owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainOwnerArgs']]]]):
        pulumi.set(self, "owners", value)

    @property
    @pulumi.getter
    def teches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]]:
        return pulumi.get(self, "teches")

    @teches.setter
    def teches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTechArgs']]]]):
        pulumi.set(self, "teches", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainAdminArgs']]]]] = None,
                 autorenew: Optional[pulumi.Input[bool]] = None,
                 billings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainBillingArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainOwnerArgs']]]]] = None,
                 teches: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTechArgs']]]]] = None,
                 __props__=None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] autorenew: Should the domain autorenew
        :param pulumi.Input[str] name: The FQDN of the domain
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of nameservers for the domain
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainAdminArgs']]]]] = None,
                 autorenew: Optional[pulumi.Input[bool]] = None,
                 billings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainBillingArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainOwnerArgs']]]]] = None,
                 teches: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTechArgs']]]]] = None,
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
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["admins"] = admins
            __props__.__dict__["autorenew"] = autorenew
            __props__.__dict__["billings"] = billings
            __props__.__dict__["name"] = name
            if nameservers is not None and not opts.urn:
                warnings.warn("""This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""", DeprecationWarning)
                pulumi.log.warn("""nameservers is deprecated: This nameservers attribute will be removed on next major release: the nameservers resource has to be used instead.
See https://github.com/go-gandi/terraform-provider-gandi/issues/88 for details.""")
            __props__.__dict__["nameservers"] = nameservers
            if owners is None and not opts.urn:
                raise TypeError("Missing required property 'owners'")
            __props__.__dict__["owners"] = owners
            __props__.__dict__["teches"] = teches
        super(Domain, __self__).__init__(
            'gandi:domain/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainAdminArgs']]]]] = None,
            autorenew: Optional[pulumi.Input[bool]] = None,
            billings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainBillingArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainOwnerArgs']]]]] = None,
            teches: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTechArgs']]]]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] autorenew: Should the domain autorenew
        :param pulumi.Input[str] name: The FQDN of the domain
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of nameservers for the domain
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["admins"] = admins
        __props__.__dict__["autorenew"] = autorenew
        __props__.__dict__["billings"] = billings
        __props__.__dict__["name"] = name
        __props__.__dict__["nameservers"] = nameservers
        __props__.__dict__["owners"] = owners
        __props__.__dict__["teches"] = teches
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def admins(self) -> pulumi.Output[Optional[Sequence['outputs.DomainAdmin']]]:
        return pulumi.get(self, "admins")

    @property
    @pulumi.getter
    def autorenew(self) -> pulumi.Output[Optional[bool]]:
        """
        Should the domain autorenew
        """
        return pulumi.get(self, "autorenew")

    @property
    @pulumi.getter
    def billings(self) -> pulumi.Output[Optional[Sequence['outputs.DomainBilling']]]:
        return pulumi.get(self, "billings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The FQDN of the domain
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nameservers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of nameservers for the domain
        """
        return pulumi.get(self, "nameservers")

    @property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Sequence['outputs.DomainOwner']]:
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter
    def teches(self) -> pulumi.Output[Optional[Sequence['outputs.DomainTech']]]:
        return pulumi.get(self, "teches")

