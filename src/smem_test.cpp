#include <rogue/RogueSMemFunctions.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main (int argc, char **argv) {

   RogueControlMem *smem;
   char res [100];

   if ( rogueSMemControlOpenAndMap(&smem,"rogueTest") < 0 ) {
      printf("Failed to open shared memory\n");
      return(0);
   }

   rogueSMemControlReq(smem,ROGUE_CMD_GET,"evalBoard.AxiVersion.UpTimeCnt","");

   while ( rogueSMemControlAckCheck(smem,res) == 0 ) {
      usleep(100);
   }
   printf("Got %s\n",res);
}


