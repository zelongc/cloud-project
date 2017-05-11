

# upload config files local.ini  vm.args   

# download sys.config
scp -i ~/dropbox/keystore/cloud.key ubuntu@130.56.249.225:/home/ubuntu/apache-couchdb-2.0.0/rel/couchdb/releases/2.0.0/sys.config ~/dropbox/ansible/config_file_for_couchdb/sys.config

#download local.ini
scp -i ~/dropbox/keystore/cloud.key ubuntu@130.56.249.225:/home/ubuntu/apache-couchdb-2.0.0/rel/couchdb/etc/local.ini ~/dropbox/ansible/config_file_for_couchdb/local.ini

#download vm.args
scp -i ~/dropbox/keystore/cloud.key ubuntu@130.56.249.225:/home/ubuntu/apache-couchdb-2.0.0/rel/couchdb/etc/vm.args ~/dropbox/ansible/config_file_for_couchdb/vm.args
