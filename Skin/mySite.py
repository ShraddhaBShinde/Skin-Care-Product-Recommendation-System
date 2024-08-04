from flask import *
from werkzeug import secure_filename
import cv2
from skincare import predict

image_path = ''

app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/',methods=['GET','POST'])
def asl():
    global image_path
    if request.method == 'POST':
        if request.form['sub'] == 'Upload':
            im = request.files['ct_scan']
            im.save('static/images/' + secure_filename(im.filename))
            image_path = 'static/images/'+ secure_filename(im.filename)
            print(image_path)

            return render_template('asl.html',image_path=image_path)

        if request.form['sub'] == 'Test':
            result = predict(image_path)
            return render_template('asl.html',image_path=image_path,result=result)

    return render_template('asl.html', image_path = 'b1.jpeg')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    #app.run()