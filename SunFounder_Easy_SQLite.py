'''
**********************************************************************
* Filename      : SunFounder_Easy_SQLite
* Description   : Very simple sqlite module
* Author        : Cavon
* E-mail        : service@sunfounder.com
* Website       : www.sunfounder.com
* Update        : Cavon    2016-12-02     V1.0.1
**********************************************************************
'''
import sqlite3

class DB(object):

    def __init__(self, db_name, table_name='default_table'):
        self.db_name = db_name
        self.table_name = table_name
        if not self.is_table_exist():
            self.create_table()

    def get(self, name, default=None):
        db = sqlite3.connect(self.db_name)
        try:
            cmd = 'SELECT * FROM %s WHERE name="%s"' % (self.table_name, name)
            print cmd, 
            value = db.execute(cmd)
            value = value.fetchall()
            #print "Value", value
            value = value[0][1]
            print 'done'
        except Exception, e:
            print e
            print 'error, use default value'
            value = default
        finally:
            db.close()

        return value

    def set(self, name, value):
        db = sqlite3.connect(self.db_name)
        if self.is_name_exist(name):
            print 'value exist'
            cmd = 'UPDATE %s SET value = %s WHERE name="%s"' % (self.table_name, value, name)
            print cmd, 
            db.execute(cmd)
            print 'done'
        else:
            print "INSERT value...",
            cmd = 'INSERT INTO %s(name, value) VALUES ("%s", %d)' % (self.table_name, name, value)
            print cmd, 
            db.execute(cmd)
            print 'done'
        db.commit()
        db.close()

    def remove(self, name):
        db = sqlite3.connect(self.db_name)
        if self.is_name_exist(name):
            print 'value exist'
            cmd = 'DELETE from %s WHERE name="%s"' % (self.table_name, name)
            print cmd, 
            db.execute(cmd)
            print 'done'
            result = True
        else:
            result = False
        db.commit()
        db.close()
        return result

    def delete(self, name):
        self.remove(name)

    def get_all(self):
        dic = {}
        db = sqlite3.connect(self.db_name)
        try:
            cmd = 'SELECT * FROM %s' % (self.table_name)
            value_count = db.execute(cmd)
            value_count = value_count.fetchall()
            for row in value_count:
                dic[row[0]] = int(row[1])
        except Exception, e:
            print e
        finally:
            db.close()

        return dic

    def is_table_exist(self):
        db = sqlite3.connect(self.db_name)
        try:
            cmd = 'select * from %s' % (self.table_name)
            value_count = db.execute(cmd)
            result = True
        except:
            result = False
        finally:
            db.close()
            return result

    def create_table(self):
        db = sqlite3.connect(self.db_name)
        try:
            print "Creating a Table...",
            cmd = 'create table %s (name varchar(20), value int)' % (self.table_name)
            db.execute(cmd)
            print "done";
        except:
            print "skiped"
            print "Skip, %s table is already exist." % self.table_name
        finally:
            db.close()

    def is_name_exist(self, name):
        if self.get(name, default=False):
            return True
        else:
            return False

if __name__ == '__main__':
    db=DB('test.db')

    print 'get value a as default = False'
    a = db.get('a', default=False)
    print 'a = ', a

    print 'get value c as default = False'
    c = db.get('c', default=False)
    print 'c = ', c

    print 'set a to 13'
    db.set('a', 13)
    print 'a set to 13'

    print 'set c to 24'
    db.set('c', 24)
    print 'c set to 24'

    print 'get value a as default = False'
    a = db.get('a', default=False)
    print 'a = ', a

    print 'get value c as default = False'
    c = db.get('c', default=False)
    print 'c = ', c

    print "\nSumary:"
    db.sumary()

    print 'set a to 45'
    db.set('a', 45)
    print 'a set to 45'

    print 'set c to 67'
    db.set('c', 67)
    print 'c set to 67'

    print 'get value a as default = False'
    a = db.get('a', default=False)
    print 'a = ', a

    print 'get value c as default = False'
    c = db.get('c', default=False)
    print 'c = ', c

    print "\nSumary:"
    db.sumary()
