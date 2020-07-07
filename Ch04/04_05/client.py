"""Example gRPC weather client"""
import grpc

import weather_pb2 as pb
import weather_pb2_grpc as gpb

# Create message
message = pb.Temperature(station='NYC', value=3.4)
message.time.GetCurrentTime()
print('sending:', message)


with grpc.insecure_channel('localhost:8888') as chan:
    stub = gpb.WeatherStub(chan)
    resp = stub.AddTemperature(message)
    print(f'Total of {resp.record_count} records')
