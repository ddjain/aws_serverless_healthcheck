# aws_serverless_healthcheck
Health check job to monitor services

### sample event dict
`{
  "url": "TARGET_URL",
  "code": EXPECTED_HTTP_RESPONSE_CODE,
  "serviceName": "SERVICE_NAME",
  "slack_url": "SLACK_HOOK_ENDPOINT"
}`
