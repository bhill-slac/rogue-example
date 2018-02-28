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

      uint32_t getCount() { return rxCount; }
      uint32_t getBytes() { return rxBytes; }
      uint32_t getLast()  { return rxLast;  }

      void acceptFrame ( ris::FramePtr frame ) {
         rxLast = frame->getPayload();
         rxBytes += rxLast;
         rxCount++;
      }

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

