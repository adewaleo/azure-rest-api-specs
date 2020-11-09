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

from .manifest_py3 import Manifest


class OCIManifest(Manifest):
    """Returns the requested OCI Manifest file.

    :param schema_version: Schema version
    :type schema_version: int
    :param config: V2 image config descriptor
    :type config: ~azure.containerregistry.models.Descriptor
    :param layers: List of V2 image layer information
    :type layers: list[~azure.containerregistry.models.Descriptor]
    :param annotations:
    :type annotations: ~azure.containerregistry.models.Annotations
    """

    _attribute_map = {
        'schema_version': {'key': 'schemaVersion', 'type': 'int'},
        'config': {'key': 'config', 'type': 'Descriptor'},
        'layers': {'key': 'layers', 'type': '[Descriptor]'},
        'annotations': {'key': 'annotations', 'type': 'Annotations'},
    }

    def __init__(self, *, schema_version: int=None, config=None, layers=None, annotations=None, **kwargs) -> None:
        super(OCIManifest, self).__init__(schema_version=schema_version, **kwargs)
        self.config = config
        self.layers = layers
        self.annotations = annotations
