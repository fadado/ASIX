#!/bin/bash
# form.sh

# Test CGI script.
# Shows query string or request body.

echo -ne "Content-Type: text/plain; charset=UTF-8\r\n"
echo -ne "\r\n"

if [[ $REQUEST_METHOD == 'GET' ]]
then
	echo "$QUERY_STRING"
else
	read -r -n "$CONTENT_LENGTH" body
	echo "$body"
fi

exit
