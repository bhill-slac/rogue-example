#include <rogue/ApiWrapper.h>

int main (int argc, char **argv) {

   try {
      rogue::ApiWrapperPtr wrap = rogue::ApiWrapper::local("evalBoard","EvalBoard");

      printf("Return value int = %li\n",wrap->getUInt32("evalBoard.AxiVersion.UpTimeCnt"));
      printf("Return value str = %s\n",wrap->getString("evalBoard.AxiVersion.UpTimeCnt").c_str());

      wrap->setUInt32("evalBoard.AxiVersion.ScratchPad",0xCC);
      printf("Spad value int = 0x%x\n",wrap->getUInt32("evalBoard.AxiVersion.ScratchPad"));

      rogue::ApiEntryList lst = wrap->getEntries();

      for (i=0; i < lst.size(); i++) {
         printf("Got path: %s. hidden=%i, typeStr=%s, cmd=%i, arg=%i\n",lst[i]->path.c_str(),lst[i]->hidden,lst[i]->typeStr.c_str(),lst[i]->cmd,lst[i]->cmdArg);
      }

      Py_BEGIN_ALLOW_THREADS;
      while(1) {
         usleep(10);
      }
      Py_END_ALLOW_THREADS;

   } catch (boost::python::error_already_set) {
      PyErr_Print();
   }
}

