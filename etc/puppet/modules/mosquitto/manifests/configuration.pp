class mosquitto::configuration {

  file {
    '/etc/mosquitto/mosquitto.conf ':
      source  => 'puppet:///modules/mosquitto/mosquitto.conf',
      notify  => Service['mosquitto'];
    '/etc/mosquitto/passwd':
      source  => 'puppet:///modules/mosquitto/passwd',
      notify  => Service['mosquitto'];
  }

}
