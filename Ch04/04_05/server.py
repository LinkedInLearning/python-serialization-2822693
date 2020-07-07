"""Example gRPC weather server"""
import logging
from threading import Lock

import weather_pb2 as pb
import weather_pb2_grpc as gpb

db = []
lock = Lock()


class WeatherServer(gpb.WeatherServicer):
    def AddTemperature(self, request, context):
        with lock:
            logging.info('add: %r', request)
            db.append(request)
            record_count = len(db)
        return pb.AddReply(record_count=record_count)


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    import grpc

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    server = grpc.server(ThreadPoolExecutor())
    gpb.add_WeatherServicer_to_server(WeatherServer(), server)
    port = 8888
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info(f'server ready on {port}')
    server.wait_for_termination()
