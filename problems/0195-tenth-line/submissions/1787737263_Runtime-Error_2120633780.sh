l=$(wc -l < a.txt)
txt=$(sed -n '10p file.txt) 
if ["$l" -ge 10]; then
echo '$txt'
else 
echo ''
fi
