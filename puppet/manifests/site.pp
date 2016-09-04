node 'pictrl_bedroom' {
  include base
  include adafruit
  include clock
}

node 'pictrl_livingroom' {
  include base
  include adafruit
  include clock
  include keypad
  include openhab2
  include mosquitto
}

node 'picam_shed', 'picam_lab' {
  include base::network
  include base::camera
}

node 'emonpi' {
  include base::network
}

node 'keyholder' {
  include base::network
}