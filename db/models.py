from peewee import Model, CharField, IPField, ForeignKeyField, SqliteDatabase

DATABASE = 'db/firewalls.db'
db = SqliteDatabase(DATABASE)


class Firewall(Model):
    name = CharField()
    ip_address = IPField()
    location = CharField()

    class Meta:
        database = db

class FirewallRule(Model):
    name = CharField()
    protocol = CharField()
    action = CharField()
    source_ip = IPField()
    source_port = CharField()
    destination_ip = IPField()
    destination_port = CharField()

    class Meta:
        database = db

class FilteringPolicy(Model):
    name = CharField()
    firewall_id = ForeignKeyField(Firewall, backref='policies')
    rule_id = ForeignKeyField(FirewallRule, backref='policies')

    class Meta:
        database = db
