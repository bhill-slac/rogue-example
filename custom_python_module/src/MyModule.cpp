/* 
 *-----------------------------------------------------------------------------
 * Title      : Source code for MyModule
 *-----------------------------------------------------------------------------
 * File       : exoTest.py
 * Created    : 2018-02-28
 *-----------------------------------------------------------------------------
 * This file is part of the rogue_example software. It is subject to 
 * the license terms in the LICENSE.txt file found in the top-level directory 
 * of this distribution and at: 
 *    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html. 
 * No part of the rogue_example software, including this file, may be 
 * copied, modified, propagated, or distributed except according to the terms 
 * contained in the LICENSE.txt file.
 *-----------------------------------------------------------------------------
*/

#include <rogue/interfaces/stream/Slave.h>
#include <rogue/interfaces/stream/Frame.h>
#include <boost/python.hpp>
#include <boost/python/module.hpp>

namespace bp = boost::python;
namespace ris = rogue::interfaces::stream;

class TestSink : public rogue::interfaces::stream::Slave {
      uint32_t rxCount, rxBytes, rxLast;
   public:

      TestSink() { rxCount = 0; rxBytes = 0; rxLast = 0;}

      uint32_t getCount() { return rxCount; } // Total frames
      uint32_t getBytes() { return rxBytes; } // Total Bytes
      uint32_t getLast()  { return rxLast;  } // Last frame size

      void acceptFrame ( ris::FramePtr frame ) {
         uint32_t nbytes = frame->getPayload();
         rxLast   = nbytes;
         rxBytes += nbytes;
         rxCount++;

         // Iterators to start and end of frame
         rogue::interfaces::stream::Frame::iterator iter = frame->beginRead();
         rogue::interfaces::stream::Frame::iterator  end = frame->endRead();

         // Example destination for data copy
         uint8_t *buff = (uint8_t *)malloc (nbytes);
         uint8_t  *dst = buff;

         //Iterate through contigous buffers
         while ( iter != end ) {

            //  Get contigous size
            auto size = iter.remBuffer ();

            // Get the data pointer from current position
            auto *src = iter.ptr ();

            // Copy some data
            memcpy(dst, src, size);

            // Update destination pointer and source iterator
            dst  += size;
            iter += size;
         }
      }

      // Expose methods to python
      static void setup_python() {
         bp::class_<TestSink, boost::shared_ptr<TestSink>, bp::bases<ris::Slave>, boost::noncopyable >("TestSink",bp::init<>())
            .def("getCount", &TestSink::getCount)
            .def("getBytes", &TestSink::getBytes)
            .def("getLast",  &TestSink::getLast)
         ;
         bp::implicitly_convertible<boost::shared_ptr<TestSink>, ris::SlavePtr>();
      };
};

BOOST_PYTHON_MODULE(MyModule) {
   PyEval_InitThreads();
   try {
      TestSink::setup_python();
   } catch (...) {
      printf("Failed to load module. import rogue first\n");
   }
   printf("Loaded my module\n");
};

