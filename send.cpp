/*
 * Usage: ./send <systemCode> <unitCode> <command>
 * Command is 0 for OFF and 1 for ON
 */

#include "RCSwitch.h"
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {

  /*
   * output PIN is hardcoded for testing purposes
   * see https://projects.drogon.net/raspberry-pi/wiringpi/pins/
   * for pin mapping of the raspberry pi GPIO connector
   */
  int PIN = 0;
  string unitcode = argv[1];
  string state  = argv[2];

  if (wiringPiSetup () == -1) return 1;
  piHiPri(20);
  /* printf("sending unitcode[%i] state[%i]\n", unitcode, state); */
  RCSwitch mySwitch = RCSwitch();
  mySwitch.setPulseLength(300);
  mySwitch.enableTransmit(PIN);
  
  std::cout<< "unitcode: " << unitcode << std::endl;
  std::cout<< "Laenge: " << unitcode.length() << std::endl;

  string::size_type pos = 0;
  
while ((pos = unitcode.find("1", pos)) != string::npos) {
   string s2 = "x";
  unitcode.replace(pos, 1, s2, 0, s2.length());
}
std::cout<< "spos  " << pos << std::endl;
std::cout<< "find  " << unitcode.find("0", pos) << std::endl;
pos=0;
while ((pos = unitcode.find("0", pos)) != string::npos) {
   string s1 = "1";
  unitcode.replace(pos, 1, s1, 0, s1.length());
}
pos=0;
while ((pos = unitcode.find("x", pos)) != string::npos) {
   string s2 = "0";
  unitcode.replace(pos, 1, s2, 0, s2.length());
}  
  string execute = unitcode + state;
  
  std::cout<< "seeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: " << execute << std::endl;
  string exe = execute;
  for(int i=0;i < 24;i+=2){
	
	execute = exe.insert(i, 1, '0');
  }

  char * buffer = new char[execute.length()];
  char *kacka=strcpy(buffer,execute.c_str());
    
  //char *array="000000000001000000000000";
  mySwitch.send(kacka);  
				
  std::cout<< "state: " << state << std::endl;
  std::cout<< "execute: " << execute << std::endl;
  return 0;
}
