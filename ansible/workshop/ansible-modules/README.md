```bash=
$ sudo dpkg -l | grep nginx
rc  libnginx-mod-http-image-filter        1.18.0-0ubuntu1.4                 amd64        HTTP image filter module for Nginx
rc  libnginx-mod-http-xslt-filter         1.18.0-0ubuntu1.4                 amd64        XSLT Transformation module for Nginx
rc  libnginx-mod-mail                     1.18.0-0ubuntu1.4                 amd64        Mail module for Nginx
rc  libnginx-mod-stream                   1.18.0-0ubuntu1.4                 amd64        Stream module for Nginx
rc  nginx-common                          1.18.0-0ubuntu1.4                 all          small, powerful, scalable web/proxy server - common files
$ ansible-playbook install.yml 
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [hello world playbook] ******************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************
ok: [localhost]

TASK [ssh connect] ***************************************************************************************************************************************************************************
changed: [localhost]

TASK [install nginx] *************************************************************************************************************************************************************************
changed: [localhost]

TASK [service start] *************************************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP ***********************************************************************************************************************************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

$ sudo dpkg -l | grep nginx
ii  libnginx-mod-http-image-filter        1.18.0-0ubuntu1.4                 amd64        HTTP image filter module for Nginx
ii  libnginx-mod-http-xslt-filter         1.18.0-0ubuntu1.4                 amd64        XSLT Transformation module for Nginx
ii  libnginx-mod-mail                     1.18.0-0ubuntu1.4                 amd64        Mail module for Nginx
ii  libnginx-mod-stream                   1.18.0-0ubuntu1.4                 amd64        Stream module for Nginx
ii  nginx                                 1.18.0-0ubuntu1.4                 all          small, powerful, scalable web/proxy server
ii  nginx-common                          1.18.0-0ubuntu1.4                 all          small, powerful, scalable web/proxy server - common files
ii  nginx-core                            1.18.0-0ubuntu1.4                 amd64        nginx web/proxy server (standard version)
$ ansible-playbook uninstall.yml 
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [hello world playbook] ******************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************
ok: [localhost]

TASK [ssh connect] ***************************************************************************************************************************************************************************
changed: [localhost]

TASK [stop start] ****************************************************************************************************************************************************************************
changed: [localhost]

TASK [ubinstall nginx] ***********************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP ***********************************************************************************************************************************************************************************
localhost                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

$ sudo dpkg -l | grep nginx
rc  libnginx-mod-http-image-filter        1.18.0-0ubuntu1.4                 amd64        HTTP image filter module for Nginx
rc  libnginx-mod-http-xslt-filter         1.18.0-0ubuntu1.4                 amd64        XSLT Transformation module for Nginx
rc  libnginx-mod-mail                     1.18.0-0ubuntu1.4                 amd64        Mail module for Nginx
rc  libnginx-mod-stream                   1.18.0-0ubuntu1.4                 amd64        Stream module for Nginx
rc  nginx-common                          1.18.0-0ubuntu1.4                 all          small, powerful, scalable web/proxy server - common files
```
