class openhab2::mqtt (
  $broker1_name = "emonpi",
  $broker1_url  = "tcp://192.168.0.155:1883",
  $broker1_user = "emonpi",
  $broker1_password = "emonpimqtt2016",
  $broker1_qos = "2",
  $broker1_retain = "false",
  $broker2_name = "piiot",
  $broker2_url  = "tcp://127.0.0.1:1883",
  $broker2_user = "piiot",
  $broker2_password = "piiot",
  $broker2_qos = "2",
  $broker2_retain = "false",
) {
  file {
    '/etc/openhab2/services/mqtt.cfg':
      content => template('openhab2/mqtt.cfg.erb'),
      notify  => Service['openhab2'];
  }
}
