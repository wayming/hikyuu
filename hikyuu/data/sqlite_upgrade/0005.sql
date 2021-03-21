BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Holiday" (
	"id"	INTEGER,
	"date"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Holiday" VALUES (1,20210101);
INSERT INTO "Holiday" VALUES (2,20210211);
INSERT INTO "Holiday" VALUES (3,20210212);
INSERT INTO "Holiday" VALUES (4,20210215);
INSERT INTO "Holiday" VALUES (5,20210216);
INSERT INTO "Holiday" VALUES (6,20210217);
INSERT INTO "Holiday" VALUES (7,20210405);
INSERT INTO "Holiday" VALUES (8,20210501);
INSERT INTO "Holiday" VALUES (9,20210503);
INSERT INTO "Holiday" VALUES (10,20210504);
INSERT INTO "Holiday" VALUES (11,20210505);
INSERT INTO "Holiday" VALUES (12,20210614);
INSERT INTO "Holiday" VALUES (13,20210920);
INSERT INTO "Holiday" VALUES (14,20210921);
INSERT INTO "Holiday" VALUES (15,20211001);
INSERT INTO "Holiday" VALUES (16,20211004);
INSERT INTO "Holiday" VALUES (17,20211005);
INSERT INTO "Holiday" VALUES (18,20211006);
INSERT INTO "Holiday" VALUES (19,20211007);

UPDATE `version` set `version` = 5;
COMMIT;