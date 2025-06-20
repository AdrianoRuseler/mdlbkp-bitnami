FROM alpine:latest

RUN apk update && apk add --no-cache openldap openldap-back-mdb openldap-clients lmdb

RUN mkdir -p /var/lib/openldap /etc/openldap/slapd.d /run/slapd

COPY slapd.conf /etc/openldap/slapd.conf
COPY DB_CONFIG /var/lib/openldap/DB_CONFIG

RUN chown -R ldap:ldap /var/lib/openldap /etc/openldap /run/slapd && \
    chmod -R 700 /var/lib/openldap /etc/openldap/slapd.d

EXPOSE 389 636

CMD ["slapd", "-d", "256", "-h", "ldap:/// ldaps:///", "-u", "ldap", "-g", "ldap"]
