Usage steps:

## To update certificates:

1) create a file which only contains the cert (or key) content, for example:

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


3) check the output.json has the right content and update the entry on the mon-store by using the following command:
```bash
ceph config-key set mgr/cephadm/cert_store.cert.grafana_cert -i grafana_certs.json
```

4) make sure the entry has been updated properly by using the following command:
```bash
ceph config-key get mgr/cephadm/cert_store.cert.grafana_cert
```

5) reconfig the corresponding Grafana daemon as following (use ceph orch ps to get the daemon name):
```bash
ceph orch daemon reconfig <your-grafana-daemon>
```

## To update corresponding keys:

1) create a file which only contains the cert (or key) content, for example:

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

2) run the script as following (you can add as many host/cert as needed, script will update ouptut.json automatically):

```bash
python3 ./update_grafana_certs.py key <your-host-name> <your-cert-file> grafana_keys.json
```


3) check the output.json has the right content and update the entry on the mon-store by using the following command:
```bash
ceph config-key set mgr/cephadm/cert_store.key.grafana_key -i grafana_keys.json
```

4) make sure the entry has been updated properly by using the following command:
```bash
ceph config-key get mgr/cephadm/cert_store.key.grafana_key
```

5) reconfig the corresponding Grafana daemon as following (use ceph orch ps to get the daemon name):
```bash
ceph orch daemon reconfig <your-grafana-daemon>
```




