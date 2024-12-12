Usage steps:

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

2) run the script as following (you can add as many host/cert as needed, script will update ouptut.json automatically):

**Note:** in case you adding a key instead of cert use "key" argument instead of cert in the above command.

```bash
python3 ./update_grafana_certs.py cert <your-host-nam> <your-cert-file> output.json
```


3) check the output.json has the right content and update the entry on the mon-store by using the following command:

```bash
ceph config-key set mgr/cephadm/cert_store.cert.grafana_cert -i output.json
```
4) make sure the entry has been updated properly by using the following command:
```bash
ceph config-key get mgr/cephadm/cert_store.cert.grafana_cert
```
5) reconfig the corresponding Grafana daemon as following (use ceph orch ps to get the daemon name):
```bash
ceph orch daemon reconfig <your-grafana-daemon>
```


