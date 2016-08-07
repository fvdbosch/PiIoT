class openhab2::enocean (
  $enocean_interface = "/dev/ttyS0",
) {
  file {
    '/etc/openhab2/services/enocean.cfg':
      content => template('openhab2/enocean.cfg.erb'),
      notify  => Service['openhab2'];
  }
}
