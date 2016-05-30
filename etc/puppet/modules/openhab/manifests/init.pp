class openhab {

  include apt

  $config_path = '/etc/openhab/configurations/'

  apt::key { 'openhab':
    key_source => 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab',
  }

  apt::source { 'openhab':
    location     => 'http://dl.bintray.com/openhab/apt-repo',
    release      => 'stable',
    repos        => 'main',
    include_src  => false,
  }

  package {
    'openhab-runtime':
      ensure => 'installed';
    'openhab-addon-binding-enocean':
      ensure => 'installed',
      require => Package['openhab-runtime'];
    'openhab-addon-binding-hue':
      ensure => 'installed',
      require => Package['openhab-runtime'];
    'openhab-addon-persistence-mysql':
      ensure => 'installed',
      require => Package['openhab-runtime'];
  }

  File {
    ensure  => 'present',
    require => Package['openhab-runtime'],
  }

  file {
    'openhab.cfg':
      source => 'puppet:///modules/openhab/config',
      target => '${config_path}/openhab.cfg';
    '${config_path}/sitemaps/openhab.sitemap':
      source  => 'puppet:///modules/openhab/sitemap';
    '${config_path}/items/openhab.items':
      source  => 'puppet:///modules/openhab/items';
    '${config_path}/rules/openhab.rules':
      source  => 'puppet:///modules/openhab/rules';
    '${config_path}/transform/openhab.transform':
      source  => 'puppet:///modules/openhab/transform';
    '${config_path}/persistence/openhab.persistence':
      source  => 'puppet:///modules/openhab/persistence';
  }
}