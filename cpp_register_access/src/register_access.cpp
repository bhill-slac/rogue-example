#include <rogue/Logging.h>
#include <rogue/protocols/udp/Core.h>
#include <rogue/protocols/udp/Client.h>
#include <rogue/protocols/rssi/Client.h>
#include <rogue/protocols/rssi/Transport.h>
#include <rogue/protocols/rssi/Application.h>
#include <rogue/protocols/packetizer/CoreV2.h>
#include <rogue/protocols/packetizer/Transport.h>
#include <rogue/protocols/packetizer/Application.h>
#include <rogue/protocols/srp/SrpV3.h>
#include <rogue/interfaces/memory/Master.h>
#include <rogue/interfaces/memory/Constants.h>


int main (int argc, char **argv) {
   uint32_t ver;
   uint32_t spad;

   //rogue::Logging::setLevel(rogue::Logging::Debug);

   // Create the UDP client, jumbo = true
   rogue::protocols::udp::ClientPtr udp  = rogue::protocols::udp::Client::create("192.168.2.196",8192,true);
   udp->setRxBufferCount(64); // Make enough room for 64 outstanding buffers

   // RSSI
   rogue::protocols::rssi::ClientPtr rssi = rogue::protocols::rssi::Client::create(udp->maxPayload());
   udp->setSlave(rssi->transport());
   rssi->transport()->setSlave(udp);

   // Packetizer, ibCrc = false, obCrc = true
   rogue::protocols::packetizer::CoreV2Ptr pack = rogue::protocols::packetizer::CoreV2::create(false,true,true);
   rssi->application()->setSlave(pack->transport());
   pack->transport()->setSlave(rssi->application());

   // Create an SRP master and connect it to the packetizer
   rogue::protocols::srp::SrpV3Ptr srp = rogue::protocols::srp::SrpV3::create();
   pack->application(0)->setSlave(srp);
   srp->setSlave(pack->application(0));

   // Create a memory master and connect it to the srp
   rogue::interfaces::memory::MasterPtr mast = rogue::interfaces::memory::Master::create();
   mast->setSlave(srp);

   // Start the RSSI connection
   rssi->start();

   while ( ! rssi->getOpen() ) {
      sleep(1);
      printf("Establishing link ...\n");
   }

   ver = 0xFFFFFFFF;
   spad = 0xFFFFFFFF;

   // Read from fpga version
   mast->reqTransaction(0x00000000,4,&ver,rogue::interfaces::memory::Read);
   mast->reqTransaction(0x00000004,4,&spad,rogue::interfaces::memory::Read);
   mast->waitTransaction(0);

   printf("Register done. Value=0x%x, Spad=0x%x, Error=0x%x\n",ver,spad,mast->getError());
}

