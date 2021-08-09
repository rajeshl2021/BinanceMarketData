# Binance Market Data Query Application
Binance Market Data query Application is a python / Flask based webservice which provides access to Biance Market data using REST API. 
Client access to this webservice is provided by a simple web gui form. The form is loaded with the list of exchange supported symbols.
User  need to select the symbol and submit "Show/Refresh" button to dispaly the latest market data snapshot for 20 depth levels.

####  Project Structure
```
-> docker-compose.yaml
-> app
   -> binance
      -> __init__.py
      -> binance_market_data.py        
   -> static
      -> style
   -> templates
      -> index
   -> app.py
   -> Dockerfile
   -> requirements
```
####  Deploy with docker-compose
```
$ docker-compose up -d


Creating network "binancemdqueyapp_default" with the default driver
Building web
[+] Building 3.6s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 208B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.7-alpine                                               3.2s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 8.34kB                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.7-alpine@sha256:124e9c6480fdd640e28453bbf94cd2b31642f661887f9d319f119b6  0.0s
 => CACHED [2/5] WORKDIR /app                                                                                      0.0s
 => CACHED [3/5] COPY requirements.txt /app                                                                        0.0s
 => CACHED [4/5] RUN pip3 install -r requirements.txt --no-cache-dir                                               0.0s
 => [5/5] COPY . /app                                                                                              0.1s
 => exporting to image                                                                                             0.1s
 => => exporting layers                                                                                            0.1s
 => => writing image sha256:b2aca2c3e41511972d6dfd58a2d6404c4f94793b55c36044a28a9de12f8c162e                       0.0s
 => => naming to docker.io/library/binancemdqueyapp_web                                                                    0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating binancemdqueyapp_web_1 ... done

```



## Expected result
```
$ docker-compose  images
  Container       Repository     Tag       Image Id       Size
----------------------------------------------------------------
binancemdqueyapp_web_1   binancemdqueyapp_web   latest   b2aca2c3e415   55.29 MB
```


####  Listing containers must show one container running and the port mapping as below:
```
$ docker ps

CONTAINER ID   IMAGE          COMMAND            CREATED         STATUS         PORTS                                       NAMES
b022b5fc5e67   binancemdqueyapp_web   "python3 app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   binancemdqueyapp_web_1
```
After the application starts, navigate to http://localhost:5000 in your web browser or run:

This will display a index page, preloaded with all the exchange supported symbols in Binance.

Based on the user selection of the symbol, upon clicking the Show/Refresh button market data book snapshot with 20 book depth will be displayed.


####  Stop and remove the containers
```
docker-compose down
```
