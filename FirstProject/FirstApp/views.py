from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    print("welcome/url is requested and display () is executed");
    ss='''
            <center>
            <h1 style="color:red">
                welcome to django FirstApp
            </h1>
            <hr/>
            </center>
        '''
    return HttpResponse (ss)
def show(request):
        ss='''<!-- 
        HTML webpage to display 'welcome-message' with  different headings 
-->        
        
 <html>
		<head>
			<title>welcome to Django</title>
			<style>
					h1{
						color:blue;
					}
					h2{
						color:green;
					}
					h3{
						color:red;
					}
					h4{
						color:pink;
					}
			</style>
		</head>
		<body>
			<center>
			<h1>hii hello all</h1>
			<hr color="red" width="85%"/>
			<h2>welcome to django html</h2>
			<hr color="red" width="75%"/>
			<h3>this is Qedge technologies</h3>
			<hr color="red" width="65%"/>
			<h4>thank you</h4>
			<hr color="red" width="55%"/>
			</center>
		</body>
</html> 
''';   
        return HttpResponse(ss);
        
        
        
        
        
        
        
        
        
        
        
def hello(request):
        print("hello/ url is required & hello() is executed");
        ss='''
        <html>
            <head>
                    <title>hello webpage</title>
                    <style>
                        h1{
                            color:blue;
                            width:90%
                        }
                        h2{
                            color:green;
                            width:80%
                        }
                        h3{
                            color:red;
                            width:70%
                        }
                        h1,h2,h3{
                                background-color:lightblue;
                                border:2px solid brown;
                    </style>
        </head>
        <body>
                <center>
                    <h1>Hello user...</h1>
                    <hr color='brown' width='80'%/>
                    <h2>welcome to django app</h2>
                    <hr color='red' width='60'%/>
                    <h3>have a good day</h3>
                    <hr color='green' width='40'%/>
                </center>
        </body>
        </html>
        ''';
        
        return HttpResponse(ss)
        
import time;
def senddatetime(request):
            print("dtime/ url is required & senddatetime() is executed");
            ct=time.ctime()
            print("client request data & time on server::",ct);
            ss='''
            <html>
            <head>
                <style>
                    h1{
                        color:blue;
                        width:90%;
                    }
                    h2{
                        color:green;
                        width:80%;
                    }
                    h3{
                        color:red;
                        width:70%
                    }
                    h1,h2,h3{
                        background-color:lightblue;
                        border:2px solid brown;
                    }
                </style>
            </head>
            <body>
                <center>
                    <h1>welcome to django</h1>
                    <hr color='brown' width='80'%/>
                    <h2>server-date & time::</h2>
                    <hr color='brown' width='70'%/>
                    <h3>''',ct,'''</h3>
                    <hr color='brown' width='60'%/>
                </center>    
            </body>
            </html>
            ''';
            return HttpResponse(ss);
            
            
def demo(request):
        print("multiple requests urls same response");
        htmldata='''<center>
                        <h1>welcome demo user</hr>
                        <hr />
                        <h2>This is same-output for diff-multiple-requests-urls</h2>
                        <hr />
                        <h3>Have a great day...</h3>
                        <hr />
                    </center>
                ''';
        return HttpResponse(htmldata);
                
                
#default url request view func
def homepage(request):  
        htmldata='''
                <center>
                    <h1>welcome to DEFAULT Homepage...</h1>
                    <hr />
                    <h2>your request page is NOT-FOUND...</h2>
                    <hr />
                    <h3>Plz try other URL or links...</h3>
                    <hr />
                </center>
            ''';
        return HttpResponse(htmldata);
        
        