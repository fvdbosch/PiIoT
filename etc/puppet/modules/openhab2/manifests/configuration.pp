class openhab2::configuration (
  $security       = 'OFF',
  $enocean        = true,
  $enocean_serial = '/dev/ttyS0',
  $persistence    = false,
  $db_name        = 'openhab',
  $db_user        = 'openhab',
  $db_pass        = 'openhab',
) {

  # Persistence
  if $persistence == true {
    class { '::mysql::server':
      root_password           => 'strongpassword',
      remove_default_accounts => true,
      override_options        => {
        'mysqld' => {
          'max_connections' => '1024',
        },
      },
    } ->

    mysql::db { $db_name:
      user     => $db_user,
      password => $db_pass,
      host     => 'localhost',
      grant    => [ALL],
    } ->

    package {
      'openhab-addon-persistence-mysql':
        ensure => 'installed',
        require => Package['mysql-server', 'openhab-runtime'];
    } ->

    file {
      '/etc/openhab/configurations/persistence/mysql.persist':
      source  => 'puppet:///modules/openhab/openhab.persist';
    }    
  }

  File {
    ensure  => 'present',
    require => Package['openhab2-offline'],
  }

  file {
    '/etc/openhab2/openhab.cfg':
      content => template('openhab2/openhab.cfg.erb'),
      notify  => Service['openhab2'];
    '/etc/default/openhab2':
      content => template('openhab2/openhab2.erb'),
      notify  => Service['openhab2'];
    '/etc/openhab2/sitemaps/openhab.sitemap':
      source  => 'puppet:///modules/openhab2/openhab.sitemap';
    '/etc/openhab2/items/openhab.items':
      source  => 'puppet:///modules/openhab2/openhab.items';
    '/etc/openhab2/rules/openhab.rules':
      source  => 'puppet:///modules/openhab2/openhab.rules';
    '/etc/openhab2/transform/openhab.map':
      source  => 'puppet:///modules/openhab2/openhab.map';
  }

}
