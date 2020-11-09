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

from msrest.pipeline import ClientRawResponse

from .. import models


class TagOperations(object):
    """TagOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_list(
            self, name, last=None, n=None, orderby=None, digest=None, custom_headers=None, raw=False, **operation_config):
        """List tags of a repository.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param last: Query parameter for the last item in previous query.
         Result set will include values lexically after last.
        :type last: str
        :param n: query parameter for max number of items
        :type n: int
        :param orderby: orderby query parameter
        :type orderby: str
        :param digest: filter by digest
        :type digest: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TagList or ClientRawResponse if raw=true
        :rtype: ~azure.containerregistry.models.TagList or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.get_list.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if last is not None:
            query_parameters['last'] = self._serialize.query("last", last, 'str')
        if n is not None:
            query_parameters['n'] = self._serialize.query("n", n, 'int')
        if orderby is not None:
            query_parameters['orderby'] = self._serialize.query("orderby", orderby, 'str')
        if digest is not None:
            query_parameters['digest'] = self._serialize.query("digest", digest, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AcrErrorsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TagList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_list.metadata = {'url': '/acr/v1/{name}/_tags'}

    def get_attributes(
            self, name, reference, custom_headers=None, raw=False, **operation_config):
        """Get tag attributes by tag.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param reference: Tag name
        :type reference: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TagAttributes or ClientRawResponse if raw=true
        :rtype: ~azure.containerregistry.models.TagAttributes or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.get_attributes.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'reference': self._serialize.url("reference", reference, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AcrErrorsException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('TagAttributes', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_attributes.metadata = {'url': '/acr/v1/{name}/_tags/{reference}'}

    def update_attributes(
            self, name, reference, value=None, custom_headers=None, raw=False, **operation_config):
        """Update tag attributes.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param reference: Tag name
        :type reference: str
        :param value: Repository attribute value
        :type value: ~azure.containerregistry.models.ChangeableAttributes
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.update_attributes.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'reference': self._serialize.url("reference", reference, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if value is not None:
            body_content = self._serialize.body(value, 'ChangeableAttributes')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    update_attributes.metadata = {'url': '/acr/v1/{name}/_tags/{reference}'}

    def delete(
            self, name, reference, custom_headers=None, raw=False, **operation_config):
        """Delete tag.

        :param name: Name of the image (including the namespace)
        :type name: str
        :param reference: Tag name
        :type reference: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`AcrErrorsException<azure.containerregistry.models.AcrErrorsException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self.config.login_uri", self.config.login_uri, 'str', skip_quote=True),
            'name': self._serialize.url("name", name, 'str'),
            'reference': self._serialize.url("reference", reference, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.AcrErrorsException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/acr/v1/{name}/_tags/{reference}'}
