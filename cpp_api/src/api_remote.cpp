#include <rogue/ApiWrapper.h>

int main (int argc, char **argv) {
   uint32_t i;

   try {
      rogue::ApiWrapperPtr wrap = rogue::ApiWrapper::remote("apiTest","dummyTree");

      wrap->setUInt32("dummyTree.AxiVersion.ScratchPad",0xCC);
      printf("Spad value int = 0x%x\n",wrap->getUInt32("dummyTree.AxiVersion.ScratchPad"));

      rogue::ApiEntryList lst = wrap->getEntries();

      for (i=0; i < lst.size(); i++) {
         printf("Got path: %s. hidden=%i, typeStr=%s, cmd=%i, arg=%i\n",lst[i]->path.c_str(),lst[i]->hidden,lst[i]->typeStr.c_str(),lst[i]->cmd,lst[i]->cmdArg);
      }
   } catch (boost::python::error_already_set) {
      PyErr_Print();
   }
}

