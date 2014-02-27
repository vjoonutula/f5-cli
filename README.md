#CLI interface into F5.
Managing an F5 through the web interface is a bummer. Why not wrap the API in a cli for easier management!

You will need to download the bigsuds soap library from f5.

https://devcentral.f5.com/articles/getting-started-with-bigsuds-ndasha-new-python-library-for-icontrol#.Uw9r0vappBI

F5 should put this on github..... :)

Pull requests welcome!

### Assumptions
Some f5 operations take a 10 seconds to complete.

1. The default node monitoring is ICMP, this monitor should be in /Common/icmp
⋅⋅* Nodes should be created with their FQDN, and should have a valid A record
2. The default pool monitor is HTTP, this monitor should be in /Common/icmp
⋅⋅* Specified nodes should be referenced with their FQDN & should use the same format as they were created above.
3. Virtual servers are assumed to balance HTTP traffic.
4. Virtual servers have the following profiles automatically assigned.
⋅⋅* tcp
⋅⋅* http
⋅⋅* oneconnect

5. Creating a VS with a SSL profile, the CA should be available in the partition.


### Usage example
#### Add some Nodes.
##### list
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land node list

##### Create
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land node create --nodes "web-n01.staging.b.chicken.net, web-n02.staging.b.chicken.net"

##### Delete Node
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land node delete --nodes "web-n01.staging.b.chicken.net, web-n02.staging.b.chicken.net"


#### Pool
##### list
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land pool list

##### Create
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land pool create --nodes "web-n01.staging.b.chicken.net:80, web-n02.staging.b.chicken.net:80" --pool_name "web.staging.b.chicken.net"

##### Delete Pool
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land pool delete --pool_name "web.staging.b.chicken.net"

#### Upload SSL Files
##### list
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_file list

##### Create/import SSL key & Cert
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_file create --name web.staging.b.chicken.net --key sample.key --certificate sample.cert

##### Delete SSL key & Cert
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_file delete --name web.staging.b.chicken.net 



####  SSL profiles
##### list

python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_profile list

##### Create
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_profile create --name web.staging.b.chicken.net --certificate web.staging.b.chicken.net --key web.staging.b.chicken.net


##### Create SSL profile with CA
###### The chain fiile should be uploaded before hand.

python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_profile create --name web.staging.b.chicken.net --certificate web.staging.b.chicken.net --key web.staging.b.chicken.net --chain mackspace_ca

##### Delete
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land ssl_profile delete --name web.staging.b.chicken.net 

#### Virtual servers
##### list
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land virtual_server list

##### Create
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land virtual_server create --vip_name "web.staging.b.chicken.net" --vip_address "10.23.251.55" --port 80 --protocol TCP --pool web.staging.b.chicken.net --type http

##### Create Virtaul server with SSL profile.
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land virtual_server create --vip_name "web.staging.b.chicken.net" --vip_address "10.23.251.55" --port 443 --protocol TCP --pool web.staging.b.chicken.net --ssl_profile web.staging.b.chicken.net --type https

##### Additional profiles to be applied at virtaul server creation.
--snat - Secure network translation, available otpions: automap or none, snat pool not implmeneted.
--protocol_profile - Specified TCP & UDP profile
--http_profile -Specified HTTP profile, defaults to the default http profile.

##### Delete
python f5-cli.py --user user --host f5-1b.dev.b.chicken.net --partition chicken_land virtual_server delete --vip_name "web.staging.b.chicken.net"


######python deps:
dnspython
