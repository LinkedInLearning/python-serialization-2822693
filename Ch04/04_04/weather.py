"""Example using protocol buffers"""
import weather_pb2 as pb

message = pb.Temperature(
    station='s42',
    value=17.8,
)
message.time.GetCurrentTime()  # Set current time
print('message', message)  # Representation, not serialization
data = message.SerializeToString()
print('data size:', len(data))

message2 = pb.Temperature.FromString(data)
print('message2', message2)
