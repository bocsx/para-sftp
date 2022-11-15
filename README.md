# para-sftp - A parallel sFTP client
An sftp client that can handle several connections in parallel.

The purpose is to support m2m file up- and downloads.

## Usage
para-sftp options

## Options
-c connect_string

-k private_key_file

-b batch_file

-m - maximum number of connections in parallel

-d - delete local files after upload

-r - delete remote files after download

## Example
para-sftp -m 2 -d -c user1@sftp-site.hu:2222 -k priv.key -b b1.sftp -c user2:password123@other-site.hu:2224 -b b2.sftp -b b3.sftp
