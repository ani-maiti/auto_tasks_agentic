echo "Counting characters in each text file..."
wc -c *.txt | tail -n 1 | awk '{print $1}'