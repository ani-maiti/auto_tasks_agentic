echo "Identifying potential government open data portals..."
curl -s https://www.data.gov/ | grep -oP '(?<=href=")[^"]+(?=")' | grep -E 'data\.gov' | sort -u | head -n 10