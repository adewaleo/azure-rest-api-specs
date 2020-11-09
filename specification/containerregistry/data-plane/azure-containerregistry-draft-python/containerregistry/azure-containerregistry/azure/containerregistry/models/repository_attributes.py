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


class RepositoryAttributes(Model):
    """Repository attributes.

    :param registry: Registry name
    :type registry: str
    :param image_name: Image name
    :type image_name: str
    :param created_time: Image created time
    :type created_time: str
    :param last_update_time: Image last update time
    :type last_update_time: str
    :param manifest_count: Number of the manifests
    :type manifest_count: int
    :param tag_count: Number of the tags
    :type tag_count: int
    :param changeable_attributes: Changeable attributes
    :type changeable_attributes:
     ~azure.containerregistry.models.ChangeableAttributes
    """

    _attribute_map = {
        'registry': {'key': 'registry', 'type': 'str'},
        'image_name': {'key': 'imageName', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'str'},
        'manifest_count': {'key': 'manifestCount', 'type': 'int'},
        'tag_count': {'key': 'tagCount', 'type': 'int'},
        'changeable_attributes': {'key': 'changeableAttributes', 'type': 'ChangeableAttributes'},
    }

    def __init__(self, **kwargs):
        super(RepositoryAttributes, self).__init__(**kwargs)
        self.registry = kwargs.get('registry', None)
        self.image_name = kwargs.get('image_name', None)
        self.created_time = kwargs.get('created_time', None)
        self.last_update_time = kwargs.get('last_update_time', None)
        self.manifest_count = kwargs.get('manifest_count', None)
        self.tag_count = kwargs.get('tag_count', None)
        self.changeable_attributes = kwargs.get('changeable_attributes', None)
