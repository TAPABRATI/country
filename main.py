from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])


def main():
    if request.method=="POST":
        resp = request.form
        a = resp.get('mobnum')
        b = resp.get('pas')


        if ("+91" in a ) and (b == "India"):
            result = "Welcome to India"
            return render_template("country1.html", resp=result,mobnum=a,pas=b)

        elif ("+97" in a ) and (b == "Dubai"):
            result = "Welcome to Dubai"
            return render_template("country2.html", resp=result, mobnum=a,pas=b)

        elif ("+92" in a ) and (b == "Pakistan"):
            result = "Welcome to Pakistan"
            return render_template("country3.html", resp=result, mobnum=a,pas=b)


    else:

        return render_template("input.html")



if __name__ == '__main__':
    app.run(debug=True)
