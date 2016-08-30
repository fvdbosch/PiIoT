class base::network (
  $ssid = '',
  $psk  = '',
){
  file {
    '/etc/wpa_supplicant/wpa_supplicant.conf':
      content => template('base/wpa_supplicant.conf.erb'),
      notify  => Service['networking'];
  }
}
