class clock {
  file {
    '/home/pi/clock.py':
      content => 'puppet:///modules/clock/clock.py';
  }
}
