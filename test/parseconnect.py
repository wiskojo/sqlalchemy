from testbase import PersistTest
import sqlalchemy.engine.url as url
import unittest
        
class ParseConnectTest(PersistTest):
    def testrfc1738(self):
        for text in (
            'dbtype://username:password@hostspec:110//usr/db_file.db',
            'dbtype://username:password@hostspec/database',
            'dbtype://username:password@hostspec',
            'dbtype://username:password@/database',
            'dbtype://username@hostspec',
            'dbtype://username:password@127.0.0.1:1521',
            'dbtype://hostspec/database',
            'dbtype://hostspec',
            'dbtype:///database',
            'dbtype:///:memory:',
            'dbtype:///foo/bar/im/a/file',
            'dbtype:///E:/work/src/LEM/db/hello.db',
            'dbtype://',
            'dbtype://username:password@/db'
        ):
            u = url.make_url(text)
            print u, text
            print u.username, u.password,  u.database
            assert str(u) == text

            
if __name__ == "__main__":
    unittest.main()
        