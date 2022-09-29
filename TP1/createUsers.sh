for i in $(seq 0 1000); do
    rig | head -n1 >> names # generate random names
    head -c 100 /dev/urandom | md5sum | cut -f1 -d " " >> pass # generate random passwords
done
paste names pass > users
rm names pass
OLDIFS="$IFS" # Sauvegarde la variable d'environement $IFS. (Voire help read)
IFS=$(echo -e '\t') # Choisi les tabulation comme séparateur.
while read name password;
do
    echo "SELECT create_user('$name', '$password')" | psql -d microblog -U common_user -h 172.28.100.16 -t > /dev/null &
done < users
IFS="$OLDIFS"
wait $(jobs -p)
echo "#Done#