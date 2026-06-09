#!/bin/bash
NAMESPACE=${1:-assessment}
echo "========== PODS =========="
kubectl get pods -n $NAMESPACE -o wide
echo
echo "========== SERVICES =========="
kubectl get svc -n $NAMESPACE
echo
echo "========== EVENTS =========="
kubectl get events -n $NAMESPACE --sort-by=.metadata.creationTimestamp | tail -30
echo
POD=$(kubectl get pods -n $NAMESPACE -o jsonpath='{.items[0].metadata.name}')
echo "========== DESCRIBE POD: $POD =========="
kubectl describe pod $POD -n $NAMESPACE
echo
echo "========== LOGS: $POD =========="
kubectl logs $POD -n $NAMESPACE --tail=80
echo
echo "Send this output to Claude/AI and ask: Identify root cause and provide remediation steps."