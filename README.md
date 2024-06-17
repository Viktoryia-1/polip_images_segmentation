Polip segmentation model on tensorflow + flask

Notebook with model code in notebook folder

Testing:
If you want to test the app without image sending,
just run it and go to http://localhost:5454/test


Docker usage:
docker build -t fl_app .
docker run --name app -p 5454:5454 fl_app
