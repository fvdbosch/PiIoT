class base::camera {
  exec {
    'enable_camera':
      command => "/usr/bin/perl -p -i -e 's|^start_x=0|start_x=1|' /boot/config.txt",
      onlyif  => '/bin/grep "^start_x=0$" /boot/config.txt';
  }
}
