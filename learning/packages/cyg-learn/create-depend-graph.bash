#! /bin/bash
set -e

apt-cyg list > list

echo -n > deps
echo -n > list1
echo "sed -r '" > replacer-l
echo "sed -r '" > replacer-r
i=1
for pack in $(cat list); do
	apt-cyg depends $pack | tail -n +2 >> deps
	printf '%d\t%s\n' $i $pack >> list1
	pattern=$(echo $pack | sed 's/\./\\\./g; s/\+/\\\+/g')
	echo "s/^$pattern > ([^ ]*)\$/$i > \1/g; " >> replacer-l
	echo "s/^([^ ]*) > $pattern\$/\1 > $i/g; " >> replacer-r
	echo $i $pack done
	i=$((i+1))
done
echo "'" >> replacer-l
echo "'" >> replacer-r

echo replacers complete ==============

chmod +x replacer-l
chmod +x replacer-r
cat deps | ./replacer-l | ./replacer-r | sed -r 's/>//g' >deps1

echo deps1 complete =======

cat list1 <(echo "#") deps1 > graph.tgf

