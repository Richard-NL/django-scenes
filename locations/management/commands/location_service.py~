from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from django.core.management.base import BaseCommand, CommandError

from locations.DirectionHandler import DirectionHandler
from locations.DirectionService import Processor

class Command(BaseCommand):
    help = 'show the directions'

    def handle(self, *args, **options):
        handler = DirectionHandler()
        processor = Processor(handler)
        transport = TSocket.TServerSocket(port=9090)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()

        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        print "Starting python server..."
        server.serve()
        print "done!"