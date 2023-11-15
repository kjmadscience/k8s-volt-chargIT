FROM voltdb/voltdb-enterprise:10.2.20

ARG volt_uid=1001
ARG volt_gid=1001 

WORKDIR /opt
# Replace with your custom JAR
COPY DeleteChargingDemoData.jar /opt/DeleteChargingDemoData.jar

USER 1001:1001

WORKDIR /opt

CMD exec /bin/sh -c "trap : TERM INT; sleep 9999999999d & wait"
