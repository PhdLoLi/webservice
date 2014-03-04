select @exits:=count(*) from information_schema.COLUMNS where TABLE_SCHEMA="snmp" AND TABLE_NAME="%s" AND COLUMN_NAME="time";
IF @exits=1 THEN
	SELECT @start_time:=min(time) from yongqian;
	SELECT @end_time:=max(time) from yongqian;
ELSE
END IF;
