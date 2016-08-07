#include "application.h"
#include "neopixel/neopixel.h"
#include "MQTT/MQTT.h"

SYSTEM_MODE(AUTOMATIC);

// IMPORTANT: Set pixel COUNT, PIN and TYPE
#define PIXEL_PIN D2
#define PIXEL_COUNT 12
#define PIXEL_TYPE WS2812B

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, PIXEL_TYPE);

MQTT client("192.168.0.212", 1883, callback);

int animation = 0;

void setup()
{
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  
  Particle.subscribe("animation", myHandler);

  while (!client.isConnected()) {
    client.connect("towerlight", "piiot", "piiot"); // connect to the server
    client.subscribe("TowerLight");
    delay(1000);
  }

}
void loop()
{
  if (client.isConnected()) {
    client.loop();
  } else {
    client.connect("towerlight", "piiot", "piiot");
    client.subscribe("TowerLight");
  }
        
  if(animation == 1) {
    siren(50);
  }
  else if(animation == 2) {
    pulse(10);
  }
  else if(animation == 3) {
    blink(500);
  }
  else if(animation == 4) {
    fill();
  }
  else {
    clear();
  }
}

void myHandler(const char *event, const char *data) {
    animation = atoi(data);
}

void siren(uint8_t wait) {
  uint16_t i, j;

  for(i=0; i<6; i++) {
    for(j=0; j<12; j++) {
        strip.setPixelColor(j, strip.Color(0, 0, 0));
    }
    
    strip.setPixelColor(i, strip.Color(255, 0, 0));
    strip.setPixelColor(i+1, strip.Color(255, 0, 0));
    strip.setPixelColor(i+2, strip.Color(255, 0, 0));
    
    strip.setPixelColor(i+6, strip.Color(255, 0, 0));
    strip.setPixelColor(i+7, strip.Color(255, 0, 0));
    strip.setPixelColor(i+8, strip.Color(255, 0, 0));
    
    strip.show();
    delay(wait);
  }  
}

void fill() {
  uint16_t i;

  for(i=0; i<12; i++) {
    strip.setPixelColor(i, strip.Color(255, 0, 0));
  }  
    strip.show();
}

void clear() {
  uint16_t i;

  for(i=0; i<12; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 0));
  }  
    strip.show();
}

void pulse(uint8_t wait) {
  uint16_t i, j;
  for(j=0; j<256; j++) {
    for(i=0; i<12; i++) {
      strip.setPixelColor(i, strip.Color(j, 0, 0));
    }  
    strip.show();
    delay(wait);
  }
  for(j=255; j>0; j--) {
    for(i=0; i<12; i++) {
      strip.setPixelColor(i, strip.Color(j, 0, 0));
    }  
    strip.show();
    delay(wait);
  }
}

void blink(uint16_t wait) {
  uint16_t i;
  
  for(i=0; i<12; i++) {
    strip.setPixelColor(i, strip.Color(0, 0, 0));
  }  
  strip.show();
  delay(wait);
  
  for(i=0; i<12; i++) {
    strip.setPixelColor(i, strip.Color(255, 0, 0));
  }  
  strip.show();
  delay(wait);
}

void callback(char* intopic, byte* payload, unsigned int length) {
  char p[length + 1];
  memcpy(p, payload, length);
  p[length] = NULL;
  String message(p);
  
  animation = atoi(message);
}