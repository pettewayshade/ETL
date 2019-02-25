from flask import Flask, request, render_template
import pymysql
from sqlalchemy import create_engine
import pandas as pd
    
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", data='')

@app.route('/data')
def getdata():
    try:
        from config import username, password, database
        rds_connection_string = ("root:"+password+"@127.0.0.1:3306/etlproject")
        engine = create_engine(f'mysql://{rds_connection_string}')
        f = 'yes'
        print(f)
    except ModuleNotFoundError:
        f = 'no'                                                                
        
    if f == 'yes':
        final = pd.read_sql_query('select * from final', con=engine).head(50)
        final = final.to_html()
        finaldict = {
                "final": final
                }             
        return render_template("index.html", data=finaldict)
    
    if f =='no':
        with open('finalcsvtohtml', 'r') as myfile:
                final = myfile.read()
        finaldict = {
                "final":final
                }
        return render_template("index.html", data=finaldict)
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
if __name__ == '__main__':
	app.run(debug=True)
