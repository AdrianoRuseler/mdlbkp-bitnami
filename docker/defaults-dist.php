<?php
$defaults['moodle']['summary'] = 'Moodle Backup Site! '; // for core settings
$defaults['moodle']['custommenuitems'] = 'Theme
-Boost | ?theme=boost
-Classic | ?theme=classic
';
$defaults['moodle']['allowthemechangeonurl'] = 1; 
$defaults['moodle']['timezone'] = 'America/Sao_Paulo';
$defaults['moodle']['defaultcity'] = 'Curitiba';
$defaults['moodle']['country'] = 'Brazil';

$defaults['moodle']['pathtophp'] = '/opt/bitnami/php/bin/php';
$defaults['moodle']['pathtodu'] = '/usr/bin/du';
$defaults['moodle']['aspellpath'] = '/usr/bin/aspell';
$defaults['moodle']['pathtogs'] = '/usr/bin/gs';
$defaults['moodle']['pathtodot'] = '/usr/bin/dot';
$defaults['moodle']['pathtopdftoppm'] = '/usr/bin/pdftoppm';
$defaults['moodle']['pathtopython'] = '/usr/bin/python3';

$defaults['moodle']['forcelogin'] = 1;
$defaults['moodle']['enablewebservices'] = 1;
$defaults['moodle']['enablewsdocumentation'] = 1;
$defaults['moodle']['webserviceprotocols'] = 'rest';

# https://docs.stack-assessment.org/en/Installation/
$defaults['qtype_stack']['platform'] = 'Server';
$defaults['qtype_stack']['maximaversion'] = '5.44.0';
$defaults['qtype_stack']['maximacommandserver'] = 'http://host.docker.internal:8081/goemaxima';

# https://coderunner.org.nz/
# https://github.com/trampgeek/jobeinabox
$defaults['qtype_coderunner']['jobe_host'] = 'host.docker.internal:4000';
# docker exec -t mdlbkp-450-jobe-1 /usr/bin/python3 /var/www/html/jobe/testsubmit.py

# https://vpl.dis.ulpgc.es/index.php/en/
$defaults['mod_vpl']['jail_servers'] = 'http://host.docker.internal:8000/vpl';
