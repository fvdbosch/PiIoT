class keypad {
  file {
    '/home/pi/keypad.py':
      content => 'puppet:///modules/keypad/keypad.py';
  }

  cron { 
    'keypad':
      command => "/home/pi/keypad.py &",
      user => "pi",
      special => "reboot",
  }
}
