class openhab::configuration (
  $version        = 2,
  $security       = 'OFF',
  $enocean        = false,
  $enocean_serial = '/dev/ttyS0',
  $persistence    = false,
  $db_name        = 'openhab',
  $db_user        = 'openhab',
  $db_pass        = 'openhab',
) {

  # Bindings
  if $enocean == true {
    package {
      'openhab-addon-binding-enocean':
        ensure => 'installed',
        require => Package['openhab-runtime'];
    }
  }

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
  }

  file {
    '/etc/openhab/configurations/openhab.cfg':
      content => template('openhab/openhab.cfg.erb');
    '/etc/openhab/configurations/sitemaps/openhab.sitemap':
      source  => 'puppet:///modules/openhab/openhab.sitemap';
    '/etc/openhab/configurations/items/openhab.items':
      source  => 'puppet:///modules/openhab/openhab.items';
    '/etc/openhab/configurations/rules/openhab.rules':
      source  => 'puppet:///modules/openhab/openhab.rules';
    '/etc/openhab/configurations/transform/openhab.map':
      source  => 'puppet:///modules/openhab/openhab.map';
  }

}
