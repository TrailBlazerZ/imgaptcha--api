# imgaptcha--api
A small flask API for image captcha

Install the dependencies as:

	pip install flask
	pip install flask-mysqldb
	sudo apt-get install python-imaging

If you encounter error installing `flask-mysqldb` install`libmysqlclient-dev` first.

`PIL` i.e Python Imaging Library is used to save dynamic images. 

References:

http://flask-mysqldb.readthedocs.org/en/latest/
http://lost-theory.org/python/dynamicimg.html
http://opencvpython.blogspot.in/2012/06/image-derivatives-sobel-and-scharr.html