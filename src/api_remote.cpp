#include <rogue/ApiWrapper.h>

int main (int argc, char **argv) {

   try {
      rogue::ApiWrapperPtr wrap = rogue::ApiWrapper::remote("rogueTest","evalBoard");

      printf("Return value int = %li\n",wrap->get("evalBoard.AxiVersion.UpTimeCnt"));
      printf("Return value str = %s\n",wrap->getDisp("evalBoard.AxiVersion.UpTimeCnt").c_str());

   } catch (boost::python::error_already_set) {
      PyErr_Print();
   }
}

