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


class ManifestAttributesBase(Model):
    """Manifest details.

    :param digest: Manifest
    :type digest: str
    :param image_size: Image size
    :type image_size: long
    :param created_time: Created time
    :type created_time: str
    :param last_update_time: Last update time
    :type last_update_time: str
    :param architecture: CPU architecture
    :type architecture: str
    :param os: Operating system
    :type os: str
    :param media_type: Media type
    :type media_type: str
    :param config_media_type: Config blob media type
    :type config_media_type: str
    :param tags: List of tags
    :type tags: list[str]
    :param changeable_attributes: Changeable attributes
    :type changeable_attributes:
     ~azure.containerregistry.models.ChangeableAttributes
    """

    _attribute_map = {
        'digest': {'key': 'digest', 'type': 'str'},
        'image_size': {'key': 'imageSize', 'type': 'long'},
        'created_time': {'key': 'createdTime', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'str'},
        'architecture': {'key': 'architecture', 'type': 'str'},
        'os': {'key': 'os', 'type': 'str'},
        'media_type': {'key': 'mediaType', 'type': 'str'},
        'config_media_type': {'key': 'configMediaType', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'changeable_attributes': {'key': 'changeableAttributes', 'type': 'ChangeableAttributes'},
    }

    def __init__(self, *, digest: str=None, image_size: int=None, created_time: str=None, last_update_time: str=None, architecture: str=None, os: str=None, media_type: str=None, config_media_type: str=None, tags=None, changeable_attributes=None, **kwargs) -> None:
        super(ManifestAttributesBase, self).__init__(**kwargs)
        self.digest = digest
        self.image_size = image_size
        self.created_time = created_time
        self.last_update_time = last_update_time
        self.architecture = architecture
        self.os = os
        self.media_type = media_type
        self.config_media_type = config_media_type
        self.tags = tags
        self.changeable_attributes = changeable_attributes
