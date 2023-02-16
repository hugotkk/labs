This repo is for learning purpose on ubuntu [autoinstall](https://ubuntu.com/server/docs/install/autoinstall-reference#identity)

# Docker Image

```
docker build -t cloud-init .
```

# password generation

```
docker run -it --rm cloud-init mkpasswd -m sha-512 ubuntu
```

# quickstart script

- Rebuild <seed_iso_path> from user-data
- Remove and create <vdi_path> and attach to the <vm_name>
- Start the <vm_name>

Usage:

```
Usage: ./quickstart <vm_name> <seed_iso_path> <ubuntu_iso_path> <vdi_path>
```

Example:
```
./quickstart ubuntu seed.iso ~/Downloads/ubuntu-22.04.1-live-server-amd64.iso ~/VirtualBox\ VMs/ubuntu/lab102.vdi
```

!(Storage Settings)[https://ibb.co/Tg44pPs]
