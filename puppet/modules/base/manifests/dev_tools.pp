class base::dev_tools {
  package { 
    'build-essential':
      ensure  => 'installed';
    'git':
      ensure  => 'installed';
    'python-dev':
      ensure  => 'installed';
    'python-smbus':
      ensure  => 'installed';
    'python-imaging':
      ensure  => 'installed';
  }
}
