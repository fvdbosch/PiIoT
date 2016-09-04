class clock {
  file {
    '/home/pi/clock.py':
      content => 'puppet:///modules/clock/clock.py';
  }

  cron { 
    'clock':
      command => "/home/pi/clock.py &",
      user => "pi",
      special => "reboot",
  }
}
