#!/bin/bash

### Starts the jupyter notebook which can be accessed from the host Machine
### on port 7888: http://localhost:7888/
jupyter notebook --ip='*' --port 8888  --NotebookApp.token='' --NotebookApp.password='' --allow-root > /tmp/error.log &