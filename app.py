from flask import Flask
app = Flask(__name__)
 
@app.route(&amp;quot;/&amp;quot;)
    def hello():
        return &amp;quot;Hello World!&amp;quot;
 
if __name__ == &amp;quot;__main__&amp;quot;:
    app.run()