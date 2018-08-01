# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import customer_pb2 as customer__pb2


class CustomerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomers = channel.unary_stream(
        '/customer.Customer/GetCustomers',
        request_serializer=customer__pb2.CustomerFilter.SerializeToString,
        response_deserializer=customer__pb2.CustomerRequest.FromString,
        )
    self.CreateCustomer = channel.unary_unary(
        '/customer.Customer/CreateCustomer',
        request_serializer=customer__pb2.CustomerRequest.SerializeToString,
        response_deserializer=customer__pb2.CustomerResponse.FromString,
        )


class CustomerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCustomers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateCustomer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomers': grpc.unary_stream_rpc_method_handler(
          servicer.GetCustomers,
          request_deserializer=customer__pb2.CustomerFilter.FromString,
          response_serializer=customer__pb2.CustomerRequest.SerializeToString,
      ),
      'CreateCustomer': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCustomer,
          request_deserializer=customer__pb2.CustomerRequest.FromString,
          response_serializer=customer__pb2.CustomerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'customer.Customer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
