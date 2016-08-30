class base::i2c {
  package { 'i2c-tools':
    ensure  => 'installed',
  }

  exec {
    'enable_i2c':
      command => "/usr/bin/perl -p -i -e 's|^dtparam=i2c_arm=off|dtparam=i2c_arm=on|' /boot/config.txt",
      onlyif  => '/bin/grep "^dtparam=i2c_arm=off$" /boot/config.txt';
  }
}
