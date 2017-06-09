#include <rogue/protocols/udp/Client.h>
#include <rogue/protocols/rssi/Client.h>
#include <rogue/protocols/rssi/Transport.h>
#include <rogue/protocols/rssi/Application.h>
#include <rogue/protocols/packetizer/Core.h>
#include <rogue/protocols/packetizer/Transport.h>
#include <rogue/protocols/packetizer/Application.h>
#include <rogue/interfaces/stream/Frame.h>

//! Receive slave data, count frames and total bytes for example purposes.
class TestSink : public rogue::interfaces::stream::Slave {

   public:

      uint32_t rxCount;
      uint64_t rxBytes;
      uint32_t rxLast;
      uint32_t rxLastB;

      TestSink() {
         rxCount = 0;
         rxBytes = 0;
         rxLast  = 0;
         rxLastB = 0;
      }

      void acceptFrame ( boost::shared_ptr<rogue::interfaces::stream::Frame> frame ) {
         rxLast   = frame->getPayload();
         rxLastB  = frame->getCount();
         rxBytes += rxLast;
         rxCount++;
      }
};


int main (int argc, char **argv) {
   struct timeval last;
   struct timeval curr;
   struct timeval diff;
   double   timeDiff;
   uint64_t lastBytes;
   uint64_t diffBytes;
   double bw;

   rogue::protocols::udp::ClientPtr udp  = rogue::protocols::udp::Client::create("192.168.2.187",8194,9000);
   udp->setRxSize(9000*36); // Make enough room for 36 outstanding buffers

   rogue::protocols::rssi::ClientPtr rssi = rogue::protocols::rssi::Client::create(9000);
   rogue::protocols::packetizer::CorePtr pack = rogue::protocols::packetizer::Core::create(9000);

   udp->setSlave(rssi->transport());
   rssi->transport()->setSlave(udp);

   rssi->application()->setSlave(pack->transport());
   pack->transport()->setSlave(rssi->application());

   boost::shared_ptr<TestSink> sink = boost::make_shared<TestSink>();
   pack->application(1)->setSlave(sink);

   lastBytes = 0;
   gettimeofday(&last,NULL);

   while(1) {
      sleep(10);
      gettimeofday(&curr,NULL);

      timersub(&curr,&last,&diff);

      diffBytes = sink->rxBytes - lastBytes;
      lastBytes = sink->rxBytes;

      timeDiff = (double)diff.tv_sec + ((double)diff.tv_usec / 1e6);
      bw = (((float)diffBytes * 8.0) / timeDiff) / 1e9;

      gettimeofday(&last,NULL);

      printf("RSSI = %i. RxLast=%i, RxCount=%i, RxTotal=%li, Bw=%f, DropRssi=%i, DropPack=%i\n",rssi->getOpen(),sink->rxLast,sink->rxCount,sink->rxBytes,bw,rssi->getDropCount(),pack->getDropCount());
   }
}

