# Ansible vault example

With `ansible-vault` variables and files can be encrypted to avoid having cleartext sensitive content exposed in ansible files like playbooks, inventory files, etc.

In this first example, the `strgen.sh` script uses ansible-vault to encrypt the `ansible_password` variable defined in the `hosts` inventory file that holds the switches password that ansible uses to connect to the switches.

Before using vault the relevant section of the `hosts` inventory file regarding ansible_ variables does look like this:

```
  vars:
    ansible_network_os: eos
    ansible_connection: network_cli
    ansible_become: yes
    ansible_become_method: enable
    ansible_user: admin
    ansible_password: abc123
```

Now we use our `strgen.sh` script that uses ànsible-vault`

```
# ./strgen.sh
secret name:ansible_password
what to encrypt:
New Vault password: 
Confirm New Vault password: 
Reading plaintext input from stdin. (ctrl-d to end input, twice if your content does not already have a newline)

ansible_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          33313733633230653565383133663332666236336137383865383266353235623066643365353234
          3933396635373966376335613264633630666663326130660a353434356164636566663637656535
          65323363643964336538306133373765323930646338656361313130623832626263306263633563
          3165353539333135310a386564333639633539653338363932626537313737666634613633386263
          6433
Encryption successful
```

The vault password (`.MyPaSsPhRaSe01`) is the passphrase used just to encrypt the original switch password (`abc123` in the example). Note that `.MyPaSsPhRaSe01` is not relevant in the switch at all, that is, the switch admin's user password is `abc123` and *not* `.MyPaSsPhRaSe01`.

So now, the hosts file regarding ansible_ variables looks like this after we edit the file to include the new *encrypted* `ansible_password` variable:

```
     ansible_network_os: eos
     ansible_connection: network_cli
     ansible_become: yes 
     ansible_become_method: enable
     ansible_user: admin
     ansible_password: !vault |
           $ANSIBLE_VAULT;1.1;AES256
           33313733633230653565383133663332666236336137383865383266353235623066643365353234
           3933396635373966376335613264633630666663326130660a353434356164636566663637656535
           65323363643964336538306133373765323930646338656361313130623832626263306263633563
           3165353539333135310a386564333639633539653338363932626537313737666634613633386263
           6433
```

Now if we try to just run the playbook like before, it fails because it has an encrypted variable and, to decrypt it, the passphare should be entered.

```
# ansible-playbook eos_shver.yml 

PLAY [all] ****************************************************************************************************************

TASK [get eos version and hostname] ***************************************************************************************
fatal: [10.34.0.101]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.102]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.11]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.12]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.21]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.22]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.31]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}
fatal: [10.34.0.32]: FAILED! => {"msg": "Attempting to decrypt but no vault secrets found"}

PLAY RECAP ****************************************************************************************************************
10.34.0.101                : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
```

To make ansible ask for the passphase in the command-line `--ask-vault-pass` should be used. And then there you enter your passphrase (`.MyPaSsPhRaSe01`) in this example.

```
# ansible-playbook --ask-vault-pass eos_shver.yml 
Vault password: 

PLAY [all] ****************************************************************************************************************

TASK [get eos version and hostname] ***************************************************************************************
ok: [10.34.0.21]
ok: [10.34.0.11]
ok: [10.34.0.101]
ok: [10.34.0.12]
ok: [10.34.0.102]
ok: [10.34.0.31]
ok: [10.34.0.22]
ok: [10.34.0.32]

TASK [debugs] *************************************************************************************************************
ok: [10.34.0.102] => {
    "msg": "Switch vlab02 runs EOS version 4.22.3M"
}
ok: [10.34.0.21] => {
    "msg": "Switch vlab21 runs EOS version 4.24.0F"
}
ok: [10.34.0.101] => {
    "msg": "Switch vlab01 runs EOS version 4.22.3M"
}
ok: [10.34.0.12] => {
    "msg": "Switch vlab12 runs EOS version 4.24.0F"
}
ok: [10.34.0.11] => {
    "msg": "Switch vlab11 runs EOS version 4.24.0F"
}
ok: [10.34.0.32] => {
    "msg": "Switch vlab32 runs EOS version 4.24.0F"
}
ok: [10.34.0.31] => {
    "msg": "Switch vlab31 runs EOS version 4.24.0F"
}
ok: [10.34.0.22] => {
    "msg": "Switch vlab22 runs EOS version 4.24.0F"
}

PLAY RECAP ****************************************************************************************************************
10.34.0.101                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --ask-vault-pass eos_shver.yml  11.57s user 2.43s system 60% cpu 23.213 total
```

Alternatively, the passphrase could be also in a file (so in that case Ansible does not ask the user for the passphase). Note that that file could be a plain-text file (like in the following example) or an *executable* file (for instance to use an HSM, TPM, etc).

```
# cat pf.txt 
.MyPaSsPhRaSe01

# ansible-playbook --vault-password-file=pf.txt eos_shver.yml

PLAY [all] ****************************************************************************************************************

TASK [get eos version and hostname] ***************************************************************************************
ok: [10.34.0.12]
ok: [10.34.0.102]
ok: [10.34.0.101]
ok: [10.34.0.11]
ok: [10.34.0.21]
ok: [10.34.0.22]
ok: [10.34.0.32]
ok: [10.34.0.31]

