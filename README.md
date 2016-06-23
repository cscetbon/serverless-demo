##Requirements

This serverless repository requires version 0.5.3
```
npm install -g serverless@0.5.3
```

##Deployment

```
make install
```

If this is the first time:

```
sls project init
```

Finally:

```
sls function deploy -a
sls endpoint deploy -a
sls event deploy -a
```

##Testing:

To test the code you just have to send some images (small less than 100k) using 

```
python tools/post_image.py ~/Pictures/Neo.jpg|curl -X POST ${endpoint}/dev/image -d @- -H "Content-Type: 
application/json"
```

Then you can count the number of images for a defined type using

```
curl '${endpoint}/dev/image/jpeg'
```