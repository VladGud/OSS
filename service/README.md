# Service check permission each 1 minute

## Manuals for demonstration

### Create a rpm package 
1. `rpmdev-setuptree`
2. `cd ~/rpmbuild/SOURCES`
3. `mkdir check_control-1.0`
4. `cp {service-directory}/src/* ./check_control-1.0`
5. `tar -cvzf check_control-1.0.tar.gz check_control-1.0`
6. `cp {service-directory}/selinux/* ./`
7. `cd ../SPECS`
8. `cp {service-directory}/rpm/check_control.spec ./`
9. `rpmbuild -ba check_control.spec`

### Create key for sign

1. `gpg2 --gen-key`
2. `gpg2 --export -a Sapegin > ~/rpmbuild/RPM-GPG-KEY-Sapegin`

### Sign package
1. In `~/.rpmmacros` add line `%_gpg_name {name}`
2. `rpm --addsign ~/rpmbuild/RPMS/noarch/check_control-1.0-1.el7.noarch.rpm`

### Create repository

1. `sudo mkdir -p /var/www/html/mephi_project`
2. `sudo cp ~/rpmbuild/RPMS/noarch/check_control-1.0-1.el7.noarch.rpm /var/www/html/mephi_project`
3. `sudo cp ~/rpmbuild/RPM-GPG-KEY-Sapegin /var/www/html/mephi_project`
4. `sudo createrepo -v /var/www/html/mephi_project`
5. `sudo cp repo/mephi_project.repo /etc/yum.repos.d/`

### Install from repository package
1. `sudo systemctl enable httpd.service`
2. `sudo systemctl start httpd.service`
3. `sudo yum install check_control`

### Start a serivce and test it

1. `systemctl start check_control`
2. `systemctl status check_control`
3. `chmod +x test_check_control.sh`
4. `./test_check_control.sh`
