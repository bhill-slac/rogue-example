#include <rogue/ApiWrapper.h>

int main (int argc, char **argv) {

   try {
      rogue::ApiWrapperPtr wrap = rogue::ApiWrapper::local("evalBoard","EvalBoard");

      printf("Return value int = %li\n",wrap->get("evalBoard.AxiVersion.UpTimeCnt"));
      printf("Return value str = %s\n",wrap->getDisp("evalBoard.AxiVersion.UpTimeCnt").c_str());

      Py_BEGIN_ALLOW_THREADS;
      while(1) {
         usleep(10);
      }
      Py_END_ALLOW_THREADS;

   } catch (boost::python::error_already_set) {
      PyErr_Print();
   }
}

