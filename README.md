# serverless-framework-sample
serverless-framework-sample

# Run apigw-service

You need to modify the bucket name to change your acutual bucket in `serverless.yml`

Deploy the serverless.yml to Cloudformation stack
```
serverless deploy
```


# Run lambda-service

- You need to modify the bucket name to change your acutual bucket in `serverless.yml`
- You need to modify the `restApiId` & `restApiRootResourceId` to your API GW created above

Deploy the serverless.yml to Cloudformation stack
```
serverless deploy
```
