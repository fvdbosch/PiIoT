class adafruit::led_backpack {

  exec {
    'download library':
      command => "git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack /home/pi/",
      onlyif  => 'test ! -d "/home/pi/Adafruit_Python_LED_Backpack"';
  }

  exec {
    'install library':
      command  => "sudo python /home/pi/Adafruit_Python_LED_Backpack/setup.py install",
      requires => File['/home/pi/Adafruit_Python_LED_Backpack/setup.py'];
  }

}
