import os
import sqlite3
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Target:
    id: int; host: str; program: str

@dataclass
class Finding:
    id: int; target: str; title: str; severity: str; details: str

class Database:
    def __init__(self, path: str):
        self.path = path
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with self._conn() as c:
            c.executescript('''CREATE TABLE IF NOT EXISTS targets(id INTEGER PRIMARY KEY, host TEXT UNIQUE NOT NULL, program TEXT NOT NULL); CREATE TABLE IF NOT EXISTS findings(id INTEGER PRIMARY KEY, target TEXT NOT NULL, title TEXT NOT NULL, severity TEXT NOT NULL, details TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP);''')

    def _conn(self): return sqlite3.connect(self.path)
    def add_target(self, host, program):
        with self._conn() as c: c.execute("INSERT INTO targets(host,program) VALUES(?,?)", (host,program))
    def remove_target(self, host):
        with self._conn() as c: c.execute("DELETE FROM targets WHERE host=?", (host,))
    def targets(self):
        with self._conn() as c: return [Target(*r) for r in c.execute("SELECT id,host,program FROM targets ORDER BY host")]
    def in_scope(self, host):
        with self._conn() as c: return c.execute("SELECT 1 FROM targets WHERE host=?", (host,)).fetchone() is not None
    def add_finding(self, target, title, severity, details):
        with self._conn() as c: return c.execute("INSERT INTO findings(target,title,severity,details) VALUES(?,?,?,?)", (target,title,severity,details)).lastrowid
    def findings(self):
        with self._conn() as c: return [Finding(*r) for r in c.execute("SELECT id,target,title,severity,details FROM findings ORDER BY id DESC")]
    def finding(self, fid):
        with self._conn() as c:
            r=c.execute("SELECT id,target,title,severity,details FROM findings WHERE id=?",(fid,)).fetchone()
            return Finding(*r) if r else None
