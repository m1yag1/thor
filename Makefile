dump.sql.gz:
	@echo Downloading db dump...
	rsync -tv --progress -e 'ssh -T -c aes128-ctr -o Compression=no -x' backup1.cnx.org:/var/backups/db_dump/20190805_dump.sql.gz ./dump.sql.gz

.PHONY: initdb
initdb: dump.sql.gz
	@echo drop and recreate db then restore dump
	docker-compose exec -u postgres cnx-db dropdb -U postgres repository
	docker-compose exec -u postgres cnx-db createdb -U postgres -O rhaptos repository
	gunzip <dump.sql.gz | docker-compose exec -T -u postgres cnx-db psql -U postgres repository

.PHONY: services
services:
	docker-compose up -d
	@echo Info: To \(re-\)init DB run "make initdb" now.
