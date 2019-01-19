#include <rogue/RogueSMemFunctions.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main (int argc, char **argv) {

   RogueControlMem *smem;
   char res [1024];

   if ( rogueSMemControlOpenAndMap(&smem,"smemTest") < 0 ) {
      printf("Failed to open shared memory\n");
      return(0);
   }

   rogueSMemControlReq(smem,ROGUE_CMD_SET,"dummyTree.AxiVersion.ScratchPad","0x55");

   while ( rogueSMemControlAckCheck(smem,res) == 0 ) { usleep(100); }

   rogueSMemControlReq(smem,ROGUE_CMD_GET,"dummyTree.AxiVersion.ScratchPad","");

   while ( rogueSMemControlAckCheck(smem,res) == 0 ) { usleep(100); }

   printf("Got %s\n",res);
}