TASK [debugs] *************************************************************************************************************
ok: [10.34.0.12] => {
    "msg": "Switch vlab12 runs EOS version 4.24.0F"
}
ok: [10.34.0.101] => {
    "msg": "Switch vlab01 runs EOS version 4.22.3M"
}
ok: [10.34.0.21] => {
    "msg": "Switch vlab21 runs EOS version 4.24.0F"
}
ok: [10.34.0.102] => {
    "msg": "Switch vlab02 runs EOS version 4.22.3M"
}
ok: [10.34.0.11] => {
    "msg": "Switch vlab11 runs EOS version 4.24.0F"
}
ok: [10.34.0.32] => {
    "msg": "Switch vlab32 runs EOS version 4.24.0F"
}
ok: [10.34.0.31] => {
    "msg": "Switch vlab31 runs EOS version 4.24.0F"
}
ok: [10.34.0.22] => {
    "msg": "Switch vlab22 runs EOS version 4.24.0F"
}

PLAY RECAP ****************************************************************************************************************
10.34.0.101                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --vault-password-file=pf.txt eos_shver.yml  12.53s user 2.54s system 131% cpu 11.467 total
```

Similarly, in this second example, complete files (instead of variables) can also be encrypted.

For instance, starting from the cleartext `hosts` inventory file:

```
# cp hosts ehosts
# ansible-vault encrypt ehosts 
New Vault password: 
Confirm New Vault password: 
Encryption successful
# cat ehosts 
$ANSIBLE_VAULT;1.1;AES256
35636264326362636131373735353039353164633439353631343366613930356630363663333831
3466323463646631333561376338343936646562646565610a653462656530323935626139613132
39386235373832336261373437373062373634303864303266646630633165363464646263353738
3064346664613366320a616331303561376538656134656333343961313738616236336138646262
38353936323064633839376339663163303832656439333963396233323436303166323439333534
38666465646633303437613463313264663038626632333262636164363134623061383636626666
34323837353038383939386466326334303531386334663034323166633962353466343136343766
65646330633666323465373561663730323639313038396137646138616139346334376534633131
34363738363762663237643165393834666534396430333732616263653236636137366363633430
38656364363831623035663339373331326630663863663362643836646334396230396137326531
62386365396233626161323834323563663930663862303538333430663662633863386530353862
63313034386661326439636436303163646435343665613263393937323437636539623362633934
32326661356539666663323366653738356363366161653336313432636432336631666239313135
64346338396238666130303463663461336437346362663662623165386662396134656264306534
38633834623961356531373030646563623336633030306136626136613463366436636465373737
36313835613037383838636465333662656139656462613262323930303136366137383565643965
65656165333430393838343430333662376662643463343430346636313630653434346665636666
66356534393466303634623161336234613837353266306136383439363132636233346664383337
38353539666462666231376531663837633735386132663366633736626131363361626539383964
66656334303736393161353237656365323961633238326265356231623138306530373234363130
33343961346634653435376135323262643134643434333430343439626463646431393339313264
63656366383765653338653530363065303264323866386261323436313233636632343562363030
63343433386566353038356634653436383739306362663133316362616231386332616630393636
61306331353262336533313164363433396162306337326532636362363563323162373133663266
30326537336435356339653363363135336436393134373939616561656330316535383634383561
30353662346631393539616561626366633431316337356239346137333432656361343866353637
64373865663032663663613063343430373933656464386162323234396232326134643361656535
39363064643037343036623031393033653037653735343037363461323830363737353564353339
38646366663634386361643331633663323932643933326161326133633062303034666132643565
62386564316665363436326235383434343261626661353766393035633439313131363738373263
36336136353735373532636364613535333830626464393738396334373932353539646430616465
37326262383132363239366163356638663239646162326461616338653437363163376466383830
37346230313564646465626339346436306634323432383735383736383638366364
# ansible-playbook --ask-vault-pass -i ehosts eos_shver.yml
Vault password: 

PLAY [all] ****************************************************************************************************************

TASK [get eos version and hostname] ***************************************************************************************
ok: [10.34.0.101]
ok: [10.34.0.102]
ok: [10.34.0.12]
ok: [10.34.0.21]
ok: [10.34.0.11]
ok: [10.34.0.31]
ok: [10.34.0.32]
ok: [10.34.0.22]

TASK [debugs] *************************************************************************************************************
ok: [10.34.0.12] => {
    "msg": "Switch vlab12 runs EOS version 4.24.0F"
}
ok: [10.34.0.11] => {
    "msg": "Switch vlab11 runs EOS version 4.24.0F"
}
ok: [10.34.0.101] => {
    "msg": "Switch vlab01 runs EOS version 4.22.3M"
}
ok: [10.34.0.102] => {
    "msg": "Switch vlab02 runs EOS version 4.22.3M"
}
ok: [10.34.0.21] => {
    "msg": "Switch vlab21 runs EOS version 4.24.0F"
}
ok: [10.34.0.22] => {
    "msg": "Switch vlab22 runs EOS version 4.24.0F"
}
ok: [10.34.0.32] => {
    "msg": "Switch vlab32 runs EOS version 4.24.0F"
}
ok: [10.34.0.31] => {
    "msg": "Switch vlab31 runs EOS version 4.24.0F"
}

PLAY RECAP ****************************************************************************************************************
10.34.0.101                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.102                : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.11                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.12                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.21                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.22                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.31                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
10.34.0.32                 : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

ansible-playbook --ask-vault-pass -i ehosts eos_shver.yml  11.03s user 2.11s system 100% cpu 13.012 total
```
