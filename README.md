The _**update_grafana_certs.py**_ script is designed to help manage SSL/TLS certificates and keys for Grafana. When run for the first time, the script creates a new JSON file to store the certificates or keys. If the file already exists, the script seamlessly updates its content, ensuring that the data stays up-to-date without overwriting existing configurations.

Before proceeding, please make sure you have your Grafana certificate and key pair.

Usage steps:

## 1) Update Grafana certificate(s):

1) create a file which only contains the certificate content, for example:

```bash
-----BEGIN CERTIFICATE-----
MIIFCDCCAvCgAwIBAgIUcttQRwsQ3MialkNhMsB61uegdC8wDQYJKoZIhvcNAQEL
BQAwFzEVMBMGA1UEAwwMY2VwaGFkbS1yb290MB4XDTI0MTIxMjA3MjU0M1oXDTM0
MTIxMzA3MjU0M1owGjEYMBYGA1UEAwwPMTkyLjE2OC4xMDAuMTAxMIICIjANBgkq
......
......
13dN3wVQEw9y/8jTphPhnvjphNSOlcS49/78n23X2ayjESoZucSsj1mYHcg=
-----END CERTIFICATE-----
```

2) run the script as following (you can add as many host/cert as needed, script will update grafana_certs.json automatically):

```bash
python3 ./update_grafana_certs.py cert <your-host-name> <your-cert-file> grafana_certs.json
```


3) check the grafana_certs.json has the right content and update the entry on the mon-store by using the following command:
```bash
ceph config-key set mgr/cephadm/cert_store.cert.grafana_cert -i grafana_certs.json
```

4) make sure the entry has been updated properly by using the following command:
```bash
ceph config-key get mgr/cephadm/cert_store.cert.grafana_cert
```

## 2) Update Grafana key(s):

1) create a file which only contains the key content, for example:

```bash
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEA0j41QbO0emj3QLfJI4Pl8cc1YcJurs4tuYVDGnBKchDjaVOC
ACC86mTRTGZ2l4mWFQE/o1Iktr5IJx9Ox6grX+756rrzWQmZhOs7039oHjX0AZNo
59NAxx02pnO+zLqdxBatEckMBWXaQwySavcCOQgGWGazFMiNZxLrGoZGO5c+zBQz
DJ5/P6cx3hkiXK4/gMwQzsMnqzaU8HPxkdhgP4ui38KPcxgYsG1RP++ZlpKCy9/2
......
......
13dN3wVQEw9y/8jTphPhnvjphNSOlcS49/78n23X2ayjESoZucSsj1mYHcg=
-----END RSA PRIVATE KEY-----
```

2) run the script as following (you can add as many host/key as needed, script will update ouptut.json automatically):

```bash
python3 ./update_grafana_certs.py key <your-host-name> <your-cert-file> grafana_keys.json
```


3) check the grafana_keys.json has the right content and update the entry on the mon-store by using the following command:
```bash
ceph config-key set mgr/cephadm/cert_store.key.grafana_key -i grafana_keys.json
```

4) make sure the entry has been updated properly by using the following command:
```bash
ceph config-key get mgr/cephadm/cert_store.key.grafana_key
```
## 4) Force cephadm cert-store to load the new content:
```bash
ceph mgr fail
```

## 3) Reconfigure Grafana daemon:

5) Once the mgr has finish the failover, reconfig the corresponding Grafana daemon as following (use ceph orch ps to get the daemon name):
```bash
ceph orch daemon reconfig <your-grafana-daemon>
```

you can also run the following to reconfigure all the daemons at once:
```bash
ceph orch reconfig grafana
```






