class mosquitto {

  include mosquitto::configuration

  package { 'mosquitto':
    ensure  => 'installed',
  } ~>

  service { 'mosquitto':
    ensure => 'running',
    enable => true,
  }
}
