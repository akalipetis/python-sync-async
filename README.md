# Python - sync and async code presentation examples from [Open Conf](https://www.open-conf.gr/)

Simple example for comparing synchronous and asynchronous code. In order to test the examples, you can do:

```shell
# Run both servers
docker-compose up -d

# Run the load test for the sync server
docker-compose exec -it sync bash -c 'echo "GET http://localhost:8000/blocked" | vegeta attack -duration=5s | vegeta report'

# Run the load test for the sync server
docker-compose exec -it async bash -c 'echo "GET http://localhost:8000/blocked" | vegeta attack -duration=5s | vegeta report'

# Change the workers used to 8
echo 'WEB_CONCURRENCY=8' > .env
docker-compose up -d

# Run other tests using the different paths for each scenario.a
```