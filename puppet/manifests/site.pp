node default {
  include base
  include openhab2
  include mosquitto
}

node piclock {
  include adafruit
  include clock
}
