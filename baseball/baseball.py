from flask import Flask, request, render_template, redirect

app = Flask(__name__) # Double Underscore (__)

@app.route('/')
def hello():
    return '<h1> Hello, World! I am here</h1>'

result = []
output = []
@app.route('/get-input/', methods=['GET', 'POST'])
def user_form():
    user_input = request.form.get('text', None)
    alert = None
    total = None
    if user_input is not None:
        if len(result) == 0:
            try:
                if user_input.isdigit():
                    result.append(int(user_input))
                else:
                    alert = "First input cannot be string"
            except AttributeError:
                pass
        elif len(result) == 1:
            try:
                if user_input.isdigit():
                    result.append(int(user_input))
                else:
                    alert = "Second digit cannot be string"
            except AttributeError:
                pass
        elif len(result) > 1:
            if user_input.upper() == "+":
                x = result[-1] + result[-2]
                result.append(x)
                total = sum(result)
            elif user_input.upper() == "D":
                x = result[-1]*2
                result.append(x)
            elif user_input.upper() == "C":
                result.pop()
            else:
                try:
                    if user_input.isdigit():
                        result.append(int(user_input))
                except AttributeError:
                    pass

    return render_template('form.html', result=result, alert=alert, total=total)


@app.route('/clear-input/')
def clear_input():
    result.clear()
    return redirect('/get-input/')

# result = []
# @app.route('/get-input/', methods=["POST",])
# def get_input():
#     user_input = request.form['text']
#     if len(result) > 1:
#         if (result[0], result[1]) is int:
#             if user_input == "+":
#                 x = result[-1] + result[-2]
#                 result.append(x)
#             elif user_input == "D":
#                 x = result[-1]*2
#                 result.append(x)
#             elif user_input == "C":
#                 result.pop()
#             else:
#                 result.append(int(user_input))
#     else:
#         if user_input == "+":
#             x = result[-1] + result[-2]
#             result.append(x)
#         elif user_input == "D":
#             x = result[-1]*2
#             result.append(x)
#         elif user_input == "C":
#             result.pop()
#         else:
#             result.append(int(user_input))
#             return f"<h1> Your input is {user_input} Do not input C or D as either of the first two input</h1>"




