update salary set sex= CASE sex when 'm' THEN 'f' ELSE 'm' END
# update salary set sex=if(sex='m','f','m')
