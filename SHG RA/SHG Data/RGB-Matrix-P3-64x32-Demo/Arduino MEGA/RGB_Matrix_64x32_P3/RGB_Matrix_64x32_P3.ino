#include "RGBmatrixPanel.h"
#include "bit_bmp.h"
#include "fonts.h"
#include <string.h>
#include <stdlib.h>
#define CLK 11 
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false, 64);

void setup()
{
  Serial.begin(115200);
  Reginit();
  matrix.begin();
  delay(500);
}

void loop()
{
  Demo_1();
}

void display_text(int x, int y, char *str, const GFXfont *f, int color, int pixels_size)
{
  matrix.setTextSize(pixels_size);// size 1 == 8 pixels high
  matrix.setTextWrap(false); // Don't wrap at end of line - will do ourselves
  matrix.setFont(f);      //set font
  matrix.setCursor(x, y);
  matrix.setTextColor(color);
  matrix.println(str);
}

void Demo_1()
{
  display_text(1, 13, "text", NULL, matrix.Color333(0, 100, 255), 2); // this text need to be printed slightly larger and over the 2 displays, not duplicated.
}
void Reginit()
{
    pinMode(24, OUTPUT); //R1
    pinMode(25, OUTPUT); //G1
    pinMode(26, OUTPUT); //B1
    pinMode(27, OUTPUT); //R2
    pinMode(28, OUTPUT); //G2
    pinMode(29, OUTPUT); //B2
    pinMode(CLK, OUTPUT);
    pinMode(OE, OUTPUT);
    pinMode(LAT, OUTPUT);

    digitalWrite(OE, HIGH);
    digitalWrite(LAT, LOW);
    digitalWrite(CLK, LOW);
    int MaxLed = 64;

    int C12[16] = {0, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1};
    int C13[16] = {0, 0, 0, 0, 0,  0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0};

    for (int l = 0; l < MaxLed; l++)
    {
        int y = l % 16;
        digitalWrite(24, LOW);
        digitalWrite(25, LOW);
        digitalWrite(26, LOW);
        digitalWrite(27, LOW);
        digitalWrite(28, LOW);
        digitalWrite(29, LOW);
        if (C12[y] == 1)
        {
          digitalWrite(24, HIGH);
          digitalWrite(25, HIGH);
          digitalWrite(26, HIGH);
          digitalWrite(27, HIGH);
          digitalWrite(28, HIGH);
          digitalWrite(29, HIGH);
        }
        if (l > MaxLed - 12)
        {
            digitalWrite(LAT, HIGH);
        }
        else
        {
            digitalWrite(LAT, LOW);
        }
        digitalWrite(CLK, HIGH);
        delayMicroseconds(2);
        digitalWrite(CLK, LOW);
    }
    digitalWrite(LAT, LOW);
    digitalWrite(CLK, LOW);

    // Send Data to control register 12
    for (int l = 0; l < MaxLed; l++)
    {
        int y = l % 16;
        digitalWrite(24, LOW);
        digitalWrite(25, LOW);
        digitalWrite(26, LOW);
        digitalWrite(27, LOW);
        digitalWrite(28, LOW);
        digitalWrite(29, LOW);
        if (C13[y] == 1)
        {
            digitalWrite(24, HIGH);
            digitalWrite(25, HIGH);
            digitalWrite(26, HIGH);
            digitalWrite(27, HIGH);
            digitalWrite(28, HIGH);
            digitalWrite(29, HIGH);
        }
        if (l > MaxLed - 13)
        {
            digitalWrite(LAT, HIGH);
        }
        else
        {
            digitalWrite(LAT, LOW);
        }
        digitalWrite(CLK, HIGH);
        delayMicroseconds(2);
        digitalWrite(CLK, LOW);
    }
    digitalWrite(LAT, LOW);
    digitalWrite(CLK, LOW);
}
