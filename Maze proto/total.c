#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

#include <wiringPi.h>
#include <wiringPiSPI.h>

#define CS_MCP 8

#define echo 19
#define trig 13

#define SPI_CHANNEL 0
#define SPI_SPEED 1000000

int read_mcp3208_adc(unsigned char adcChannel)
{
	unsigned char buff[3];
	int adcValue = 0;

	buff[0] = 0x06|((adcChannel&0x07) >> 2);
	buff[1] = ((adcChannel & 0x07) << 6);
	buff[2] = 0x00;

	digitalWrite(CS_MCP,0);

	wiringPiSPIDataRW(SPI_CHANNEL,buff,3);

	buff[1] = 0x0f &buff[1];
	adcValue = (buff[1]<<8)|buff[2];

	digitalWrite(CS_MCP,1);
	//adcValue = (float)(adcValue*3.3)/1024;
	return adcValue;
}

float cho(){
	time_t start_time, end_time;
	float distance;
	digitalWrite(trig,LOW);
	delay(500);
	digitalWrite(trig,HIGH);
	delayMicroseconds(10) ;

    digitalWrite(trig, LOW) ;

    while (digitalRead(echo) == 0) ;

    start_time = clock() ;

    while (digitalRead(echo) == 1) ;

    end_time = clock() ;

    distance = (end_time - start_time)/(CLOCKS_PERSEC)*17000;

    return distance;
}

int main(int argc, char const *argv[])
{
	int adcChannel = 1;
	int resi = 0;
	int adcValue = 0;
	int resivalue = 0;
	float choum = 0;

	if(wiringPiSetupGpio() == -1)
	{
		fprintf(stdout, "Unable : %s\n", strerror(errno));
		return 1;
	}

	if(wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED)==-1)
	{
		fprintf(stdout, "%s\n", strerror(errno));
		return 1;
	}

	pinMode(CS_MCP,OUTPUT);
	pinMode(trig,OUTPUT);
	pinMode(echo,INPUT);


	while(1)
	{
		adcValue = read_mcp3208_adc(adcChannel);
		printf("watervalue = %u\n",adcValue);
		resivalue = read_mcp3208_adc(resi);
		printf("resivalue = %u\n",resivalue);
		choum=cho();
		printf("distance %.2f cm\n", choum);
		sleep(1);
	}
	return 0;
}
