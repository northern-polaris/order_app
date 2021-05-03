import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.transaction import atomic
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from order_app.cons import ERROR_TYPE, HTTP_404, ERRORS, MESSAGE, OTHER, DATA, INVALID_DATA, INTEGRITY_ERROR, VALIDATION_ERROR
from order_app.exceptions import APIException202, InvalidData

logger = logging.getLogger(__name__)


class ParentListAPIView(ListAPIView):
    queryset = None
    serializer_class = None
    filter_serializer_class = None
    filter_map = {}
    queryset_kwargs = {}
    # permission_classes = [CanView]


class ParentCreateAPIView(CreateAPIView):

    @atomic
    # @permission_classes([CanAdd])
    def create(self, request, DATA=None, *args, **kwargs):
        data = {}
        if 'data' in request.data:  # POST request with FILES
            for key in request.FILES.keys():
                data[key] = request.FILES[key]
            post_data = json.loads(request.data['data'])
            data.update(post_data)
        else:  # SIMPLE POST request
            data = request.data
        write_serializer = self.get_serializer(data=data)
        response_data = {}
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        response_headers = None
        try:
            write_serializer.is_valid(raise_exception=True)
            instance = write_serializer.save()
            read_serializer = self.read_serializer_class(instance)
            # track_action(request.user, instance, ADDITION)
            headers = self.get_success_headers(read_serializer.data)
            response_data = {DATA: read_serializer.data}
            response_status = status.HTTP_201_CREATED
            response_headers = headers
        except ValidationError as ve:
            logger.error('Create Error: {}'.format(ve))
            error_dict = ve.get_full_details()
            response_data = {
                ERROR_TYPE: VALIDATION_ERROR,
                ERRORS: error_dict,
                # MESSAGE: get_validation_error_message(error_dict)
            }
            response_status = status.HTTP_400_BAD_REQUEST
        except ObjectDoesNotExist as dne:
            logger.error('Object does not exist Error: {}'.format(dne))
            response_data = {
                ERROR_TYPE: HTTP_404,
                ERRORS: '{}'.format(dne),
                MESSAGE: 'Nuk ekziston',
            }
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        except IntegrityError as ie:
            logger.error('{}'.format(ie))
            response_data = {
                ERROR_TYPE: INTEGRITY_ERROR,
                ERRORS: '{}'.format(ie),
                MESSAGE: 'Gabim në databazë',
            }
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        except InvalidData as ex:
            response_data = {
                ERROR_TYPE: INVALID_DATA,
                ERRORS: ex.get_message(),
                MESSAGE: ex.get_message(),
            }
            response_status = status.HTTP_400_BAD_REQUEST
        except APIException202 as ae:
            headers = self.get_success_headers(write_serializer.data)
            response_data = {DATA: ae.obj, MESSAGE: ae.message}
            response_status = status.HTTP_202_ACCEPTED
            response_headers = headers
        except Exception as e:
            response_data = {
                ERROR_TYPE: OTHER,
                ERRORS: '{}'.format(e),
                MESSAGE: 'Problem në server'
            }
        finally:
            return Response(response_data, status=response_status, headers=response_headers)


class ParentListCreateAPIView(ParentCreateAPIView, ParentListAPIView):
    list_read_serializer_class = None
    read_serializer_class = None
    write_serializer_class = None
    filter_serializer_class = None
    serializer_error_msg = "'%s' should either include a `serializer_class` attribute, or override the `get_serializer_class()` method."
    queryset = None
    filter_map = {}

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [CanView, ]
    #     if self.request.method == 'POST':
    #         self.permission_classes = [CanAdd, ]
    #     return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            if self.list_read_serializer_class is not None:
                return self.list_read_serializer_class
            assert self.read_serializer_class is not None or self.serializer_class is not None, (
                    self.serializer_error_msg % self.__class__.__name__)
            return self.read_serializer_class
        if self.request.method == 'POST':
            assert self.write_serializer_class is not None or self.serializer_class is not None, (
                    self.serializer_error_msg % self.__class__.__name__)
            return self.write_serializer_class
        assert self.serializer_class is not None, (self.serializer_error_msg % self.__class__.__name__)
        return self.serializer_class

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None or self.serializer_class is not None, (
                self.serializer_error_msg % self.__class__.__name__)
        return self.read_serializer_class


class ParentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an object instance.
    """
    queryset = None
    serializer_class = None
    read_serializer_class = None
    write_serializer_class = None
    serializer_error_msg = "'%s' should either include a `serializer_class` attribute, or override the `get_serializer_class()` method."
    delete_obj_id_physical = None

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         self.permission_classes = [CanView, ]
    #     if self.request.method == 'POST':
    #         self.permission_classes = [CanAdd, ]
    #     if self.request.method == 'PUT':
    #         self.permission_classes = [CanChange, ]
    #     if self.request.method == 'DELETE':
    #         self.permission_classes = [CanDelete, ]
    #     return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            assert self.read_serializer_class is not None or self.serializer_class is not None, (
                    self.serializer_error_msg % self.__class__.__name__)
            return self.read_serializer_class
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            assert self.write_serializer_class is not None or self.serializer_class is not None, (
                    self.serializer_error_msg % self.__class__.__name__)
            return self.write_serializer_class
        assert self.serializer_class is not None, (self.serializer_error_msg % self.__class__.__name__)
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({DATA: serializer.data})
        except Http404 as e:
            response_data = {
                ERROR_TYPE: HTTP_404,
                ERRORS: '{}'.format(e),
                MESSAGE: 'Nuk u gjet'
            }
            response_status = status.HTTP_404_NOT_FOUND
            return Response(response_data, status=response_status)

    @atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {}
        if 'data' in request.data:  # POST request with FILES
            for key in request.FILES.keys():
                data[key] = request.FILES[key]
            post_data = json.loads(request.data['data'])
            data.update(post_data)
        else:  # SIMPLE POST request
            data = request.data
        write_serializer = self.get_serializer(instance, data=data, partial=partial)

        response_data = {}
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:
            write_serializer.is_valid(raise_exception=True)
            # self.perform_update(write_serializer)
            instance = write_serializer.save()
            read_serializer = self.read_serializer_class(instance)

            # track_action(request.user, instance, CHANGE)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            response_data = {DATA: read_serializer.data}
            response_status = status.HTTP_200_OK
        except ValidationError as ve:
            logger.error('Create Error: {}'.format(ve))
            error_dict = ve.get_full_details()
            response_data = {
                ERROR_TYPE: VALIDATION_ERROR,
                ERRORS: error_dict,
                MESSAGE: get_validation_error_message(error_dict)
            }
            response_status = status.HTTP_400_BAD_REQUEST
        except ObjectDoesNotExist as dne:
            logger.error('Object does not exist Error: {}'.format(dne))
            response_data = {
                ERROR_TYPE: HTTP_404,
                ERRORS: '{}'.format(dne),
                MESSAGE: 'Nuk ekziston',
            }
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        except IntegrityError as ie:
            logger.error('{}'.format(ie))
            response_data = {
                ERROR_TYPE: INTEGRITY_ERROR,
                ERRORS: '{}'.format(ie),
                MESSAGE: 'Gabim në databazë',
            }
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        except InvalidData as ex:
            response_data = {
                ERROR_TYPE: INVALID_DATA,
                ERRORS: ex.get_message(),
                MESSAGE: ex.get_message(),
            }
            response_status = status.HTTP_400_BAD_REQUEST
        except APIException202 as ae:
            response_data = {DATA: ae.obj, MESSAGE: ae.message}
            response_status = status.HTTP_202_ACCEPTED
        except Exception as e:
            response_data = {
                ERROR_TYPE: OTHER,
                ERRORS: '{}'.format(e),
                MESSAGE: 'Problem në server'
            }
        finally:
            return Response(response_data, status=response_status)

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            # track_action(request.user, instance, DELETION)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404 as e:
            response_data = {
                ERROR_TYPE: HTTP_404,
                ERRORS: '{}'.format(e),
                MESSAGE: 'Nuk u gjet'
            }
            response_status = status.HTTP_404_NOT_FOUND
            return Response(response_data, status=response_status)
