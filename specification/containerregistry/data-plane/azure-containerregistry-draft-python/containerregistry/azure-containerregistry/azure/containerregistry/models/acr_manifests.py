# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AcrManifests(Model):
    """Manifest attributes.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param manifests_attributes: List of manifests
    :type manifests_attributes:
     list[~azure.containerregistry.models.ManifestAttributesBase]
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'manifests_attributes': {'key': 'manifests', 'type': '[ManifestAttributesBase]'},
    }

    def __init__(self, **kwargs):
        super(AcrManifests, self).__init__(**kwargs)
        self.registry = kwargs.get('registry', None)
        self.image_name = kwargs.get('image_name', None)
        self.manifests_attributes = kwargs.get('manifests_attributes', None)
